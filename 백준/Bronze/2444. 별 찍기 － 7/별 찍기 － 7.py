n = int(input())


for i in range(n - 1):
    stars = 1 + 2 * i
    spaces = n - i - 1
    print(' ' * spaces + '*' * stars)


for i in range(n - 1, -1, -1):
    stars = 1 + 2 * i
    spaces = n - i - 1
    print(' ' * spaces + '*' * stars)