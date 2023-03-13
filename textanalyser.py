import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.sentiment import SentimentIntensityAnalyzer
from textstat.textstat import *
# download required NLTK packages
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('opinion_lexicon')
nltk.download('stopwords')
nltk.download('vader_lexicon')
# initialize sentiment analyzer
sia = SentimentIntensityAnalyzer()

# define function to clean text
def clean_text(text):
    # convert to lowercase
    text = text.lower()
    # remove stopwords
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(text)
    filtered_text = [word for word in word_tokens if word not in stop_words]
    return ' '.join(filtered_text)

# define function to get sentiment scores and other features
def get_word_counts(text):
    # calculate sentiment scores
    scores = sia.polarity_scores(text)
    # calculate other features
    sentences = sent_tokenize(text)
    word_count = len(word_tokenize(text))
    avg_sentence_length = word_count / len(sentences)
    complex_word_count = 0
    personal_pronouns = 0
    for word, pos in nltk.pos_tag(word_tokenize(text)):
        # count complex words (words with 3 or more syllables)
        if textstat.syllable_count(word) >= 3:
            complex_word_count += 1
        # count personal pronouns (PRP)
        if pos == 'PRP':
            personal_pronouns += 1
    # calculate percentage of complex words
    complex_word_percentage = complex_word_count / word_count
    # calculate FOG index
    fog_index = 0.4 * (avg_sentence_length + complex_word_percentage)
    # calculate average word length
    word_lengths = [len(word) for word in word_tokenize(text)]
    avg_word_length = sum(word_lengths) / word_count
    # calculate syllables per word
    syllables_per_word = textstat.syllable_count(text) / word_count
    return pd.Series([scores['pos'], scores['neg'], scores['pos'] - scores['neg'], scores['compound'], avg_sentence_length, complex_word_percentage, fog_index, word_count / len(sentences), complex_word_count, word_count, syllables_per_word, personal_pronouns, avg_word_length])

# read input data from Excel file
df = pd.read_excel('Output.xlsx')

# clean text
df['Clean_Text'] = df['Text'].apply(clean_text)

# calculate sentiment scores and other features
df[['Positive_Score', 'Negative_Score', 'Polarity_Score', 'Subjectivity_Score', 'Avg_Sentence_Length', 'Percentage_of_Complex_Words', 'FOG_Index', 'Avg_Number_of_Words_per_Sentence', 'Complex_Word_Count', 'Word_Count', 'Syllables_per_Word', 'Personal_Pronouns', 'Avg_Word_Length']] = df['Clean_Text'].apply(get_word_counts)

# write data to output Excel file
df.to_excel('Output_data_structure.xlsx', index=False)
