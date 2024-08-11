import requests
from bs4 import BeautifulSoup

# URL of the page you want to scrape
url = 'https://apnews.com/'

# Send a GET request to fetch the page content
response = requests.get(url)
response.raise_for_status()  # Check if the request was successful

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Find all news articles based on the provided HTML structure
articles = soup.find_all('div', class_='PagePromo')

# Loop through the articles and extract details
for article in articles:
    headline = article.find('h3', class_='PagePromo-title')
    link = article.find('a', class_='Link')['href']
    description = article.find('div', class_='PagePromo-description')

    # Attempt to find the <img> tag with class 'Image'
    img_tag = article.find('img', class_='Image')

    # Check if the img_tag is not None and has the 'srcset' attribute
    if img_tag and img_tag.has_attr('srcset'):
        # Extract the image URL from the srcset attribute
        image = img_tag['srcset'].split(',')[0].split(' ')[0]  # Get the first image URL
    else:
        # Handle the case where the img_tag is None or does not have srcset attribute
        image = 'No image found'
    
    # Print the details
    print('Headline:', headline.get_text(strip=True) if headline else 'No headline found')
    print('Link:', link if link else 'No link found')
    print('Description:', description.get_text(strip=True) if description else 'No description found')
    print('Image URL:', image)
    print('-' * 80)

# To follow pagination or get more articles, you'd need to handle the pagination logic based on the site's structure
