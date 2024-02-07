import requests
from bs4 import BeautifulSoup
import csv

URL = "https://www.goodreads.com/quotes/tag/inspirational"
r = requests.get(URL)


if r.status_code != 200:
    print(f"Failed to retrieve the webpage. Status code: {r.status_code}")
    exit()

soup = BeautifulSoup(r.content, 'html.parser')

quotes = []  # a list to store quotes

quote_divs = soup.find_all('div', class_='quote')

for div in quote_divs:
    quote = {}
    quote['lines'] = div.find('div', class_='quoteText').text.strip().split('\n')[0][1:-1]
    quote['author'] = div.find('span', class_='authorOrTitle').text.strip()
    quote['tags'] = ', '.join([tag.text for tag in div.find_all('a', class_='smallText')])
    quotes.append(quote)

filename = 'inspirational_quotes_goodreads.csv'
with open(filename, 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, ['lines', 'author', 'tags'])
    w.writeheader()
    for quote in quotes:
        w.writerow(quote)

print("Quotes scraped successfully and saved to", filename)
