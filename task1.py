import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

nltk.download()

example_text = 'Hello mr. Smith, how are you doing today? The weather is greate and python is Awesome, The sky is pinkish-blue. You should not eat card-board'

print(sent_tokenize(example_text))

print(word_tokenize(example_text))
