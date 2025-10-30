from bs4 import BeautifulSoup
from os import system
import fungsi
import requests 
import os

def main_scraper(url, directory):
    fungsi.create_directory(directory)
    source_code = requests.get(url)
    source_text = source_code.text
    soup = BeautifulSoup(source_text, 'html.parser')
    articles = soup.find_all(True, {'class': 'clearfix'})

    for article in articles:
        article_format = "URL: " + article.a.get("txt") + "\n"

        if fungsi.does_file_exist(directory + "/artikel.txt") is False:
            fungsi.create_new_file(directory + "/artikel.txt")

        fungsi.write_to_file(directory + "/artikel.txt", article_format)
        fungsi.get_details(article.a.get("href"))
        print(article_format)

main_scraper("hhttps://tekno.kompas.com/read/2025/10/29/18580047/menggenggam-realme-15t-5g-hp-tipis-baterai-besar-yang-ringan-di-tangan", "hasil")