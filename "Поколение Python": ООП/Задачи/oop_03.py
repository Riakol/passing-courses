def inversions(sequence):
    counter = 0
    for i in range(len(sequence)):
        for j in range(i + 1, len(sequence)):
            if sequence[i] > sequence[j]:
                counter += 1
    return counter

