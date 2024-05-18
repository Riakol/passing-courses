def print_digits(n):
    def leng(length):
        if length <= len(str(n)) - 1:
            print(str(n)[length])
            leng(length + 1)

    leng(0)
