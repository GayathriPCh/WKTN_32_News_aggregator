import requests
from bs4 import BeautifulSoup
import csv

# URL of the page you want to scrape
url = 'https://apnews.com/'

# Send a GET request to fetch the page content
response = requests.get(url)
response.raise_for_status()  # Check if the request was successful

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Find all news articles based on the provided HTML structure
articles = soup.find_all('div', class_='PagePromo')

# Define the filename
filename = 'data/ap_news.csv'

# Open a CSV file to write the data
with open(filename, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Write the header
    writer.writerow(['Headline', 'Link', 'Description', 'Image URL'])
    
    # Write the news articles
    for article in articles:
        headline = article.find('h3', class_='PagePromo-title')
        link = article.find('a', class_='Link')['href']
        description = article.find('div', class_='PagePromo-description')
        img_tag = article.find('img', class_='Image')
        image = img_tag['srcset'].split(',')[0].split(' ')[0] if img_tag and img_tag.has_attr('srcset') else 'No image found'
        
        writer.writerow([
            headline.get_text(strip=True) if headline else 'No headline found',
            link if link else 'No link found',
            description.get_text(strip=True) if description else 'No description found',
            image
        ])
