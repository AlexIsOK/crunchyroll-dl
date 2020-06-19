
#Scrape a URL using a four line Python script.

import sys
import cloudscraper

scraper = cloudscraper.create_scraper()

print(scraper.get(sys.argv[1:]).text)

