# Import necessary libraries
from nltk.corpus import stopwords
from collections import Counter

# Read the contents of the text file
with open('unfiltered.txt', 'r') as file:
    text = file.read()

# Define a stop word list
stop_words = set(stopwords.words('english'))

# Tokenize the text and remove stop words
words = text.split()
filtered_words = [word.lower() for word in words if word.lower() not in stop_words]

# Count word frequencies
word_count = Counter(filtered_words)

output = [(count, word) for word, count in word_count.items()]
output.sort(reverse=True)


topN = 10
# Display word frequency count
for count, word in output[:topN]:
    print(f'{word}: {count}')
