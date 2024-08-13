import json
import nltk
from nltk.tokenize import word_tokenize
from difflib import SequenceMatcher

nltk.download('punkt')

# Define categories and their keywords
categories = {
    "Business": ["business", "economy", "market", "stock", "trade"],
    "Political": ["election", "government", "policy", "vote", "president"],
    "Sports": ["sports", "game", "match", "tournament", "team"],
    "Technology": ["technology", "tech", "software", "hardware", "AI"],
    "Entertainment": ["entertainment", "movie", "music", "show", "film"]
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
                common_news.append((ap_article, bbc_article))

    return common_news

# Load news data from JSON files
with open('ap_news.json', 'r') as ap_file:
    ap_news = json.load(ap_file)

with open('bbc_news.json', 'r') as bbc_file:
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

# Save the results to a file
with open('categorized_news_output.txt', 'w', encoding='utf-8') as output_file:
    output_file.write("=== Common News ===\n")
    for ap_article, bbc_article in common_news:
        output_file.write("AP Headline: " + ap_article['headline'] + "\n")
        output_file.write("AP Category: " + ap_article['category'] + "\n")
        output_file.write("AP Link: " + ap_article['link'] + "\n")
        output_file.write("BBC Title: " + bbc_article['title'] + "\n")
        output_file.write("BBC Category: " + bbc_article['category'] + "\n")
        output_file.write("BBC Link: " + bbc_article['link'] + "\n")
        output_file.write("-" * 80 + "\n")

    output_file.write("\n=== AP News ===\n")
    for article in ap_news:
        output_file.write("Headline: " + article['headline'] + "\n")
        output_file.write("Category: " + article['category'] + "\n")
        output_file.write("Link: " + article['link'] + "\n")
        output_file.write("-" * 80 + "\n")

    output_file.write("\n=== BBC News ===\n")
    for article in bbc_news:
        output_file.write("Title: " + article['title'] + "\n")
        output_file.write("Category: " + article['category'] + "\n")
        output_file.write("Link: " + article['link'] + "\n")
        output_file.write("-" * 80 + "\n")

print("Categorization and comparison complete! Check the 'categorized_news_output.txt' file for results.")
