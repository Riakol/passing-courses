def palindromes(): 
    n = 0 
    while True: 
        n += 1 
        s = str(n) 
        if s == s[::-1]: 
            yield n

            