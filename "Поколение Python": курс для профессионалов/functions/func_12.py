# put your python code here
arr = input()

if type(eval(arr)) == list:
    print(eval(arr)[-1])
elif type(eval(arr)) == tuple:
    print(eval(arr)[0])
elif type(eval(arr)) == set:
    print(len(eval(arr)))
