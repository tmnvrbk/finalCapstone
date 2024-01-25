
Sentiment Analysis with Spacy and TextBlob

This program performs sentiment analysis on product reviews using the Spacy and TextBlob libraries. It utilizes natural language processing (NLP) techniques to analyze the sentiment of each review, categorizing them as very negative, negative, neutral, positive, or very positive.

Overview

The program reads product reviews from a CSV file (amazon_product_reviews.csv) and processes them through the Spacy NLP model to remove stop words. It then calculates the sentiment polarity of each review using TextBlob and categorizes it into one of the predefined sentiment classes.

Prerequisites

Spacy: Install Spacy by running pip install spacy.
TextBlob: Install TextBlob with pip install textblob.
Download the English language model for Spacy: python -m spacy download en_core_web_md.
Getting Started

Clone the repository.
Install the required libraries.
Run the provided Python script.
bash
Copy code
python sentiment_analysis.py
Output

The program outputs a DataFrame containing the original reviews and their corresponding sentiment categories. The sentiment is classified as very negative, negative, neutral, positive, or very positive based on the polarity calculated by TextBlob.

Contributing

Feel free to contribute to the improvement of this sentiment analysis program. Fork the repository, make your changes, and submit a pull request.
