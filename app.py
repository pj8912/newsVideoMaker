from flask import Flask, request, jsonify, render_template
from get_tamil_feeds import *
import sqlite3

app = Flask(__name__)


conn = sqlite3.connect('todo.db', check_same_thread=False)
cursor = conn.cursor()

urls = [
        'https://www.news18.com/rss/world.xml',
        'http://timesofindia.indiatimes.com/rssfeeds/296589292.cms']
feed = combine_feeds(urls,100)

@app.route('/')
def home():
    return render_template('index.html', data=feed)


@app.route('/savec',methods=['POST'])
def save_content():
    news_title =request.json['news_title']
    news_desc =request.json['news_desc']
    news_image_url =request.json['news_image_url']
    news_source_url =request.json['news_source_url']
    cursor.execute("INSERT INTO saved_content(n_title,n_desc,n_source_url,n_image_url) VALUES(?,?,?,?)",(news_title,news_desc,news_image_url,news_source_url))
    conn.commit()
    if cursor.rowcount > 0:
        return jsonify({"status":1, "message":"content saved"})
    else:
        return jsonify({"status" : 0,"message":"failed!"})
    
# SAVED CONTENT PAGE
@app.route('/saved_c')
def saved_content_page():
    cursor.execute("SELECT * FROM saved_content ORDER BY created_at DESC")
    row = cursor.fetchall()
    return render_template("saved.html", contents=row)



    

if __name__ ==  "__main__":
    app.run(debug=True,port=7000)
