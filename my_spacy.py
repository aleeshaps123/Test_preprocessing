import spacy
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Load the English language model
nlp = spacy.load('en_core_web_sm')

# Get user input for the text
sample_text = input("Please enter a sentence: ")

# Process the text with spacy
doc = nlp(sample_text)

# Tokenize into words using nltk
words = word_tokenize(sample_text)
print("\nTokenized Words:")
print(words)


# Initialize the Porter Stemmer from nltk
stemmer = PorterStemmer()

# Perform stemming on each word
stemmed_words = [stemmer.stem(word) for word in words]
print("\nStemmed Words:")
print(stemmed_words)

# Lemmatize each word
lemmatized_words = [token.lemma_ for token in doc]
print("\nLemmatized Words:")
print(lemmatized_words)

# Get the list of stop words from nltk
stop_words = set(stopwords.words('english'))

# Remove stop words
filtered_words = [word for word in words if word.lower() not in stop_words]
print("\nFiltered Words (Stop Words Removed):")
print(filtered_words)


