import requests
from bs4 import BeautifulSoup
import sqlite3

def scrape_and_store():
    url = "https://quotes.toscrape.com/"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS quotes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        quote TEXT,
        author TEXT
    )
    """)

    quotes = soup.find_all("div", class_="quote")

    for q in quotes:
        text = q.find("span", class_="text").text
        author = q.find("small", class_="author").text

        cursor.execute("INSERT INTO quotes (quote, author) VALUES (?, ?)", (text, author))

    conn.commit()
    conn.close()