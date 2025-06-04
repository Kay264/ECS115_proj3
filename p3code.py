from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt
from datetime import datetime

url = "https://techcrunch.com/" # used https://techcrunch.com/latest for prob #1-3
page = requests.get(url)
print("Connection Check:", page) # checks if connection is successful

soup = BeautifulSoup(page.text, "html.parser")
articles = soup.find_all("div", class_="loop-card__content") # goes through divs containing article

author_list = [] # list of authors to count
author_dict = {} # dictionary of authors for bar graph

hour_list = [] # list of hours to count
hour_dict = {} # dictionary of hours for bar graph

date_list = [] # list of dates to count
date_dict = {} # dictionary of dates for bar graph
# list of weekdays, each is associated with an integer
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"] 


# Questions 1-3
# 1. What are the latest article titles on TechCrunch?
# 2. Who are the authors of these articles?
# 3. What are the publication dates?
for article in articles: # loops through each article
    title = article.find("a", class_="loop-card__title-link")
    author = article.find("a", class_="loop-card__author")
    date = article.find("time", class_="loop-card__time")

    # gets rid of loop-cards that are not articles
    if (author != None and date != None): 

        datetime_str = date.get('datetime') # string of datetime link
        date_obj = datetime.strptime(datetime_str[:10], "%Y-%m-%d") # ONLY gets the date
        hour_obj = datetime_str[11:13] # ONLY gets the hour

        author_list.append(author.text) # add to list of authors
        hour_list.append(hour_obj) # add to list of hours
        date_list.append(weekdays[date_obj.weekday()]) # add to list

        # prints latest article titles, authors, and dates
        print(title.text)
        print(author.text)
        print(date.text.strip())
        print(date.get('datetime'))

        print()


# 4. Plot the number of articles is written by each author on the homepage?
for author in author_list: # go through list of authors
    if author in author_dict: # if author already exists
        author_dict[author] += 1 # add 1
    else: # if author doesn't exist
        author_dict[author] = 1 # make it, start with 1

# Bar graph of authors
plt.bar(range(len(author_dict)), list(author_dict.values()), align='center')
plt.xticks(range(len(author_dict)), list(author_dict.keys()))
plt.show()      


# 5. Plot the distribution of article publication hours over a 24-hour period?
for hour in hour_list: # go through list of hours
    if hour in hour_list: # if hour already exists
        hour_dict[hour] += 1 # add 1
    else: # if it doesn't exist
        hour_dict[hour] = 1 # make it, start with 1

# Bar graph of how many articles are published per hour
plt.bar(range(len(hour_dict)), list(hour_dict.values()), align='center')
plt.xticks(range(len(hour_dict)), list(hour_dict.keys()))
plt.show()


# 6. Plot the number of articles published each day over the course of one week?
for dt in date_list: # go through list of weekdays
    if dt in date_list: # if weekday already exists
        date_dict[dt] += 1 # add 1
    else: # if it doesn't exist
        date_dict[dt] = 1 # make it, start with one

# Bar graph of how many articles are published per weekday
plt.bar(range(len(date_dict)), list(date_dict.values()), align='center')
plt.xticks(range(len(date_dict)), list(date_dict.keys()))
plt.show()