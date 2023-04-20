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
    Removes duplicate URLs that have the same beginning in a list of URLs.

    :param links: List of URLs to be cleared of duplicates.
    :type links: List of strings
    :raises: None
    :return: A new list of URLs without duplicates for the same location.
    :rtype: List of strings
    """
    # Create an empty list to store the unique urls
    unique_strings = []

    # Iterate over each url in the input list
    for s in links:
        # Skip empty strings and check if the first 16 characters of the current url match
        # the first 16 characters of any url in the list of unique urls
        if not s or s[:16] in [x[:16] for x in unique_strings]:
            continue
        # If the current url is unique, add it to the list of unique urls
        unique_strings.append(s)

    return unique_strings


def get_jjit_data(link: str) -> dict:
    """
    Scrape data from a job listing webpage on the Just Join IT website.

    :param link: str, the link of the job listing webpage on the Just Join IT website
    :type link: str
    :raise TypeError: if link is not a str
    :return: A dictionary containing the scraped data for the given job listing webpage.
             Keys in the dictionary:
                 - 'listing_name': str, the name of the job listing
                 - 'categories': str, the category of the job listing
                 - 'seniority': str, the required experience level for the job
                 - 'required_skills': list of str, the required skills for the job
    :rtype: dict
    """

    # If link parameter is not string raise TypeError
    if not isinstance(link, str):
        raise TypeError("The link argument must be a string")

    # Create session instance
    s = requests.Session()

    # Define base url
    url = f"https://justjoin.it/api/offers/{link}"

    # Make a GET request to URL
    data = s.get(url)

    # Format the response as JSON
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