import gensim
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import remove_stopwords, STOPWORDS

# Get user input for the text
sample_text = input("Please enter a sentence: ")

# Tokenize into words using Gensim's simple_preprocess
words = simple_preprocess(sample_text)
print("\nWords:")
print(words)

# Remove stop words using Gensim's remove_stopwords and custom stopwords list
filtered_text = remove_stopwords(sample_text)
filtered_words = simple_preprocess(filtered_text)
print("\nFiltered Words (Stop Words Removed):")
print(filtered_words)
