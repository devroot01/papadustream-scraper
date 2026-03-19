from bs4 import BeautifulSoup
import requests

class HomeScraper:
    def scrape(self,url):
        html=requests.get(url).text
        soup=BeautifulSoup(html,"lxml")
        items=[]
        for a in soup.find_all("a"):
            href=a.get("href")
            if href and ("/film/" in href or "/serie/" in href):
                items.append({"title":a.text.strip(),"url":href})
        return items
