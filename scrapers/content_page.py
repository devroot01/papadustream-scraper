from bs4 import BeautifulSoup
import requests

class ContentScraper:
    def scrape(self,url):
        html=requests.get(url).text
        soup=BeautifulSoup(html,"lxml")
        t=soup.find("h1")
        d=soup.find("p")
        return {"title":t.text.strip() if t else None,
                "description":d.text.strip() if d else None}
