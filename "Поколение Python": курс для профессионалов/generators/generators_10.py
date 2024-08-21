def is_prime(number): 
    if number < 2: 
        return False 
    return all(number % i for i in range(2, int(number ** 0.5) + 1))

