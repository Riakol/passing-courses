# put your python code here
my_dict = {}

for i in range(int(input())):
    text = input().split()
    my_dict[text[0]] = text[1]
    my_dict[text[1]] = text[0]

print(my_dict[input()])