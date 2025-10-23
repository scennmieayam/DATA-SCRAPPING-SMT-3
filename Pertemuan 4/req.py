import requests
# import os
from bs4 import BeautifulSoup
import scrapp
# result = requests.get("https://www.detik.com")
# print(result)
# print(result.encoding)
# print(result.status_code)
# print(result.elapsed)
# print(result.url)
# print(result.history)
# print(result.headers['Content-Type'])

#Logic

# def main_scraper(url,directory):
#     scrapp.create_directory(directory)
#     source_code = requests.get(url)
#     source_text = source_code.text
#     print(source_text)

# main_scraper("https://www.detik.com","Hasil")

def main_scraper(url,directory):
    scrapp.create_directory(directory)
    source_code = requests.get(url)
    source_text = source_code.text
    soup = BeautifulSoup(source_text,"html.parser")
    # print(soup.find_all("div",{'class':'grid-row list-content list-content--column'}))
    print(soup.find_all("article",{'class':'list-content__item column-4 recommendation_firstrow'}))
main_scraper("https://www.detik.com","Hasil")
print(scrapp)
