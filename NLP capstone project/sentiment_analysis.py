"""
Andrea Russo AR23110010747
T21 CAPSTONE PROJECT

"""

#%% Import libraries and modules

# NPL
import spacy
from spacytextblob.spacytextblob import SpacyTextBlob

# Data and numbers
import pandas as pd

# Spellcheck
from textblob import TextBlob

# Progress tracking
from tqdm import tqdm

# Evaluation and Plotting
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt


#%%
"""
1) Data Collection:
    Here we import the dataset into a dataframe and load the language model.
    We use a relative directory approach where we make sure the files are in the same folder.
"""

# Load language model
nlp = spacy.load('en_core_web_md') 
# Ensure spaCyTextBlob is added to the spaCy pipeline
nlp.add_pipe('spacytextblob')

# Load text into a dataframe
df = pd.read_csv('amazon_product_reviews.csv')

print(df.shape) # (28332, 24)


#%%
"""
2) Exploratory data analysis:
    Here we analyse the data and look for anomalies.
    Data analysis is key to obtain good results in any ML program
"""

# 1) Check for misisng values checking for nan and summing over boolens 

tot_nan = sum(df['reviews.text'].isna())
print(f"There are {tot_nan} NaN values in the reviews dataset.") # No missing values


# 2) Remove noise such as URLs, HTML tags and special characters

# Remove URLs
df['reviews.text'] = df['reviews.text'].replace(to_replace=r'http\S+', value='', regex=True)

# Remove HTML tags
df['reviews.text'] = df['reviews.text'].replace(to_replace=r'<.*?>', value='', regex=True)

# Remove special characters (retain alphabets, numbers and basic punctuation)
df['reviews.text'] = df['reviews.text'].replace(to_replace=r'[^a-zA-Z0-9\s.,!?]', value='', regex=True)


# 3) NORMALISE the text by turning it into lowercase

df['reviews.text'] = df['reviews.text'].apply(lambda x: x.lower() if isinstance(x, str) else x) # This handles possible numbers


#%%
"""
1. Spelling Correction
Tool Used: TextBlob
Description: The function starts by using TextBlob to correct spelling mistakes in the input text. This is a form of normalization that aims to fix typos and common misspellings, potentially making the text more uniform and easier to analyze.
2. Stopword Removal and Tokenization
Tool Used: spaCy
Description: After correcting the spelling, the corrected text is processed with spaCy. This step involves breaking down the text into individual tokens (words) and filtering out stopwords. Stopwords are common words that usually have little to no significance in understanding the sentiment or topic of the text and are removed to reduce the dimensionality of the data.
3. Lemmatization
Tool Used: spaCy
Description: Along with stopword removal, the function performs lemmatization on the remaining tokens. Lemmatization is the process of reducing words to their base or root form. Unlike stemming, lemmatization considers the context and part of speech of a word, making it a more sophisticated and accurate way of bringing words to their canonical forms.
4. Re-assembly
Description: Finally, the remaining lemmatized tokens (which are not stopwords or punctuation) are reassembled into a cleaned text string. This results in a version of the original text that's been normalized for spelling, devoid of less meaningful words, and reduced to base word forms.
"""

# 4) Apply spelling corrections, remove stopwords and punctuation,
#    then lemmatize the tokens

def clean_text(text):
    """Function to preprocess text: correct spelling, remove stopwords and lemmatize."""
    blob = TextBlob(text)
    corrected_text = str(blob.correct())
    doc = nlp(corrected_text)
    cleaned_text = ' '.join(token.lemma_ for token in doc if not token.is_stop and not token.is_punct)
    return cleaned_text

def preprocess_reviews(reviews):
    """Apply text cleaning and return the cleaned texts."""
    cleaned_reviews = [clean_text(review) for review in tqdm(reviews, desc="Cleaning and correcting reviews")]
    return cleaned_reviews

# Apply cleaning and correcting
tqdm.pandas(desc="Progress")
df['cleaned_reviews.text'] = preprocess_reviews(df['reviews.text'].tolist())

# Save cleaned dataframe for faster reloading
df.to_csv('cleaned_data.csv', index=False)


#%%
"""
3-4) Data transformation and modelling.
    Since we are useing a pre-trained ML model, we do not need to build
    the model from scratch includin transforming and fitting. 
    
    If this cell takes too long, jump to the next to load the cleaned data directly
"""
# Load cleaned dataframe
df = pd.read_csv('cleaned_data.csv')

# Extract the cleaned reviews into a new DataFrame
cleaned_reviews_df = df[['reviews.text','cleaned_reviews.text','reviews.rating']].copy()

# Drop rows with NaN values in the cleaned_reviews.text column
cleaned_reviews_df.dropna(subset=['cleaned_reviews.text'], inplace=True)

# Remove duplicate rows based on the cleaned_reviews.text column
cleaned_reviews_df.drop_duplicates(subset=['cleaned_reviews.text'], inplace=True)

# Reset the DataFrame index
cleaned_reviews_df.reset_index(drop=True, inplace=True)


def apply_sentiment_analysis(text):
    """Applies sentiment analysis on the provided text and returns sentiment scores."""
    doc = nlp(text)
    return doc._.polarity, doc._.subjectivity

# Apply sentiment analysis to each cleaned review
cleaned_reviews_df['sentiment_polarity'], cleaned_reviews_df['sentiment_subjectivity'] = zip(*cleaned_reviews_df['cleaned_reviews.text'].apply(apply_sentiment_analysis))

#%%
"""
5) Evaluation and reporting
"""

# For demonstration, let's print the sentiment for the first few reviews
print(cleaned_reviews_df[['reviews.rating', 'sentiment_polarity', 'sentiment_subjectivity']].head())

# Further analysis and evaluation can be performed based on the sentiment scores
# For example, categorizing reviews as positive, neutral, or negative based on polarity
cleaned_reviews_df['sentiment_category'] = cleaned_reviews_df['sentiment_polarity'].apply(
    lambda x: 'positive' if x > 0 else ('neutral' if x == 0 else 'negative'))


# Summarize the distribution of sentiments
print(cleaned_reviews_df['sentiment_category'].value_counts())

def categorize_rating(rating):
    if rating in [4, 5]:
        return 'positive'
    elif rating == 3:
        return 'neutral'
    elif rating in [1, 2]:
        return 'negative'

cleaned_reviews_df['rating_category'] = cleaned_reviews_df['reviews.rating'].apply(categorize_rating)

# Get the ground truth categories and the predicted sentiment categories
y_true = cleaned_reviews_df['rating_category']
y_pred = cleaned_reviews_df['sentiment_category']

# Calculate and print the classification report
report = classification_report(y_true, y_pred, labels=['positive', 'neutral', 'negative'], target_names=['positive', 'neutral', 'negative'])
print(report)

# Calculate the confusion matrix
cm = confusion_matrix(y_true, y_pred, labels=['positive', 'neutral', 'negative'])

# Enhanced display of the confusion matrix
fig, ax = plt.subplots(figsize=(8, 8))  # Larger figure size
disp = ConfusionMatrixDisplay(confusion_matrix=cm,
                              display_labels=['Positive', 'Neutral', 'Negative'])

# Use a color map of your choice
disp.plot(cmap=plt.cm.Purples, ax=ax)

# Customizations
ax.set_title('Sentiment Analysis Confusion Matrix', fontsize=18, pad=20)
ax.set_xlabel('Predicted Sentiment', fontsize=16, labelpad=10)
ax.set_ylabel('Actual Sentiment', fontsize=16, labelpad=10)
ax.tick_params(axis='both', which='major', labelsize=14)

plt.tight_layout()

# Save the plot as a high-quality PDF
plt.savefig('sentiment_analysis_confusion_matrix.pdf', format='pdf', dpi=300)

plt.show()
