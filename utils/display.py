def display_similar_articles(similar_articles):
    for article_pair in similar_articles:
        print("Similar Articles:")
        print("AP News Version:")
        print(article_pair[0])  # Print the first version
        print("BBC News Version:")
        print(article_pair[1])  # Print the second version
        print('-' * 80)
