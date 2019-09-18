__author__ = "Yogi Arif Widodo"
__copyright__ = "Copyright 2019"
__version__ = "0.1"
__email__ = "yogirenbox33@gmail.com"
__status__ = "Development"
__codename__ = 'Pemrograman-Tingkat-Lanjut-Python'
__source__ = "https://github.com/yogithesymbian/Pemrograman-Tingkat-Lanjut-Python"
__info__ = "URL scodeid"

import sys
# Python 3 program to demonstrate working
# of method 1 (horizontal) and method 2 (vertical) and method3 (obat nyamuk).

# init assign for rows and cols
rows, cols = (5, 6)

# initialize the arr for arr[position][position]
arr = [[0 for i in range(cols)] for j in range(rows)]


def flowAssignTest():  # log flow assign testing
    for i in range(rows):
        for j in range(cols):
            # horizontal <------ rows
            # print(i, j)  # horizontal left to right
            # print(x, x) # horitzontal left to right then right to left

            # print(j, i)  # vertical down from left to right
            # print(x, x) # vertical down from left to right then up
            # vertical <--------
            # but u will get the error index out of bound, so u need change the rows to cols and else too

            # obat nyamuk
            if i == 0:
                print(i, j)
            if j == rows:
                # if i == 1:
                #     print(i, j)
                # if i == 2:
                #     print(i, j)
                # if i == 3:
                #     print(i, j)
                if i != 0 and i != rows - 1:
                    print(i, j)

    for i in range(rows):
        for j in reversed(range(cols)):
            # j = [j]
            # j.reverse()
            # j.__reversed__
            if i == rows - 1:
                print(i, j)
                # downToLeft = [j]
                # downToLeft.sort(reverse=True)
                # print(downToLeft)
                # print(sorted(list([j]), reverse=True))
    for i in reversed(range(rows)):
        for j in range(cols):
            if j == 0:
                if i != rows-1 and i != 0:
                    print(i, 0)

    for i in range(rows):
        for j in range(cols):
            if (i != rows - 1 and i != 0 and i != 1) and (j != 0 and j != cols - 1):
                if i != rows - 2:
                    print(i, j)
                # if i != rows - 3:
                #     print(i, j)

    for i in range(rows):
        for j in reversed(range(cols)):
            if (i != rows - 1 and i != 0 and i != 1) and (j != 0 and j != cols - 1):
                if i != rows - 3:
                    print(i, j)
                    # end of flow obat nyamuk


def resultArray(data1, data2):
    isi = 0  # init for arr value (increment)
    for i in range(data1):
        for j in range(data2):
            isi += 1
            arr[j][i] = isi

    # arr[0][5] = 1
    # show the array
    for row in arr:
        print("""
            """, row)


def arrMethod1(isi):
    print("""

    =================METHOD 1 HORIZONTAL=======================

    """)
    # method 1
    resultArray(rows, cols)  # horizontal resultArray(i, j)


def arrMethod2(isi):
    print("""

        =================METHOD 2 VERTICAL=======================

        """)
    # method 2
    ##
    # just invert the first method
    # to get vertical flow assign
    # ##
    resultArray(cols, rows)  # vertical resultArray(j,i)


def arrMethod3(isi):
    print("""

        =================METHOD 3 CAPSULE=======================

        """)
    # method 3
    for i in range(rows):  # vertical
        for j in range(cols):
            isi += 1
            # arr[i][j] = isi
            # obat nyamuk
            if i == 0:  # top assign
                arr[i][j] = isi
            if j == rows:  # End Assign rows.length
                # if i == 1:
                #     print(i, j)
                # if i == 2:
                #     print(i,j)
                arr[i][j] = isi
            if i == cols:
                print(i, j)

    # show the array
    for row in arr:
        print("""
        """, row)


def start():
    # flowAssignTest()
    # arrMethod1(0)
    arrMethod2(0)
    # arrMethod3(0)


if __name__ == '__main__':
    try:
        start()
    except KeyboardInterrupt as err:
        print(
            "\n[!] By ...: thanks for use my code (c) 2019 github.com/yogithesymbian")
        sys.exit(0)
