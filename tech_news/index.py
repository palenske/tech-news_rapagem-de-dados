from scraping_menu import analyzer_menu
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home_page():
    return print(analyzer_menu())

app.run()