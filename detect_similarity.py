import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

def detect_similarity(ap_features, bbc_features):
    similarities = cosine_similarity(ap_features, bbc_features)
    return similarities

if __name__ == "__main__":
    ap_df = pd.read_csv('ap_news_preprocessed.csv')
    bbc_df = pd.read_csv('bbc_news_preprocessed.csv')

    from extract_features import extract_features

    ap_features = extract_features('ap_news_preprocessed.csv')
    bbc_features = extract_features('bbc_news_preprocessed.csv')

    similarities = detect_similarity(ap_features, bbc_features)

    # Save or process the similarity results
    pd.DataFrame(similarities).to_csv('../data/similarities.csv', index=False)
