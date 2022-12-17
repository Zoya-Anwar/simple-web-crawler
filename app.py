from flask import Flask, render_template, request
from web_crawler import web_crawl

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def web_scraper(url=None): 
    if request.method == 'POST':
        scraped = web_crawl(request.form['url'])
        return render_template('index.html', url=url, scraped=scraped)
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('index.html', url=url)
