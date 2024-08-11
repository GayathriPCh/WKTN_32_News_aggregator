from utils.data_processing import categorize_and_find_similar
from utils.display import display_similar_articles

def main():
    # Categorize and find similar articles
    similar_articles = categorize_and_find_similar()
    
    # Display similar articles
    display_similar_articles(similar_articles)

if __name__ == "__main__":
    main()
