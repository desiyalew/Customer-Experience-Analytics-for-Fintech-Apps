from google_play_scraper import reviews, Sort
import pandas as pd

def fetch_reviews(package_name, lang='en', count=500):
    result, continuation_token = reviews(
        package_name,
        lang=lang,
        country="ET",
        sort=Sort.MOST_RELEVANT,
        count=count
    )
    return pd.DataFrame(result)

def save_reviews(df, filename):
    df.to_csv(filename, index=False)

if __name__ == "__main__":
    apps = {
        "CBE": "com.combanketh.mobilebanking",
        "BOA": "com.boa.boaMobileBanking",
        "Dashen": "com.dashen.dashensuperapp"
    }

    for name, package in apps.items():
        print(f"Fetching reviews for {name}")
        df = fetch_reviews(package)
        save_reviews(df, f"../data/raw/{name.lower()}_reviews.csv")