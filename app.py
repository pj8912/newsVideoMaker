from flask import Flask, request, jsonify, render_template, redirect
from get_feeds import *
import sqlite3
from get_feeds import * 

app = Flask(__name__)


conn = sqlite3.connect('todo.db', check_same_thread=False)
cursor = conn.cursor()

urls = ['https://feeds.feedburner.com/Hindu_Tamil_india.xml',
        'https://www.news18.com/rss/world.xml',
        'http://timesofindia.indiatimes.com/rssfeeds/296589292.cms']
feed = combine_feeds(urls,100)

#home
@app.route('/')
def home():
    return render_template('index.html', data=feed)

#saved feed to database
@app.route('/savec',methods=['POST'])
def save_content():
    news_title =request.json['news_title']
    news_desc =request.json['news_desc']
    news_image_url =request.json['news_image_url']
    news_source_url =request.json['news_source_url']
    cursor.execute("INSERT INTO saved_content(n_title,n_desc,n_source_url,n_image_url) VALUES(?,?,?,?)",(news_title,news_desc,news_source_url,news_image_url))
    conn.commit()
    if cursor.rowcount > 0:
        return jsonify({"status":1, "message":"content saved"})
    else:
        return jsonify({"status" : 0,"message":"failed!"})
    
# SAVED CONTENT PAGE
@app.route('/saved_c')
def saved_content_page():
    conn = sqlite3.connect('todo.db', check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM saved_content ORDER BY created_at DESC")
    row = cursor.fetchall()

    return render_template("saved.html", contents=row)



#add rss link page
@app.route('/upload-rss')
def add_rss_page():
    return render_template('add_rss.html')

#add rss link to database
@app.route('/addrss', methods=['POST'])
def add_rss():
    if request.method == 'POST':
        rss_link = request.form['rss_link']
        lang = request.form['language']
        topic = request.form['topic']
        cursor.execute("INSERT INTO rss_links(rss_link,link_language,link_topic) VALUES(?,?,?)",(rss_link,lang,topic))
        conn.commit()
        return redirect('/upload-rss')
    else:
        return redirect('/')



#delete news
@app.route('/deletenews',methods=['POST'])
def delete_news():
    newsid = request.json['newsid']
    conn = sqlite3.connect('todo.db', check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM saved_content WHERE n_id = ?",(newsid,))
    conn.commit()

    cursor.execute("SELECT n_title FROM saved_content WHERE n_id = ?",(newsid,))
    if cursor.rowcount < 1:
        return jsonify({"status":1, "message":"news deleted"})
    else:
        return jsonify({"status" : 0,"message":"failed!"})
    

if __name__ ==  "__main__":
    app.run(debug=True,port=7000)
