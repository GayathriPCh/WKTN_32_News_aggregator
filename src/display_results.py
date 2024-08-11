import pandas as pd

def display_results():
    similarities = pd.read_csv('../data/similarities.csv')
    ap_df = pd.read_csv('../data/ap_news.csv')
    bbc_df = pd.read_csv('../data/bbc_news.csv')

    for i, row in similarities.iterrows():
        similar_indices = row.sort_values(ascending=False).index
        similar_scores = row.sort_values(ascending=False).values

        print(f"AP News Headline: {ap_df.loc[i, 'headline']}")
        print("Similar BBC News:")
        for j in similar_indices:
            print(f"Score: {similar_scores[j]} - BBC Headline: {bbc_df.loc[j, 'headline']}")
        print('-' * 80)

if __name__ == "__main__":
    display_results()
