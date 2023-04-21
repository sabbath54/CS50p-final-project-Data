# What skills do I need?

#### Video Demo: <https://youtu.be/0gKqUfIXRBI>

#### Description:

My Name is Lukasz Marszalek, I come from Poland, Wrocław, and this is my CS50p final project!

This project main objective was to find what skills are most usefull to get a Python-related job in Polish IT industry.

Project contains three separate parts:
- Scraping
- Data preparation
- Data visualisation
More about all of those below

#### Usage

```
streamlit run project.py
```

#### Scraping

To meet objectives first I had to gather data. To do that I decided to scrapes two most popular job-boards in Poland nofluffjobs.com and justjoin.it. They both allow scraping and you can find it in their robots.txt file. I obtained four types of information:
- Listing name
- Category of listing
- Seniority of listing
- Required skills for the role
For both webpages I had to use different techniques to scrape. In first condition I had to parse HTML code and then extract parts of website of interest to me and in second condition I just had to get JSON response from webpage API and then extract the data.

#### Data preparation

To prepare the data I used Pandas library in Jupyter. First I removed all records with missing values and then I had to match categories, seniorities and skill names from both webpages, as they had different names for categories and diffrent style of storing data. I also had to remove irrelevant categories that required python skills but only optionaly and they were focused on different programming languages. Last thing to do before visualasing data was to merge both data frames.

#### Data visualisation

To present the data I used streamlit app. As the project asked just one question there is only one bar chart that visualise the results. User is allowed to chose which categorie of job and what seniority is of interest to him and then he can see the top 15 skills on bar chart, top16-50 listed under chart and individual listings that fits filters below.