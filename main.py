from extract import *
from scrape import *
import time


print("NYT Technology News")
print('---------------------------------------')
print()
time.sleep(1)

# 
content = extract_article_data_from_page(my_url)
starts, ends = find_url_indices(content)
url_list = extract_urls(starts, ends, content)

# Gets the article summary + infos
for url in url_list:
    print("Read the full article: URL: " + str(url))
    article_summary = get_articles_info(url)  
    print("-----------------------------------------------------------------------------------------------")
    print()
    time.sleep(20)  # Allows user to get through all the text.

print()
print(str(len(url_list)) + " different articles were extracted!")