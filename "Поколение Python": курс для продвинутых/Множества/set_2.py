n, m, k, x, y, z, t, a = (int(input()) for _ in range(8))

A_and_B = n + m - t - x
B_and_C = m + k - t - y
A_and_C = n + k - t - z

one_book = (n - (t + A_and_B + A_and_C)) + (m - (t + A_and_B + B_and_C)) + (k - (t + A_and_C + B_and_C))
two_books = A_and_B + B_and_C + A_and_C
no_books = a - (one_book + two_books + t)

print(f"{one_book}\n{two_books}\n{no_books}")
