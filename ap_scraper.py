import requests
from bs4 import BeautifulSoup
import json

def scrape_ap_news():
    url = 'https://apnews.com/'
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')
    articles = soup.find_all('div', class_='PagePromo')

    ap_news = []
    for article in articles:
        headline = article.find('h3', class_='PagePromo-title')
        link = article.find('a', class_='Link')['href']
        description = article.find('div', class_='PagePromo-description')

        img_tag = article.find('img', class_='Image')
        if img_tag and img_tag.has_attr('srcset'):
            image = img_tag['srcset'].split(',')[0].split(' ')[0]
        else:
            image = None

        ap_news.append({
            'headline': headline.get_text(strip=True) if headline else None,
            'link': link,
            'description': description.get_text(strip=True) if description else None,
            'image': image
        })

    with open('ap_news.json', 'w') as f:
        json.dump(ap_news, f, indent=4)

if __name__ == "__main__":
    scrape_ap_news()
