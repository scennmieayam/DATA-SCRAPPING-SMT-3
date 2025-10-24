from bs4 import BeautifulSoup
from os import system
import os 
import fungsi
import requests

def main_scrapper(url, directory, file):
    fungsi.create_directory(directory)
    source_code = requests.get(url)
    source_text = source_code.text
    soup = BeautifulSoup(source_text, "html.parser")
    articles = soup.find("div", {"class":["row mt3 col-offset-fluid clearfix"]})
    articles2 = articles.find("div", {"class":["col-bs10-7"]})
    articles3 = articles2.find("div", {"class":["row article__wrap__grid--flex col-offset-fluid mt2"]})
    articles4 = articles3.find_all("div", {"class":["article__box"]})

    for article4 in articles4:
        # print("URL: ", article4.h3.a.get("href"))
        # print("Title: ", article4.h3.text, "\n")
        file_path = os.path.join(directory, file)
        fungsi.write_to_file(file_path, "URL: " + article4.h3.a.get("href"))
        fungsi.write_to_file(file_path, "Title: " + article4.h3.text + "\n")

main_scrapper("https://tekno.kompas.com/gadget", "hasil", "mencoba.txt")
fungsi.read_data("hasil/mencoba.txt", 3*2)