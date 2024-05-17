def print_digits(n):
    def leng(length):
        if length >= 0:
            print(str(n)[length])
            leng(length - 1)

    leng(len(str(n)) - 1)
