# init assign for rows and cols
rows, cols = (4, 4)

# initialize the arr for arr[position][position]
arr = [[0 for i in range(cols)] for j in range(rows)]
nilai = 0

# arr[1][2] = 12
for i in range(rows):
    for j in range(cols):
        arr[i][j] = nilai
        nilai += 1


for row in arr:
    print("""
            """, row)
