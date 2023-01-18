import requests
import csv

def main():
    # Get URLs
    links = Get_jjit_links()
    # Clean list of URLs from duplicates for same location
    links = clear_links(links)

    # Create list in which all data will be stored
    data = []
    # Itereate over all URLs to be scraped, get data for each and append returned dictionaries to the list
    for link in links:
        data.append(Get_jjit_data(link))

    # Open a new file in write mode
    with open("job_listings.csv", "w", newline="") as csvfile:
    # Create a CSV writer
        writer = csv.DictWriter(csvfile, fieldnames=["listing_name", "categories", "seniority", "required_skills"])
        
        # Write column names
        writer.writeheader()

        # Iterate over the list of dictionaries and write each one to the CSV file
        for result in data:
            try:
                writer.writerow({
                    "listing_name": result["listing_name"],
                    "categories": result["categories"],
                    "seniority": result["seniority"],
                    "required_skills": result["required_skills"]
                })
            except UnicodeEncodeError:
                print(result["listing_name"])
                continue



def Get_jjit_links():
    # Create session instance
    s = requests.Session()

    # Define url to scrape
    url = "https://justjoin.it/api/offers/search?keywords[]=python"

    # Scrape the data
    data = s.get(url)

    # Turn data into JSON file
    data = data.json()

    # Create list to store URLs
    links = []

    #Iterate over all URLs and append them to list
    for result in data:
        links.append(result["id"])

    return links

def clear_links(links):
    """
    List of links contains multiple urls for same listing but in different locations, this func clear urls that has the same beginning
    :param links: List of urls to be cleared
    :type links: List of strings
    :return: List of urls without duplicates for same location
    :rtype: List of strings
    """
    unique_strings = []
    for s in links:
        if not s or s[:16] in [x[:16] for x in unique_strings]:
            continue
        unique_strings.append(s)
    return unique_strings


def Get_jjit_data(link):
    """
    Scrape data from from each job listing. Data to be scraped:
    Listing name
    Category of listing
    Experience (Intern, Junior, Mid, Senior, Lead)
    Tech stack
    :param link: Link of webpage to be scraped
    :type link: String
    :raise !!!!!!! TypeError: If n is not an int --- explains what error might be raised by func
    :return: Listing name, category, required skills and seniority
    :rtype: Dictionary
    """
    # Create session instance
    s = requests.Session()

    # Define base url
    url = f"https://justjoin.it/api/offers/{link}"

    # Make GET request
    data = s.get(url)

    # Format request as JSON
    data = data.json()

    # Create empty list to store skills
    required_skills = []
    # Iterate through all results in skills category
    for skill in data["skills"]:
        required_skills.append(skill["name"])

    # Create and return dictionary containing all scraped data for single webpage
    final_data = {
        "listing_name": data["title"],
        "categories": data["marker_icon"],
        "seniority": data["experience_level"],
        "required_skills": required_skills
    }

    return final_data


if __name__ == "__main__":
    main()