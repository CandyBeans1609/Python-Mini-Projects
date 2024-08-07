# Quotes and Authors Web Scraper

This guide demonstrates how to implement a web scraping script that extracts quotes and their corresponding authors from the [Quotes to Scrape](http://quotes.toscrape.com/) website. The script uses the `requests` library to fetch web pages and `BeautifulSoup` to parse the HTML content.

<br>

<p align="center">
    <img src="https://d1pnnwteuly8z3.cloudfront.net/images/4d5bf260-c3d0-4f21-b718-8ede8d4ca716/febf9de6-8a5a-4055-b274-e685485496f5.jpeg">
</p>

<br>

## 🌟 Explanation

- **Web Scraping**: The script scrapes a website for quotes and their authors.
- **Pagination Handling**: Iterates through multiple pages until no more quotes are found.
- **Data Extraction**: Utilizes `BeautifulSoup` to parse HTML and extract relevant data.
- **Data Storage**: Stores authors in a set to ensure uniqueness and quotes in a list.

<br>

## ⚙️ Prerequisites

- **Basic Python Knowledge**: Understanding of Python syntax, functions, and loops.
- **Familiarity with Web Scraping**: Basic knowledge of HTML structure and web scraping techniques.
- **Required Libraries**: `requests`, `beautifulsoup4`, and `lxml` libraries for HTTP requests and HTML parsing.

<br>

## 🛠️ How to Run

1. **Ensure the script is saved as** `scrape.py`:
    - Copy the provided script code and save it as `scrape.py`.

2. **Install the required libraries**:
    ```bash
    pip install requests beautifulsoup4 lxml
    ```

This will install:

- `requests`: a library for making HTTP requests.
- `beautifulsoup4`: a library for parsing HTML and XML documents.
- `lxml`: a library for processing XML and HTML, used by BeautifulSoup for faster parsing.


3. **Run the script**:
    ```bash
    python3 scrape.py
    ```

<br>

The script will print out the list of unique authors and their quotes in a readable format.

### Example Output:
```
Authors

Albert Einstein
Jane Austen
J.K. Rowling
...

Quotes

“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”
“It is our choices, Harry, that show what we truly are, far more than our abilities.”
...
```

<br>

## 📺 Output
![image](https://github.com/user-attachments/assets/4f805a33-dd0a-4bf5-8e57-b6a6c42397c8)

![image](https://github.com/user-attachments/assets/885e3a84-6146-4166-bd46-fffe86a7498d)




## 📜 Conclusion

This web scraping script efficiently extracts quotes and their authors from a website using `requests` and `BeautifulSoup`. It demonstrates key web scraping techniques and pagination handling.

<br>

## 👻 Author

[Akanksha Kanade](https://github.com/CandyBeans1609)

