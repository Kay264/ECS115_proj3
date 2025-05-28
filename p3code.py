from bs4 import BeautifulSoup
import requests

url = "https://techcrunch.com/"
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")

print("Connection Check:", page)

# print(soup) # all of html
soup.find_all("loop-card__title-link")
print(soup.find_all("h3", class_="loop-card__title")) # article titles (wip)