import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import stopwords

# Ensure you have the required NLTK data
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('stopwords')

# Get user input for the text
sample_text = input("Please enter a sentence: ")

# Tokenize into words
words = word_tokenize(sample_text)
print("\nWords:")
print(words)

# Initialize the Porter Stemmer
stemmer = PorterStemmer()

# Perform stemming on each word
stemmed_words = [stemmer.stem(word) for word in words]
print("\nStemmed Words:")
print(stemmed_words)

# Initialize the WordNet Lemmatizer
lemmatizer = WordNetLemmatizer()

# Perform lemmatization on each word
lemmatized_words = [lemmatizer.lemmatize(word) for word in words]
print("\nLemmatized Words:")
print(lemmatized_words)

# Get the list of stop words
stop_words = set(stopwords.words('english'))

# Remove stop words
filtered_words = [word for word in words if word.lower() not in stop_words]
print("\nFiltered Words (Stop Words Removed):")
print(filtered_words)
