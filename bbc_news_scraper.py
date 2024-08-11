import requests
import json
from bs4 import BeautifulSoup
import csv

# URL of the BBC news website
url = 'https://www.bbc.com/news/'

# Send an HTTP GET request to the website
response = requests.get(url)

# Parse the HTML code using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the JSON data within the script tag
script_tag = soup.find('script', id='__NEXT_DATA__')
if script_tag:
    json_data = json.loads(script_tag.string)
    
    # Navigate through the JSON structure
    try:
        # Extract the news sections
        sections = json_data['props']['pageProps']['page']['@\"news\",']['sections']
        
        # Define the filename
        filename = 'data/bbc_news.csv'

        # Open a CSV file to write the data
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            # Write the header
            writer.writerow(['Title', 'Link', 'Description', 'Image'])
            
            # Write the news articles
            for section in sections:
                for content in section['content']:
                    writer.writerow([
                        content['title'],
                        content['href'],
                        content['description'],
                        content['image']['model']['blocks']['src']
                    ])
    except KeyError as e:
        print(f"KeyError: {e} - Please check the JSON structure.")
else:
    print("JSON data not found in the script tag.")
