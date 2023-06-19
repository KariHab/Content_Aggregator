import requests
from bs4 import BeautifulSoup as soup 

my_url = "https://www.nytimes.com/section/technology"

def get_content_string(url):
    page = requests.get(url)
    page_soup = soup(page.content, 'html.parser')
    containers = page_soup.find_all("script", {"type": "application/ld+json"})

    article_list = []
    for container in containers:
        for dictionary in container:
            article_list.append(dictionary)
    article_list[0:2] = [''.join(article_list[0:2])]
    content_string = article_list[0]
    article_index = content_string.index("itemListElement")
    content_string = content_string[article_index + 18:]
    return content_string


def find_occurrences(content_string):
    start_indices = [i for i in range(len(content_string)) if
                     content_string.startswith('https://www.nytimes.com/2023', i)]
    end_indices = [i for i in range(len(content_string)) if content_string.startswith('.html', i)]
    end_indices = [x + 5 for x in end_indices]

    if len(start_indices) > len(end_indices):
        difference = len(start_indices) - len(end_indices)
        start_indices = start_indices[:difference]
    if len(end_indices) > len(start_indices):
        difference = len(end_indices) - (len(end_indices) - len(start_indices))
        end_indices = end_indices[:difference]
    return start_indices, end_indices

def get_all_urls(start_indices, end_indices, content_string):
    url_list = []
    for i in range(len(start_indices)):
        url_list.append(content_string[start_indices[i]:end_indices[i]])
    return url_list