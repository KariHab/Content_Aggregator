# Imports all the methods and variables from each script.
from extract import *
from scrape import *
import time


print("NYT Technology News")
print('---------------------------------------')
print()
time.sleep(1)

# Gets all the latest URL's from the NY Times Technology Section.
content_string = get_content_string(my_url)
starts, ends = find_occurrences(content_string)
url_list = get_all_urls(starts, ends, content_string)

# Gets the article summary and performs sentiment analysis on the chosen URL.
for url in url_list:
    print("Read the full article: URL: " + str(url))
    article_summary = summarize_article(url)   
    print("-----------------------------------------------------------------------------------------------")
    print()
    time.sleep(20)  # Allows user to get through all the text.

print()
print("In total " + str(len(url_list)) + " different articles were extracted!")