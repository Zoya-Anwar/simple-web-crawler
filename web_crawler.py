import requests 
from bs4 import BeautifulSoup, SoupStrainer
import re
from collections import deque
import urllib.parse

def web_crawl(start_link):
    links = set()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
    }

    links.add(start_link)

    while len(links) < 100:
        print(len(links))
        current_link = list(links)[-1]
        f = requests.get(current_link, headers=headers)
        soup = BeautifulSoup(f.content, 'html.parser', parse_only=SoupStrainer("a"))
        
        for new_link in soup.find_all(href=True):
            if not re.match('^(http|https)://', new_link['href']):  # this is a relative path
                add_link = urllib.parse.urljoin(current_link, new_link['href'])
            else:
                add_link = new_link['href']

            print(add_link)
            links.add(add_link)

            if len(links) == 100: 
                break

    return links
# for link in links:
#     print(link)