import requests
from bs4 import BeautifulSoup
import csv
from pandas import read_csv
import io


def main():
    # Load list of links for each job listing in NoFluffJobs
    data = read_csv("nfj_links.csv")
    nfj_urls = data["url"].tolist()

    # Create list to store results
    results = []

    # Iterate through all urls in list to get data and append it to "results" list
    for url in nfj_urls:
        data = get_nfj_data(f"http://nofluffjobs.com{url}")
        try:
            results.append(data)
        except AttributeError:
            continue
        except requests.exceptions.RequestException:
            continue
        print(data)

    # Open a new file in write mode
    with io.open('job_listings.csv', 'w', newline='') as csvfile:
    # Create a CSV writer
        writer = csv.DictWriter(csvfile, fieldnames=['listing_name', 'categories', 'seniority', 'required_skills'])

        # Write column names
        writer.writeheader()

        # Iterate over the list of dictionaries and write each one to the CSV file
        
        for result in results:
            try:
                writer.writerow({
                    'listing_name': result['listing_name'],
                    'categories': result['categories'],
                    'seniority': result['seniority'],
                    'required_skills': result['required_skills']
                })
            except TypeError:
                continue


def get_nfj_data(url):
    """
    Scrape data from from each job listing. Data to be scraped:
    Name of listing
    Category of listing (DevOps, Data Engineer etc.)
    Experience (Intern, Junior, Mid, Senior, Lead)
    Skills
    :param link: Link to be scraped
    :type link: String
    :raise !!!!!!! TypeError: If n is not an int --- explains what error might be raised by func
    :return: Data meant to be scraped, listed above
    :rtype: Dictionary
    """
    # Make an HTTP GET request to the website
    response = requests.get(url)

    # Parse the HTML of the webpage
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the information about listing's name
    try:
        listing_name = soup.find('h1', class_='font-weight-bold').text
    except AttributeError:
        return None

    # Find the category names in elements with the attribute "commonpostingcattech"
    categories = []
    for li in soup.find_all('li', attrs={"commonpostingcattech": True}):
        for a in li.find_all('a'):
            categories += [a.text]


    # Find the seniority in the element with the id "posting-seniority"
    seniority = soup.find('li', id='posting-seniority').span.text

    # Find the required skills in elements with the attribute "commonpostingitemtag"
    required_skills = [li.text for li in soup.find_all('li', attrs={"commonpostingitemtag": True})]

    # Store the data in a dictionary and return it
    data = {
        "listing_name": listing_name,
        "categories": categories,
        "seniority": seniority,
        "required_skills": required_skills
    }
    return data


if __name__ == "__main__":
    main()
