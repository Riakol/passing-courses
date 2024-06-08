# put your python code here
math_f = input()
num_range = [int(i) for i in input().split()]
answer = [eval(math_f) for x in range(num_range[0], num_range[1] + 1)]

print(f"Минимальное значение функции {math_f} на отрезке [{num_range[0]}; {num_range[1]}] равно {min(answer)}")
print(f"Максимальное значение функции {math_f} на отрезке [{num_range[0]}; {num_range[1]}] равно {max(answer)}")
