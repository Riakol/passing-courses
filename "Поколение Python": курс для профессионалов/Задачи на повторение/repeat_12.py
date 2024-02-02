d1, d2, d3 = [int(input()) for _ in range(3)]

if d1 == d2 == d3 or (d1 + d2 + d3) - max(d1, d2, d3) > max(d1, d2, d3):
    print(d1 + d2 + d3)

elif max(d1, d2, d3) == d1:
    print((d2 + d3) * 2)

elif max(d1, d2, d3) == d2:
    print((d1 + d3) * 2)

elif max(d1, d2, d3) == d3:
    print((d1 + d2) * 2)
    