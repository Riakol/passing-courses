# put your python code here
m, n = [int(input()) for _ in range(2)]
mathem = {input() for _ in range(m)}
informatcs = {input() for _ in range(n)}

slozhene = mathem | informatcs
peresechenie = mathem & informatcs

if mathem ^ informatcs:
    if len(mathem) != m:
        exit(print(len(informatcs)))
    print(len(mathem ^ informatcs))
else:
    print('NO')