from bs4 import BeautifulSoup
from os import system
import fungsi
import requests 

def main_scrapper(url, directory):
    fungsi.create_directory(directory)
    source_code = requests.get(url)
    source_text = source_code.text
    soup = BeautifulSoup(source_text, "html.parser")
    articles = soup.find_all("h3", {"class":["article__title article__title--medium"]})
    articles2 = soup.find_all(True,{"class":["article__box", "article__title"]})

    system("clear")

    for article in articles:
        print("URL: ", article.a.get("href"))
        print("Title: ", articles.a.text, "\n")
    
    for article2 in articles2:
        print("URL: ", article2.a.get("href"))
        print("Title: ", article2.a.text, "\n")

main_scrapper("https://tekno.kompas.com/gadget", "hasil")