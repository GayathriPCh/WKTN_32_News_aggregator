from flask import Flask, jsonify, request, render_template
import json
import uuid  # For generating unique IDs
from gemini_api import analyze_article  # Import the analyze_article function

app = Flask(__name__)

def generate_temporary_ids(data):
    for source, articles in data.items():
        for article in articles:
            article['id'] = str(uuid.uuid4())  # Assign a unique ID
    return data

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/news', methods=['GET'])
def news_list():
    with open('categorized_news_output.json', encoding='utf-8') as f:
        data = json.load(f)
    
    data_with_ids = generate_temporary_ids(data)
    
    # Normalize the JSON structure
    news_data = []
    for source, articles in data_with_ids.items():
        for article in articles:
            news_data.append({
                'id': article.get('id'),
                'headline': article.get('headline') or article.get('title'),
                'link': article.get('link'),
                'description': article.get('description'),
                'image': article.get('image'),
                'category': article.get('category', 'Uncategorized'),
                'source': source
            })

    return render_template('news_list.html', news=news_data)

@app.route('/analyze', methods=['GET'])
def analyze_article_content():
    article_id = request.args.get('id')
    print(f"Received Article ID: {article_id}")  # Log received ID
    
    if not article_id:
        return "Article ID is required", 400
    
    with open('categorized_news_output.json', encoding='utf-8') as f:
        data = json.load(f)
    
    # Print the entire data to check structure
    print("Loaded JSON data:")
    print(data)
    
    # Look for the article with the given ID
    article_found = False
    for source, articles in data.items():
        for article in articles:
            if article.get('id') == article_id:
                article_found = True
                content = article.get('content')
                if content:
                    analysis = analyze_article(content)
                    return jsonify({'analysis': analysis})
    
    if not article_found:
        print("Article not found with ID:", article_id)
        return "Article not found", 404


if __name__ == '__main__':
    app.run(debug=True)
