def amount_of_num(n):
    sting_n = str(n)
    if len(str(sting_n)) > 0:
        return len(sting_n)
    else:
        return amount_of_num(n - 1)

    
print(amount_of_num(int(input())))
