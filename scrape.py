from newspaper import Article


def get_articles_info(url):
    article = Article(url)

    article.download()
    article.parse()
    print(article.title)
    # Gets the author or authors of the article
    author_string = "Author(s): "
    for author in article.authors:
        author_string += author  
    print(author_string)
    date = article.publish_date
    #format the date to day month year
    print("\033[1;37;40mPublish Date: " + str(date.strftime("%d/%m/%Y")))
    print('\033[1;37;40m')
    print("\033[1;33;40mSUMMARY \033[1;37;40m")
    print("\033[1;33;40m-----------------------------------------------------------------------------------------------\033[1;37;40m")
    print(article.text[:])
