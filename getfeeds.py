import feedparser
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def get_domain_from_url(url):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    if domain.startswith('www.'):
        domain = domain[4:]
    return domain


# Function to fetch RSS feed data
def get_rss_feed_data(url, num_posts):
    feed = feedparser.parse(url)
    data = []
    counter = 0
    # news_website_name = feed.feed.title
    website_name = None
    for entry in feed.entries:
        if counter >= num_posts:
            break
        title = entry.title #newstitle
        pub_date = entry.published #published date

        summary_html = entry.summary #news summary
        summary_text = BeautifulSoup(summary_html, 'html.parser').get_text()
        
        source_url = entry.link 
        dname = get_domain_from_url(source_url)
        website_name = dname 


        image_url = ''
        
        if 'enclosures' in entry and len(entry.enclosures) > 0:
            image_url = entry.enclosures[0]['url']
        
        elif 'media_content' in entry and len(entry.media_content) > 0:
            image_url = entry.media_content[0]['url']
        
        elif 'content' in entry and 'encoded' in entry.content:
            content_html = entry.content.encoded
            image_start = content_html.find('<img src="') + len('<img src="')
            image_end = content_html.find('"', image_start)
            image_url = content_html[image_start:image_end]
        
        elif 'content' in entry and 'value' in entry.content[0]:
            content_html = entry.content[0].value
            content_soup = BeautifulSoup(content_html, 'html.parser')
            image_element = content_soup.find('img')
            if image_element:
                image_url = image_element['src']

        elif 'description' in entry and 'img' in entry.description :
            description_html = entry.description
            description_soup = BeautifulSoup(description_html, 'html.parser')
            image_url = description_soup.find('img')['src'] if description_soup.find('img') else None

        data.append({
            'title': title,
            'published_date': pub_date,
            'summary': summary_text,
            'image_url': image_url,
            'source_url' : source_url,
            'source_name' :  website_name
        })
        counter += 1
    return data

def combined_feeds(url_list, category_ids, num_posts=20):
    combined_data = []
    if isinstance(category_ids, int):
        # If there's only one category ID, convert it to a list
        category_ids = [category_ids]
    for url, category_id in zip(url_list, category_ids):
        feed_data = get_rss_feed_data(url, num_posts)
        for entry in feed_data:
            # Include the category ID in the data dictionary
            entry['category_id'] = category_id
        combined_data.extend(feed_data)

    combined_data.sort(key=lambda x: x['published_date'], reverse=True)
    return combined_data