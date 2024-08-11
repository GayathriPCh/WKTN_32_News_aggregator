import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the page you want to scrape
url = 'https://apnews.com/'

def fetch_ap_news(url):
    response = requests.get(url)
    response.raise_for_status()  # Check if the request was successful
    
    soup = BeautifulSoup(response.text, 'html.parser')
    articles = soup.find_all('div', class_='PagePromo')
    
    data = []
    for article in articles:
        headline = article.find('h3', class_='PagePromo-title')
        link_tag = article.find('a', class_='Link')
        description = article.find('div', class_='PagePromo-description')
        image_tag = article.find('img', class_='Image')

        link = link_tag['href'] if link_tag else 'No link found'
        image = image_tag['srcset'].split(',')[0].split(' ')[0] if image_tag and 'srcset' in image_tag.attrs else 'No image found'

        data.append({
            'headline': headline.get_text(strip=True) if headline else 'No headline found',
            'link': link,
            'description': description.get_text(strip=True) if description else 'No description found',
            'image': image
        })

    df = pd.DataFrame(data)
    df.to_csv('ap_news.csv', index=False)

if __name__ == "__main__":
    fetch_ap_news(url)
