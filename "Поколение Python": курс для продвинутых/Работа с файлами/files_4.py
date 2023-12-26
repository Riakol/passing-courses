m_file = open('numbers.txt', 'r', encoding='utf-8')
digits = m_file.readlines()

for i in range(len(digits) - 1):
    print(int(digits[0]) + int(digits[1]))

m_file.close()
