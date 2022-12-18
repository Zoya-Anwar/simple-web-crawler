import requests 
from bs4 import BeautifulSoup, SoupStrainer
import re
import urllib.parse
import validators

def web_crawl(start_link):
    links = []
    link_index = -1
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }

    links.append(start_link)

    while len(links) < 100 and (link_index + 1) < len(links):
        link_index = link_index + 1
        current_link = links[link_index]

        try: 
            f = requests.get(current_link, headers=headers, timeout=3)
        except requests.exceptions.RequestException: 
            continue # skip to next link

        soup = BeautifulSoup(f.content, 'html.parser', parse_only=SoupStrainer("a"))
        
        for new_link in soup.find_all(href=True):

            add_link = new_link['href']

            if not re.match('^(http|https)://', add_link):  # assume it is a relative path
                add_link = urllib.parse.urljoin(current_link, add_link)

            if validators.url(add_link): # check it is a valid URL
                
                if add_link not in links:
                    print(add_link) 
                    links.append(add_link)

                if len(links) == 100: 
                    break

    return links