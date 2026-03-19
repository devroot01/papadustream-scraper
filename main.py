import json, os
from scrapers.home import HomeScraper
from scrapers.content_page import ContentScraper
from scrapers.player_extractor import PlayerExtractor
from services.mongo import Mongo

mongo = Mongo()
BASE_URL = "https://papadustream.food"

os.makedirs("storage/json", exist_ok=True)

home = HomeScraper()
content = ContentScraper()
player = PlayerExtractor()

items = home.scrape(BASE_URL)

for item in items[:3]:
    details = content.scrape(item["url"])
    players = player.extract_iframes(item["url"])

    data = {
        "title": details["title"],
        "description": details["description"],
        "url": item["url"],
        "players": players
    }

    with open(f"storage/json/{data['title']}.json","w",encoding="utf-8") as f:
        json.dump(data,f,indent=4,ensure_ascii=False)

    mongo.save(data)
