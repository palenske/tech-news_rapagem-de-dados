from scraping_menu import analyzer_menu
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home_page(debug=True):
    return render_template("homepage.html", analyzer_menu=analyzer_menu)

app.run()