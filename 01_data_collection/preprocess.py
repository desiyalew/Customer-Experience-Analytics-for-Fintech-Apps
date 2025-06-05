import pandas as pd
from datetime import datetime

def clean_date(date_str):
    try:
        return datetime.fromtimestamp(date_str / 1000).strftime('%Y-%m-%d')
    except:
        return None

def preprocess(df):
    df.drop_duplicates(subset=['content'], inplace=True)
    df['date'] = df['at'].apply(clean_date)
    df['bank'] = df['source_app']
    df['rating'] = df['score']
    df['review'] = df['content']
    return df[['review', 'rating', 'date', 'bank', 'source_app']]

if __name__ == "__main__":
    combined = pd.concat([
        pd.read_csv("../data/raw/cbe_reviews.csv").assign(source_app="CBE"),
        pd.read_csv("../data/raw/boa_reviews.csv").assign(source_app="BOA"),
        pd.read_csv("../data/raw/dashen_reviews.csv").assign(source_app="Dashen")
    ], ignore_index=True)

    cleaned = preprocess(combined)
    cleaned.to_csv("../data/Cleaned_data/cleaned_reviews.csv", index=False)