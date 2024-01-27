def filter_anagrams(word, words):
    return [i for i in words if sorted(i) == sorted(word)]

