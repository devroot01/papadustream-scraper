# Papadustream Scraper
Advanced scraper extracting metadata and players.
Educational use only.

# 🎬 Papadustream Scraper correct URL: https://papadustream.food/

Advanced scraper for extracting content metadata and streaming sources.

---

# ⚠️ Important

Papadustream:

* Uses external video hosts
* Changes domains frequently
* May be illegal depending on country

This project is for **educational use only**.

---

# 🧠 How It Works

1. Scrapes homepage (films / series / anime)
2. Extracts metadata
3. Extracts video players (iframes)
4. Saves:

   * JSON locally
   * MongoDB

---

# 🔥 Features

* Content scraping
* Player extraction
* MongoDB storage
* JSON export
* Playwright anti-bot support

---

# 🚀 Run

```bash
pip install -r requirements.txt
playwright install
python main.py
```

---

# ⚡ Next Steps

* Extract real video streams (m3u8)
* Auto-download episodes
* Multi-thread scraping
* Proxy rotation

---

# 🧠 Pro Tip

Papadustream ≠ data source
👉 It’s a **gateway to video hosts**

To go further:

* parse iframe → extract host → extract m3u8

---

# 👑 Final Goal

Build your own:

* Netflix-style backend
* Streaming aggregator
* Anime/movie API
