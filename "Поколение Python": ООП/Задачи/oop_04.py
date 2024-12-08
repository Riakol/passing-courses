# put your python code here
def inversions(sequence):
    return len(sequence) - len(set(sequence))

text = [x.strip() for x in open(0)]
print(inversions(text))

