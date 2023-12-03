# put your python code here
coefficients, arg = input().split(), int(input())

def evaluate(coefficients, x):
    powers = map(lambda j: len(coefficients) - j, range(1, len(coefficients) + 1))
    return sum(map(lambda i, j: int(i) * x ** j, coefficients, powers))


print(evaluate(coefficients, arg))