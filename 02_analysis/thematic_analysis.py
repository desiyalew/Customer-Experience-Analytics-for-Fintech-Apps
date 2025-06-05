# thematic_analysis.py

from sklearn.feature_extraction.text import TfidfVectorizer
from collections import Counter
import pandas as pd
import os

# Define themes and associated keywords
THEMES = {
    "UI & Design": ["interface", "design", "layout", "navigation", "look", "feel"],
    "Performance": ["slow", "fast", "lag", "crash", "performance", "speed"],
    "Security & Login": ["login", "password", "biometric", "fingerprint", "security", "otp"],
    "Customer Support": ["support", "help", "response", "chatbot", "service", "agent"],
    "Features & Functionality": ["transfer", "payment", "budget", "notifications", "loan", "card"],
    "Usability": ["easy", "simple", "user-friendly", "confusing", "complex"]
}

def extract_keywords(texts, top_n=100):
    """
    Extract top TF-IDF weighted keywords from the corpus.
    
    Args:
        texts (list): List of review texts
        top_n (int): Number of top keywords to extract
        
    Returns:
        list: Top keywords
    """
    vectorizer = TfidfVectorizer(stop_words='english', max_features=top_n, ngram_range=(1,2))
    tfidf_matrix = vectorizer.fit_transform(texts)
    feature_array = vectorizer.get_feature_names_out()
    tfidf_sum = tfidf_matrix.sum(axis=0)
    keywords = [(feature_array[i], tfidf_sum[0, i]) for i in range(len(feature_array))]
    keywords.sort(key=lambda x: x[1], reverse=True)
    return [k[0] for k in keywords]

def map_keywords_to_themes(keywords, theme_dict=THEMES):
    """
    Manually assign each keyword to one or more themes.
    
    Args:
        keywords (list): List of extracted keywords
        theme_dict (dict): Dictionary mapping themes to keywords
        
    Returns:
        dict: {keyword: [themes]}
    """
    keyword_theme_map = {}
    for keyword in keywords:
        matched_themes = []
        for theme, theme_keywords in theme_dict.items():
            if any(t.lower() in keyword.lower() for t in theme_keywords):
                matched_themes.append(theme)
        if matched_themes:
            keyword_theme_map[keyword] = matched_themes
        else:
            keyword_theme_map[keyword] = ["Other"]
    return keyword_theme_map

def assign_theme(review, keyword_theme_map):
    """
    Assign a theme to a review based on keywords.
    
    Args:
        review (str): Review text
        keyword_theme_map (dict): Mapping of keywords to themes
        
    Returns:
        str: Assigned theme(s), comma-separated
    """
    words = set(review.lower().split())
    themes_found = set()
    for word in words:
        for keyword, themes in keyword_theme_map.items():
            if word in keyword:
                themes_found.update(themes)
    return ", ".join(themes_found) if themes_found else "Other"

def run_thematic_analysis(input_path='../data/analyzed/analyzed_reviews.csv', output_path='../data/thematic_reviews/thematic_reviews.csv'):
    """
    Run thematic analysis on reviews.
    
    Args:
        input_path (str): Path to sentiment-analyzed CSV
        output_path (str): Output path for final CSV
    """
    df = pd.read_csv(input_path)

    # Extract top keywords
    print("Extracting keywords using TF-IDF...")
    all_texts = df['review'].tolist()
    top_keywords = extract_keywords(all_texts, top_n=100)

    # Map keywords to themes
    print("Mapping keywords to themes...")
    keyword_theme_map = map_keywords_to_themes(top_keywords)

    # Assign themes to each review
    print("Assigning themes to reviews...")
    df['theme'] = df['review'].apply(lambda x: assign_theme(x, keyword_theme_map))

    # Save output
    df.to_csv(output_path, index=False)
    print(f"Thematic analysis completed and saved to {output_path}")

if __name__ == "__main__":
    run_thematic_analysis()