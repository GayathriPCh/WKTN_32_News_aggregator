import requests
import json
from bs4 import BeautifulSoup

# URL of the BBC news website
url = 'https://www.bbc.com/news/'  # Replace with the actual page URL

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
        for section in sections:
            print(f"Section Type: {section['type']}")
            for content in section['content']:
                print(f"Title: {content['title']}")
                print(f"Link: {content['href']}")
                print(f"Description: {content['description']}")
                print(f"Image: {content['image']['model']['blocks']['src']}")
                print()
    except KeyError as e:
        print(f"KeyError: {e} - Please check the JSON structure.")
else:
    print("JSON data not found in the script tag.")
