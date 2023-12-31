with open('lines.txt', 'r', encoding='utf-8') as my_file:
   content = my_file.readlines()
   length = len(max(content, key=len))
   for row in list(map(lambda x: x[:-1], filter(lambda x: len(x) >= length, content))):
       print(row)
