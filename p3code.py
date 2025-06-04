from bs4 import BeautifulSoup
import requests
import datetime

url = "https://techcrunch.com/latest/"
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")

print("Connection Check:", page) # checks if connection is successful

articles = soup.find_all("div", class_="loop-card__content") 
author_list = []
author_dict = {}

# Questions 1-3
# 1. What are the latest article titles on TechCrunch?
# 2. Who are the authors of these articles?
# 3. What are the publication dates?
for article in articles: # loops through each article
    title = article.find("a", class_="loop-card__title-link")
    author = article.find("a", class_="loop-card__author")
    date = article.find("time", class_="loop-card__time")
 
    if (author != None):
        author_list.append(author.text)

    # gets rid of loop-cards that are not articles just in case
    if (author != None and date != None): 
        print(title.text)
        print(author.text)
        print(date.text.strip())

        print()

# 4. Plot the number of articles is written by each author on the homepage?
for author in author_list:
    if author in author_dict:
        author_dict[author] += 1
    else:
        author_dict[author] = 1

'''
# 5. Plot the distribution of article publication hours over a 24-hour period?
# 6. Plot the number of articles published each day over the course of one week?
datetime_list = []
datetime_dict = {}

for article in soup.find_all("time"):
    if article.has_attr("datetime"):
        datetime_list.append(article["datetime"])

hour = 0
month = 0
day = 0
        
for dt in datetime_list:
   
    if hour < 10:
        hourstr = "T0" + str(hour) + ":"
    elif (25 > hour > 9):
        hourstr = "T" + str(hour) + ":"

    if month < 10:
        monthstr = "-0" + str(month) + "-"
    elif (9 < month < 32):
        monthstr = "-" + str(month) + "-"

    if day < 10:
        daystr = "-0" + str(day) + "T"
    elif (9 < month < 32):
        daystr = "-" + str(day) + "T"

    if hourstr in dt:
        datetime_dict[hour] += 1
    elif (25 > hour):
        datetime_dict[hour] = 1
        hour += 1

    # figure out code regarding months days and days of the week

print(datetime_dict)
'''

'''
logic notes
4. Plot the number of articles is written by each author on the homepage?
- use dictionary to keep count of authors
- plot

5. Plot the distribution of article publication hours over a 24-hour period?
- figure out how to get code of 24 hour period
- use datetime???
- use a counter
- plot

6. Plot the number of articles published each day over the course of one week?
- use same code above
- separate by days of week
- use a counter per day
- plot
'''