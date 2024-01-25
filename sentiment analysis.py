import spacy
import pandas as pd
from textblob import TextBlob

# Path to the file where the reviews are stored
file_path = "/Users/timon/Dropbox/TV23110010620/Data Science (Fundamentals)/T21 - Capstone Project - NLP Applications/amazon_product_reviews.csv"

# Function that will remove all stop words from a text through nlp
def remove_stop_words(text):
    doc = nlp(text)
    return ' '.join([token.text for token in doc if not token.is_stop])

# Function to get sentiment polarity 
def get_sentiment(text): 
    sentiment = TextBlob(text).sentiment.polarity
    # Sentiment polarity is obtained as a value between -1 and 1
    # Below this will be expressed in a range from negative to positive
    if sentiment < -0.5: 
        sentiment = "Very negative"
    elif sentiment < 0: 
        sentiment = "Negative"
    elif sentiment == 0: 
        sentiment = "Neutral"
    elif sentiment > 0.5: 
        sentiment = "Very positive"
    elif sentiment > 0: 
        sentiment = "Positive"

    # Return the polarity
    return sentiment


# Loading the nlp model into variable nlp
nlp = spacy.load('en_core_web_md') 

# Loading the .csv into a dataframe
reviews_df = pd.read_csv(file_path)

# Clear out any empty values
reviews_df = reviews_df.dropna(subset=['reviews.text'])

# Apply the function remove_stop_words to remove all stop words from the reviews column into a new column
reviews_df['reviews_no_stop_words'] = reviews_df['reviews.text'].apply(remove_stop_words)

# Apply the function get_sentiment to the 'reviews_no_stop_words' column 
reviews_df['sentiment'] = reviews_df['reviews_no_stop_words'].apply(get_sentiment) 

# Display the first 20 rows of the DataFrame with the new sentiment column 
print(reviews_df[['reviews.text', 'reviews_no_stop_words', 'sentiment']].head(20))
