
#Scrape a URL using a four line Python script.

import sys
import cloudscraper

scraper = cloudscraper

print(scraper.get(sys.argv[1:]).text)

