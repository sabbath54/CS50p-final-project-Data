from jjit_links import Jjit_links


def main():
    # Create list of links for each job listing in JustJoinIt
    jjit_urls = Jjit_links()


def get_jjit_data(links)
    """
    Scrape data from from each job listing. Data to be scraped:
    Name of company
    Location (Remote or exact city)
    Listing name instead of in other scraper Category of listing (DevOps, Data Engineer etc.)
    Experience (Intern, Junior, Mid, Senior, Lead)
    Tech stack instead of mandatory and nice to have skills
    Salary
    :param links: Links to be scraped
    :type links: List of strings
    :raise !!!!!!! TypeError: If n is not an int --- explains what error might be raised by func
    :return: All data selected to be scraped for each listing
    :rtype: list of dictionaires
    """