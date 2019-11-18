from bs4 import BeautifulSoup as bs
from langdetect import detect 
import requests
import time

def get_quotes(num, category):
        url = 'https://www.goodreads.com/quotes/tag/' + category + '?page=' + str(num)
        req = requests.get(url)
        soup = bs(req.text, 'html.parser')
        filteredSoup = soup.find_all('div', class_="quoteText")
        write_to_file(filteredSoup)
        
def write_to_file(quotes):
    f = open("quotes.txt","a+")
    for q in quotes:
      string = q.get_text().strip()
      end = string.find('―') - 6
      sliced_text = string[1:end]
      if (sliced_text not in [' ... ', '']) and (detect(sliced_text) == 'en') and (len(sliced_text.split()) <  30):
          final_text = sliced_text + "\n"
          f.write(final_text) 

def start_scrape(categories, sleep_time=5):
  for category in categories:
      for n in range(1,71):
        print('WE ARE ON PAGE:',n, 'CATEGORY:', category)
        get_quotes(n, category)
        time.sleep(sleep_time)

start_scrape(
  categories=['philosophy', 'inspiration'],
  sleep_time = 10
)