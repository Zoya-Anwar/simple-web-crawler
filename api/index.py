from flask import Flask, render_template, request
from web_crawler import web_crawl

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def home_page(url=None): 
    if request.method == 'POST':
        if url != "":
            scraped = web_crawl(request.form['url'])
            return render_template('index.html', url=url, scraped=scraped)
    return render_template('index.html', url=url)
