import re

def abbreviate(phrase):
    words = re.findall(r'\b[A-Za-z]+', phrase)
    abbreviations = []

    for word in words:
        abbreviations.append(word[0])
        abbreviations.extend(re.findall(r'[A-Z]', word[1:]))
    return ''.join(abbreviations).upper()

