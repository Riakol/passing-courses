# put your python code here
list_of_students = [[any(item == '5' for item in input().split()[1:]) for _ in range(int(input()))] for _ in range(int(input()))]
print(['NO', 'YES'][all([any(student) for student in list_of_students])])





