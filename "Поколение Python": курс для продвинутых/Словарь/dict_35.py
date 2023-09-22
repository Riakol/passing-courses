# put your python code here
dnk = input().upper()
DNK_to_RNK = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}

for i in dnk:
    print(DNK_to_RNK[i], end='')