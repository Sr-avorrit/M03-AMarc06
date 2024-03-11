def wordFreq(s):
    s = ''.join(c for c in s if c not in ('!', '.', ':', ',', '?', ';', '-', '_')).lower()
    words = s.split()
    wordFreq = {}
    for word in words:
        if word.lower() in wordFreq:
            wordFreq[word.lower()] += 1
        else:
            wordFreq[word.lower()] = 1
    return wordFreq


def commonWord(wordFreq):
    commonWord = max(wordFreq, key=wordFreq.get)
    return (commonWord, wordFreq[commonWord])

text = "The cat ate the food of the other cat. The dog drank water from the bowl."
wordFreqDict = wordFreq(text)
print(wordFreqDict)
mostCommonWord = commonWord(wordFreqDict)
print(mostCommonWord)