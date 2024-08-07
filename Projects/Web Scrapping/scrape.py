import requests
import bs4

url = 'https://quotes.toscrape.com/page/'

authors = set()
quotes = []
page = 1

while True:
    base_url = url + str(page)
    res = requests.get(base_url)

    page_valid = "No quotes found!" not in res.text
    if not page_valid:
        break

    soup = bs4.BeautifulSoup(res.text, 'lxml')

    for name in soup.select('.author'):
        authors.add(name.text)

    for quote in soup.select(".text"):
        quotes.append(quote.text)

    page += 1

print("\nAuthors\n")
for author in authors:
    print(author)

print("\nQuotes\n")
for quote in quotes:
    print(quote)
