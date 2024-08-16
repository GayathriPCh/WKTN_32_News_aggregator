import requests
import json
from bs4 import BeautifulSoup

def scrape_bbc_news():
    url = 'https://www.bbc.com/news/'
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, 'html.parser')
    script_tag = soup.find('script', id='__NEXT_DATA__')

    bbc_news = []
    if script_tag:
        json_data = json.loads(script_tag.string)
        try:
            # Adjusted JSON path according to the structure you provided
            sections = json_data['props']['pageProps']['page']['@\"news\",']['sections']
            for section in sections:
                for content in section['content']:
                    bbc_news.append({
                        'title': content['title'],
                        'link': content['href'],
                        'description': content['description'],
                        'image': content.get('image', {}).get('model', {}).get('blocks', {}).get('src')
                    })
        except KeyError as e:
            print(f"KeyError: {e} - Please check the JSON structure.")

    # File path for saving the BBC news JSON file
    with open('bbc_news.json', 'w') as f:
        json.dump(bbc_news, f, indent=4)

if __name__ == "__main__":
    scrape_bbc_news()
