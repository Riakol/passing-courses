# put your python code here
num_dict = int(input())
slang_list = [input() for _ in range(num_dict)]
slang_dict = {str(i)[:str(i).index(':')].lower(): str(i)[str(i).index(':') + 2:] for i in slang_list}
num_words = int(input())
print(*[slang_dict.setdefault(input().lower(), 'Не найдено') for _ in range(num_words)], sep='\n')