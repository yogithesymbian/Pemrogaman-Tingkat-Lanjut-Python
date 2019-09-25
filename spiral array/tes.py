# init assign for rows and cols
rows, cols = (5, 6)

# initialize the arr for arr[position][position]
arr = [[2 for i in range(cols)] for j in range(rows)]

arr[1][2] = 12

for row in arr:
    print("""
            """, row)
