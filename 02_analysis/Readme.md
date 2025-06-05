# Sentiment and Thematic Analysis Module (`02_analysis`)

## Overview

This module is responsible for Task 2 of the project: quantifying review sentiment and identifying key themes from the user reviews. This helps uncover satisfaction drivers and pain points for each bank. It consists of two main scripts: `sentiment_analyzer.py` for sentiment analysis and `thematic_analyzer.py` for thematic analysis.

## Files

*   `sentiment_analyzer.py`: Performs sentiment analysis on the preprocessed reviews.
*   `thematic_analyzer.py`: Conducts thematic analysis to identify common topics and themes in the reviews.

---

## 1. Sentiment Analysis (`sentiment_analyzer.py`)

### Purpose

This script analyzes the sentiment of each review, classifying it as positive, negative, or neutral, and assigns a confidence score.

### Functionality

1.  **Initialization:**
    *   Loads a pre-trained sentiment analysis model (`distilbert-base-uncased-finetuned-sst-2-english`) from the Hugging Face Transformers library. This model is fine-tuned for sentiment classification on the SST-2 dataset.

2.  **`analyze_sentiment(text)`:**
    *   Takes a single review text as input.
    *   Truncates the input text to the first 512 tokens to comply with the model's input size limit.
    *   Passes the text to the sentiment analysis pipeline.
    *   Returns a tuple containing the sentiment label (e.g., 'POSITIVE', 'NEGATIVE') and the corresponding confidence score.
    *   Includes basic error handling: if analysis fails, it returns ('NEUTRAL', 0.0).

3.  **`run_sentiment_analysis(input_path, output_path)`:**
    *   The main function to process a dataset.
    *   **Input:** Reads a CSV file (e.g., `cleaned_reviews.csv` from preprocessing) specified by `input_path`. This CSV is expected to have a column named `review` containing the review texts.
    *   Applies the `analyze_sentiment` function to each review in the `review` column.
    *   Adds two new columns to the DataFrame: `sentiment_label` and `sentiment_score`.
    *   **Output:** Saves the updated DataFrame with sentiment information to a new CSV file specified by `output_path` (e.g., `analyzed_reviews.csv`).

### Input/Output (as per provided script)

*   **Input File:** `../data/Cleaned_data/cleaned_reviews.csv` (relative path)
    *   *Project Integration Note:* In the main project pipeline, this input path would typically be derived from `config.ini` (e.g., `config['PATHS']['PROCESSED_DATA_DIR'] + "all_banks_reviews_processed.csv"`).
*   **Output File:** `../data/analyzed/analyzed_reviews.csv` (relative path)
    *   *Project Integration Note:* The main project pipeline might consolidate this output into a single file after thematic analysis, using a path from `config.ini`.

### Standalone Execution (as per provided script)

The script can be run directly:
```bash
python 02_analysis/sentiment_analyzer.py
