# sentiment_analysis.py

from transformers import pipeline
import pandas as pd
import os

# Initialize Hugging Face sentiment analysis pipeline
sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

def analyze_sentiment(text):
    """
    Analyze the sentiment of a given text.
    
    Args:
        text (str): Input review text
        
    Returns:
        tuple: (label, score)
    """
    try:
        result = sentiment_pipeline(text[:512])  # Limit to 512 tokens for BERT models
        return result[0]['label'], result[0]['score']
    except Exception as e:
        print(f"Error analyzing sentiment: {e}")
        return "NEUTRAL", 0.0

def run_sentiment_analysis(input_path='../data/Cleaned_data/cleaned_reviews.csv', output_path='../data/analyzed/analyzed_reviews.csv'):
    """
    Run sentiment analysis on all reviews in the dataset.
    
    Args:
        input_path (str): Path to input CSV file with reviews
        output_path (str): Path to save output CSV file
    """
    # Load cleaned reviews
    df = pd.read_csv(input_path)

    # Apply sentiment analysis
    print("Running sentiment analysis on reviews...")
    df[['sentiment_label', 'sentiment_score']] = df['review'].apply(
        lambda x: pd.Series(analyze_sentiment(x))
    )

    # Save updated dataframe
    if not os.path.exists('data'):
        os.makedirs('data')
    df.to_csv(output_path, index=False)
    print(f"Sentiment analysis completed and saved to {output_path}")

if __name__ == "__main__":
    run_sentiment_analysis()