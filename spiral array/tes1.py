def counter(n):
    for i in range(1, n*n):
        yield i+1


n = 11
a = [[1 for x in range(n)] for y in range(n)]
x = y = n//2
val = counter(n)

for i in range(2, n, 2):
    y += 1
    x -= 1
    for k in range(i):
        x += 1
        a[x][y] = next(val)
    for k in range(i):
        y -= 1
        a[x][y] = next(val)
    for k in range(i):
        x -= 1
        a[x][y] = next(val)
    for k in range(i):
        y += 1
        a[x][y] = next(val)

for i in range(n):
    for j in range(n):
        print(a[i][j], end="")
        print("  ", end="")
    print("\n")
