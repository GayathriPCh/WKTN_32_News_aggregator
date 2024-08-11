import pandas as pd

def load_data():
    # Load the CSV files
    ap_df = pd.read_csv('data/ap_news.csv')
    bbc_df = pd.read_csv('data/bbc_news.csv')
    return ap_df, bbc_df

def find_similar_articles(df, column_name='Headline'):
    similar_articles = []
    
    # Ensure column contains strings and handle missing values
    df[column_name] = df[column_name].fillna('')  # Replace NaN with empty string
    df[column_name] = df[column_name].astype(str)  # Ensure all values are strings
    
    for i, row in df.iterrows():
        for j, other_row in df.iterrows():
            if i != j:
                # Check if the column value is a substring of the other column value
                if row[column_name] in other_row[column_name]:
                    similar_articles.append((row[column_name], other_row[column_name]))
                    
    return similar_articles


def categorize_and_find_similar():
    ap_df, bbc_df = load_data()
    # Combine dataframes (optional, for ease of comparison)
    combined_df = pd.concat([ap_df, bbc_df], ignore_index=True)
    
    # Find similar headlines
    similar_headlines = find_similar_articles(combined_df)
    return similar_headlines
