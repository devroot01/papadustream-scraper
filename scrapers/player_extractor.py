from bs4 import BeautifulSoup
import requests

class PlayerExtractor:
    def extract_iframes(self,url):
        html=requests.get(url).text
        soup=BeautifulSoup(html,"lxml")
        return [i.get("src") for i in soup.find_all("iframe") if i.get("src")]
