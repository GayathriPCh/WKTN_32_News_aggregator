import requests
import json
from bs4 import BeautifulSoup
import pandas as pd

# URL of the BBC news website
url = 'https://www.bbc.com/news/'  # Replace with the actual page URL

def fetch_bbc_news(url):
    response = requests.get(url)
    response.raise_for_status()  # Check if the request was successful
    
    soup = BeautifulSoup(response.content, 'html.parser')
    script_tag = soup.find('script', id='__NEXT_DATA__')
    
    if script_tag:
        json_data = json.loads(script_tag.string)
        
        try:
            sections = json_data['props']['pageProps']['page']['@\"news\",']['sections']
            data = []
            for section in sections:
                if 'content' in section:
                    for content in section['content']:
                        data.append({
                            'title': content.get('title', 'No title'),
                            'link': content.get('href', 'No link'),
                            'description': content.get('description', 'No description'),
                            'image': content.get('image', {}).get('model', {}).get('blocks', {}).get('src', 'No image')
                        })
            df = pd.DataFrame(data)
            df.to_csv('bbc_news.csv', index=False)
        except KeyError as e:
            print(f"KeyError: {e} - Please check the JSON structure.")
    else:
        print("JSON data not found in the script tag.")

if __name__ == "__main__":
    fetch_bbc_news(url)
