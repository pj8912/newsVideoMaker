from flask import Flask, render_template, request
from get_tamil_feeds import *
app = Flask(__name__)



urls = [
    'https://tamil.news18.com/rss/live-updates.xml',
        'https://www.news18.com/rss/world.xml',
        'http://timesofindia.indiatimes.com/rssfeeds/296589292.cms']
feed = combine_feeds(urls,100)

@app.route('/')
def home():
    return render_template('index.html', data=feed)





if __name__ ==  "__main__":
    app.run(debug=True)
