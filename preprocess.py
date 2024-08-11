import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import re

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'\W+', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def preprocess_data(file_path):
    df = pd.read_csv(file_path)
    df['description'] = df['description'].apply(preprocess_text)
    return df

if __name__ == "__main__":
    ap_df = preprocess_data('ap_news.csv')
    bbc_df = preprocess_data('bbc_news.csv')
    ap_df.to_csv('ap_news_preprocessed.csv', index=False)
    bbc_df.to_csv('bbc_news_preprocessed.csv', index=False)
