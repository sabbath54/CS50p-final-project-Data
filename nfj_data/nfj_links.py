import requests
from bs4 import BeautifulSoup
import csv

def main():
  # Get set of links
  data = Nfj_links()
 
 # Open CSV file in writer mode
  with open("nfj_links.csv", "w", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=["url"])
    
    # Write header to CSV file
    writer.writeheader()
    
    # Write URLs to CSV file
    for result in data:
      writer.writerow({
        "url": result
      })

def Nfj_links():
    """
    Scrape links of job listings from 16 pages on Nofluffjobs website.
    :return: Set of links
    :rtype: Set
    """

  # Initialize an empty set to store the links
  links = set()

  # Loop through all the pages
  for page_number in range(1, 17):
    # Send an HTTP request to the URL of the current page
    url = f"https://nofluffjobs.com/pl/Python?gclid=CjwKCAiAy_CcBhBeEiwAcoMRHPy1h93drfenR1DoO7CYBQ4HIoXLV0CVdcfn431PCxxIj7Oxw7vFDhoC1_wQAvD_BwE&page={page_number}"
    page = requests.get(url)

    # Parse the HTML content
    soup = BeautifulSoup(page.content, 'html.parser')

    # Find all <a> elements with specified attribute and id
    a_elements = soup.find_all("a", attrs={"nfj-postings-item": "", "id": lambda x: x and x.startswith("nfjPostingListItem-")})
    for a in a_elements:
      links.add(a["href"])
      print(a["href"])


  # Return the list of links
  return links


if __name__ == "__main__":
    main()
