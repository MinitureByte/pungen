# Pungen

Pun generation / lookup utility

# Notes

- uses jellyfish for phonetic matching of strings

* oxford english dictionary api for thesaurus matching
  - use word embedding to represent meaning of words or concept net
  - https://en.wikipedia.org/wiki/Word_embedding
  - http://conceptnet5.media.mit.edu/
    - https://github.com/commonsense/conceptnet5/wiki/API
  - https://relatedwords.org
  - http://storage.googleapis.com/books/ngrams/books/datasetsv2.html
  - http://www.speech.cs.cmu.edu/cgi-bin/cmudict

`pun --about "plant"`

1. looks up words related to plants

`pun --soundlike "leaf"`

1. search corpus for high ranking words that sound similar to leaf
   -> leave
