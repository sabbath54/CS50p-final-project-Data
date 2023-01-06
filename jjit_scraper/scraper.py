import requests
from collections import Counter

def main():
    print(get_jjit_data())

def get_jjit_data():
    s = requests.session()

    # Define API Url
    url_search = "https://justjoin.it/api/offers/search?keywords[]=python&keywords[]=junior"

    # Define Header for get request
    headers = {'User-Agent': 'python-requests/2.28.1', 'Accept-Encoding': 'gzip, deflate, br', 'Accept': '*/*', 'Connection': 'keep-alive'}

    # Get data from
    x = s.get("https://justjoin.it/api/offers/search?keywords[]=python", headers = headers)

    #
    x = x.json()

    # Create list with all skills needed for the job
    skills = []
    for i in x:
        skill = i["skills"]
        skills.append(skill)


    # Sum find most needed skill in skills list
    result = []
    for skill in skills:
        for _dict in skill:
            result.append(_dict["name"])


    return Counter(result).most_common(20)



if __name__ == "__main__":
    main()

