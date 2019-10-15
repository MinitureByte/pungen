import math
import json
import fuzzy
import Levenshtein

soundex = fuzzy.Soundex(4)

words = {}

THE_WORD = "leaf"
print(THE_WORD, soundex(THE_WORD))
THRESHOLD = 3

# with open("words_dictionary.json", "r") as f:
#     data = json.load(f)
#     for word in data:
#         words[word] = {"soundex": soundex(word)}

words = ["two", "to", "leaf", "leave", "leafgirl"]

distList = {}

for word in words:
    sd = soundex(word)
    distList[word] = {
        "soundex": sd,
        "distance": Levenshtein.distance(soundex(THE_WORD), sd)
    }

print(distList)

# # print(words)
# similar = []

# for word in words:
#     if Levenshtein.distance(words[word]["soundex"], soundex(THE_WORD)) < THRESHOLD:
#         similar.append(words[word])

# print(similar)
