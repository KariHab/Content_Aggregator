import requests
from bs4 import BeautifulSoup as sp 

my_url = "https://www.nytimes.com/section/technology"

def extract_article_data_from_page(url):
    page = requests.get(url)
    page_parsed = sp(page.content, 'html.parser')
    # searches for all <script> elements with the attribute type="application/ld+json". 
    data_stock = page_parsed.find_all("script", {"type": "application/ld+json"})
    article_list = []
    #append to list all the dict stored in the data_stock - each data contains several dict
    for data in data_stock:
        for dict in data:
            article_list.append(dict)
    #join the 2 first items in the list to make sure we don't have any split accross multiple <script> 
    article_list[0:2] = [''.join(article_list[0:2])]
    content = article_list[0]
    #get the index where "itemListElement" to have all the articles data
    article_index = content.index("itemListElement")
    content = content[article_index:]
    return content

#locate the start and end index of url 
def find_url_indices(content):
    start = [i for i in range(len(content)) if
                     content.startswith('https://www.nytimes.com/2023', i)]
    end = [i for i in range(len(content)) if content.startswith('.html', i)]
    end = [x + 5 for x in end]
#make sur we have clean URL terminated with .html
    if len(start) > len(end):
        difference = len(start) - len(end)
        start = start[:difference]
    if len(end) > len(start):
        difference = len(end) - (len(end) - len(start))
        end = end[:difference]
    return start, end

#extracting the URLs from the content using the start and end indices.
def extract_urls(start, end, content):
    url_list = []
    for i in range(len(start)):
        url_list.append(content[start[i]:end[i]])
    return url_list