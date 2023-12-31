import sqlite3

conn = sqlite3.connect('todo.db', check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""CREATE TABLE saved_content(
n_id INTEGER PRIMARY KEY AUTOINCREMENT,
n_title TEXT,
n_desc TEXT,
n_source_url TEXT,
n_image_url TEXT,
language TEXT,
status BOOLEAN DEFAULT 0,
created_at datetime default current_timestamp,
updated_at datetime default current_timestamp     
)""")

cursor.execute("""CREATE TABLE IF NOT EXISTS video_content(
vid INTEGER PRIMARY KEY AUTOINCREMENT,
v_title TEXT,
v_tags TEXT, 
v_video TEXT,
status BOOLEAN,
created_at datetime default current_timestamp,
updated_at datetime default current_timestamp
)""")

cursor.execute("""CREATE TABLE IF NOT EXISTS rss_links(
rss_id INTEGER PRIMARY KEY AUTOINCREMENT,
rss_link TEXT,
link_language TEXT,
link_topic TEXT,
created_at DATETIME DEFAULT current_timestamp
)""")

cursor.close()
conn.close()

print("database created")
