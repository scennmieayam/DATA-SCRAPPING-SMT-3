import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template

app = Flask(__name__)

def klasifikasi_berita(judul):
    judul_lower = judul.lower()
    
    kata_kunci_merah = [
        "cuaca", "surabaya", "syaban", "banjir", "meluap", "efisiensi", "becak", "kampung", "pesawat"
    ] # untuk klasifikasi warna berita sesuai foto yang ada di grup
    
    for kata in kata_kunci_merah:
        if kata in judul_lower:
            return "berita"
    
    return "informasi"

@app.route("/")
def detik_populer():
    html_doc = requests.get("https://www.detik.com/jatim/berita/indeks")
    soup = BeautifulSoup(html_doc.text, 'html.parser')
    populer_area = soup.find(attrs={'class': 'grid-row list-content'})
    items = populer_area.findAll(attrs={'class': 'list-content__item'})

    data = []
    for item in items:
        img_tag = item.find('a').find('img')
        link_tag = item.find('a')
        date_tag = item.find('div', {'class': 'media__date'}).find('span')
        
        title = img_tag['title']
        status = klasifikasi_berita(title)
        
        data.append({
            'title': title,
            'image': img_tag['src'],
            'link': link_tag['href'],
            'date': date_tag['title'],
            'status': status
        })

    return render_template("index.html", data=data)

if __name__ == '__main__':
    app.run(debug=True)