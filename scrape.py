from newspaper import Article


def summarize_article(url):
    article = Article(url)

    article.download()
    article.parse()
    print(article.title)
    # Gets the author or authors of the article
    author_string = "Author(s): "
    for author in article.authors:
        author_string += author  # adds all authors (if more than 1) to the author string.
    print(author_string)
    date = article.publish_date
    print("Publish Date: " + str(date.strftime("%m/%d/%Y")))

    # Gets the article summary
    print("Article summary")
    print("-----------------------------------------------------------------------------------------------")
    print(article.text[:])
