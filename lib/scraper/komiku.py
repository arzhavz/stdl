import re
from requests import *
from bs4 import BeautifulSoup as bs


def rep(text, d):
    for i, j in d.items():
        text = text.replace(i, j)
    return text.strip()


def Komiku(judul: str = None) -> dict:
    if re.search(r"http[s]://", judul):
        _data = get(judul)
    else:
        data = get(f"https://data.komiku.id/cari/?post_type=manga&s={judul}")
        html = bs(data.text, "html.parser")
        url = html.find("div", {"class": "daftar"}).find("a")
        _data = get(url.get("href"))
    _html = bs(_data.text, "html.parser")
    table = _html.find("table", {"id": "Daftar_Chapter"})
    tr = table.find_all("tr")
    list_tr = []
    for td in tr:
        if td.find("td", {"class": "judulseries"}):
            list_tr.append(td)
    res = []
    for item in list_tr:
        link = item.find("a").get("href")
        title = item.find("a").get("title")
        chapter = item.find("span").text
        date = item.find("td", {"class": "tanggalseries"}).text
        res.append({
            "url": f"https://komiku.id{link}",
            "title": title,
            "chapter": chapter,
            "date": rep(date, {"\n": "", "\t": ""})
        })
    res.reverse()
    results = []
    for m in res:
        data = get(m["url"])
        html = bs(data.text, "html.parser")
        section = html.find("section", {"id": "Baca_Komik"})
        image = section.find_all("img")
        resm = []
        for img in image:
            num = img.get("id")
            uri = img.get("src")
            alt = img.get("alt")
            resm.append({
                "id": int(num),
                "alt": alt,
                "src": uri
            })
        results.append({
            **m,
            "img": resm
        })
    
    return results