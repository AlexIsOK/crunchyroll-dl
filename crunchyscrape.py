
#Scrape a URL using a four line Python script.

import sys
import cloudscraper

scraper = cloudscraper.create_scraper(allow_brotli=False)

#Don't ask questions
page = sys.argv[1:][0]

#print("Getting page...")
#print(page)

print(scraper.get(page).text)

