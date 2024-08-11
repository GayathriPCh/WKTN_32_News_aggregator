import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

def extract_features(file_path):
    df = pd.read_csv(file_path)
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(df['description'])
    return X

if __name__ == "__main__":
    ap_features = extract_features('ap_news_preprocessed.csv')
    bbc_features = extract_features('bbc_news_preprocessed.csv')
    # Save features if needed for further processing
