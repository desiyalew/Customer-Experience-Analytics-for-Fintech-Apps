# Task 1: Data Collection and Preprocessing

This module is responsible for scraping user reviews from the Google Play Store and preprocessing them for analysis.

## Files

-   **`scraper.py`**: Contains the script to scrape reviews for CBE, BOA, and Dashen Bank apps using the `google-play-scraper` library.
    -   Target: 500+ reviews per bank.
    -   Data collected: Review Text, Rating, Date, Bank/App Name, Source (Google Play).
    -   Output: `../data/raw/boa_reviews.csv`, `../data/raw/cbe_reviews.csv` , and `../data/raw/dashen_reviews.csv`
-   **`preprocess.py`**: Contains the script to clean the raw review data.
    -   Tasks: Handles duplicates, missing data, normalizes dates (to YYYY-MM-DD).
    -   Input: `../data/raw/boa_reviews.csv`, `../data/raw/cbe_reviews.csv` , and `../data/raw/dashen_reviews.csv`
    -   Output: `../data/Cleaned_data/cleaned_reviews.csv` (columns: review, rating, date, bank, source)
-   **`requirements.txt`**: Python libraries required for this module (e.g., `google-play-scraper`,`numpy`,`pandas`).

## Setup

1.  Ensure you are in the project's virtual environment.
2.  Install dependencies:
    ```bash
    pip install -r 01_data_collection/requirements.txt
    ```

## How to Run

1.  **Scrape Reviews**:
    ```bash
    python scraper.py
    ```
    This will generate `../data/raw/boa_reviews.csv`, `../data/raw/cbe_reviews.csv` , and `../data/raw/dashen_reviews.csv`.
    *Note: You might need to identify the correct app IDs for each bank on the Google Play Store and configure them in `scraper.py`.*

2.  **Preprocess Reviews**:
    ```bash
    python preprocess.py
    ```
    This will take `../data/raw/boa_reviews.csv`, `../data/raw/cbe_reviews.csv` , and `../data/raw/dashen_reviews.csv`. as input and generate `../data/Cleaned_data/cleaned_reviews.csv`.

## Expected Output

-   `../data/raw/boa_reviews.csv`, `../data/raw/cbe_reviews.csv` , and `../data/raw/dashen_reviews.csv`: Unprocessed reviews directly from scraping.
-   `../data/Cleaned_data/cleaned_reviews.csv`: Cleaned dataset ready for analysis, with columns: `review`, `rating`, `date`, `bank`, `source`.
-   Minimum 1200+ reviews in `cleaned_reviews.csv` with <5% missing data for critical fields.

## Git Workflow

-   Work on the `task-1` branch.
-   Commit frequently with meaningful messages.
-   Example commit: `feat: Implement scraper for CBE reviews`
-   Example commit: `fix: Handle missing dates during preprocessing`
-   Once complete, merge `task-1` into `main` (or a development branch if used).