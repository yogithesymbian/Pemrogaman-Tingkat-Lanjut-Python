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

isi = 0  # init for arr value (increment)


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
            if i == 1:
                if j == rows:
                    print(i, j)


def arrMethod1(isi):
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


def arrMethod2(isi):
    print("""

        =================METHOD 2 VERTICAL=======================

        """)
    # method 2
    for i in range(cols):  # vertical
        for j in range(rows):
            isi += 1
            arr[j][i] = isi

    # show the array
    for row in arr:
        print("""
        """, row)


def start():
    print("hello world")
    flowAssignTest()
    # arrMethod1(0)
    # arrMethod2(0)


if __name__ == '__main__':
    try:
        start()
    except KeyboardInterrupt as err:
        print(
            "\n[!] By ...: thanks for use my code (c) 2019 github.com/yogithesymbian")
        sys.exit(0)
