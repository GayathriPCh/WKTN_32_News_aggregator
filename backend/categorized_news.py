import json
import nltk
from nltk.tokenize import word_tokenize
from difflib import SequenceMatcher

nltk.download('punkt')

# Define categories and their keywords
categories = {
    "Business": ["business", "economy", "market", "stock", "trade"],
    "Political": ["election", "government", "policy", "vote", "president","Trump","trump","Donald","Biden"],
    "Sports": ["sports", "game", "match", "tournament", "team","Olympics"],
    "Technology": ["technology", "tech", "software", "hardware", "AI","Crypto","cryptocurrency","Bitcoin"],   
    "Entertainment": ["entertainment", "movie", "music", "show", "film","Netflix","Hollywood","TV"]
}

# Preprocess text for comparison and categorization
def preprocess_text(text):
    tokens = word_tokenize(text.lower())
    return ' '.join(tokens)

# Categorize articles based on keywords
def categorize_article(text):
    text = preprocess_text(text)
    for category, keywords in categories.items():
        for keyword in keywords:
            if keyword in text:
                return category
    return "Uncategorized"

# Compare headlines and find common news
def compare_headlines(ap_news, bbc_news):
    common_news = []

    for ap_article in ap_news:
        ap_headline = preprocess_text(ap_article['headline'])
        for bbc_article in bbc_news:
            bbc_title = preprocess_text(bbc_article['title'])

            # Use SequenceMatcher to find the similarity ratio
            similarity = SequenceMatcher(None, ap_headline, bbc_title).ratio()
            if similarity > 0.7:  # Adjust this threshold as needed
                common_news.append({
                    "AP": {
                        "headline": ap_article['headline'],
                        "category": ap_article['category'],
                        "link": ap_article['link']
                    },
                    "BBC": {
                        "title": bbc_article['title'],
                        "category": bbc_article['category'],
                        "link": bbc_article['link']
                    }
                })

    return common_news

# Load news data from JSON files
with open('../scraper/ap_news.json', 'r') as ap_file:
    ap_news = json.load(ap_file)

with open('../scraper/bbc_news.json', 'r') as bbc_file:
    bbc_news = json.load(bbc_file)

# Categorize AP news
for article in ap_news:
    category = categorize_article(article['headline'])
    article['category'] = category

# Categorize BBC news
for article in bbc_news:
    category = categorize_article(article['title'])
    article['category'] = category

# Find common news
common_news = compare_headlines(ap_news, bbc_news)

# Prepare the final data structure
output_data = {
    "common_news": common_news,
    "ap_news": ap_news,
    "bbc_news": bbc_news
}

# Save the results to a JSON file
with open('categorized_news_output.json', 'w', encoding='utf-8') as output_file:
    json.dump(output_data, output_file, ensure_ascii=False, indent=4)

print("Categorization and comparison complete! Check the 'categorized_news_output.json' file for results.")
