from extract import *
from scrape import *
import time
import pyfiglet as pf

new_paper_title = pf.figlet_format('New York Times', font = "cybermedium")
new_paper_subtitle = pf.figlet_format('  Technology', font = "cybermedium")
print('\033[1;37;40m')
print('\033[1;32;40m',new_paper_title,"\n", new_paper_subtitle, '\033[1;37;40m')
time.sleep(2)


content = extract_article_data_from_page(my_url)
starts, ends = find_url_indices(content)
url_list = extract_urls(starts, ends, content)

# Gets the article summary + infos
for url in url_list:
    print("\033[1;34;40mRead the full article: URL: \033[1;37;40m" + str(url))
    article_summary = get_articles_info(url)  
    print("\033[1;33;40m-----------------------------------------------------------------------------------------------\033[1;37;40m")
    print()
    time.sleep(20)  # Allows user to get through all the text.

print()
print(str(len(url_list)) + " different articles were extracted!")