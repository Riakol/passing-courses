row, col = int(input()), int(input())
text = [input() for _ in range(row*col)]
result = [print(*text[i:col + i]) for i in range(0, len(text), col)]
