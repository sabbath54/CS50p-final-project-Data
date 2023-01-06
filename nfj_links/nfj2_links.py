import requests
from bs4 import BeautifulSoup

# Make a request to the website
response = requests.get('https://nofluffjobs.com/pl/Python?gclid=CjwKCAiAy_CcBhBeEiwAcoMRHPy1h93drfenR1DoO7CYBQ4HIoXLV0CVdcfn431PCxxIj7Oxw7vFDhoC1_wQAvD_BwE&page=2')

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

links = []

a_elements = soup.find_all('a', attrs={'nfj-postings-item': '', 'id': lambda x: x and x.startswith('nfjPostingListItem-')})
for a in a_elements:
    links.append(a['href'])

i = 0
for link in links:
    i +=1
    print(f"{i}{link}")
    