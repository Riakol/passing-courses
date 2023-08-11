# put your python code here
m, n = [int(input()) for _ in range(2)]

mathematics = {input() for _ in range(m)}
informatics = {input() for _ in range(n)}

if (mathematics | informatics) - (mathematics & informatics):
    print(len((mathematics | informatics) - (mathematics & informatics)))
else:
    print('NO')