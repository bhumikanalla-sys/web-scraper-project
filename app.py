from flask import Flask, render_template
import sqlite3
from scraper import scrape_and_store

app = Flask(__name__)

# run scraper when server starts
scrape_and_store()

def get_data():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT quote, author FROM quotes")
    data = cursor.fetchall()

    conn.close()
    return data


@app.route("/")
def index():
    data = get_data()
    return render_template("index.html", data=data)


if __name__ == "__main__":
    app.run(debug=True)