# Python 3 program to demonstrate working
# of method 1 (horizontal) and method 2 (vertical) and method3 (obat nyamuk).

# init assign for rows and cols
rows, cols = (5, 6)

# initialize the arr for arr[position][position]
arr = [[0 for i in range(cols)] for j in range(rows)]

isi = 0  # init for arr value (increment)

# log flow assign testing
# for i in range(rows):
#     for j in range(cols):
# print(i, j)  # horizontal (0,0 .. 4.0)
# print(j, i) # vertical but u will get the error index out of bound , so u need change the rows to cols and else too
print("""

=================METHOD 1 HORIZONTAL=======================

""")
# method 1
for i in range(rows):  # horizontal
    for j in range(cols):
        isi += 1
        arr[i][j] = isi

# arr[0][5] = 1
# show the array
for row in arr:
    print("""
    """, row)

print("""

=================METHOD 2 VERTICAL=======================

""")

isi = 0
# method 2
for i in range(cols):  # vertical
    for j in range(rows):
        isi += 1
        arr[j][i] = isi

# show the array
for row in arr:
    print("""
    """, row)
