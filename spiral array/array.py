__author__ = "Yogi Arif Widodo"
__copyright__ = "(C) 2019"
__version__ = "0.1"
__email__ = "yogirenbox33@gmail.com"
__status__ = "Development"
__codename__ = 'Pemrograman-Tingkat-Lanjut-Python'
__source__ = "https://github.com/yogithesymbian/Pemrograman-Tingkat-Lanjut-Python"
__info__ = "URL scodeid"
# MY - REFERENCE
# https://www.geeksforgeeks.org/print-a-given-matrix-in-spiral-form/
import sys
from color import ColorPrint as warna
# Python 3 program to demonstrate working
# of method 1 (horizontal) and method 2 (vertical) and method3 (obat nyamuk).

# init assign for rows and cols
rows, cols = (5, 6)

# initialize the arr for arr[position][position]
arr = [[0 for i in range(cols)] for j in range(rows)]
#  arr[0..6][0..5]


def flowAssignTest():  # log flow assign testing
    for i in range(rows):
        for j in range(cols):
            # horizontal <------ rows
            # print(i, j)  # horizontal left to right

            # if i % 2 == 0:
            #     print("-")
            # else:
            #     # j.__invert__
            #     # rever = reversed([j])
            #     rever = sorted([j])
            #     print(i, rever)
            # print(x, x) # horitzontal left to right then right to left

            # print(j, i)  # vertical down from left to right
            # print(x, x) # vertical down from left to right then up
            # vertical <--------
            # but u will get the error index out of bound, so u need change the rows to cols and else too

            # obat nyamuk
            # TOP
            if i == 0:
                print(i, j)
            # END TO DOWN
            if j == rows:
                # if i == 1:
                #     print(i, j)
                # if i == 2:
                #     print(i, j)
                # if i == 3:
                #     print(i, j)
                if i != 0 and i != rows - 1:
                    print(i, j)

    # END - DOWN - HORIZONTAL - LEFT
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

    # LEFT - TOP
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


def resultArray(data1, data2, stat):
    isi = 0  # init for arr value (increment)
    for i in range(data1):
        for j in range(data2):
            isi += 1
            if stat == 1:
                if i % 2 == 0:
                    arr[i][j] = isi
                else:
                    arr[i][j] = isi
            if stat == 2:
                arr[j][i] = isi

    # arr[0][5] = 1
    # show the array
    for row in arr:
        print("""
            """, row)


def arrMethod1(isi):
    warna.print_pass("""
    _______________________________________________
    * HORIZONTAL
    """)
    # method 1
    resultArray(rows, cols, stat=1)  # horizontal resultArray(i, j)


def arrMethod2(isi):
    warna.print_pass("""
    _______________________________________________
    * VERTICAL
    """)
    # method 2
    ##
    # just invert the first method
    # to get vertical flow assign
    # ##
    resultArray(cols, rows, stat=2)  # vertical resultArray(j,i)


def assignFlowObtNyamuk():
    isi = 0
    isiForOtherLoop = 0
    for i in range(rows):
        for j in range(cols):
            # obat nyamuk
            isi += 1
            isiForOtherLoop = isi
            if i == 0:
                print(i, j)
                arr[i][j] = isi
            if j == rows:
                # if i == 1:
                #     print(i, j)
                # if i == 2:
                #     print(i, j)
                # if i == 3:
                #     print(i, j)
                if i != 0 and i != rows - 1:
                    print(i, j)
                    arr[i][j] = isi

    # horzIsi = isi
    # isi = 0
    for i in range(rows):
        for j in reversed(range(cols)):
            isi += 1
            # isiForOtherLoop - isi
            # isiForOtherLoop += 1
            # j = [j]
            # j.reverse()
            # j.__reversed__
            if i == rows - 1:
                print(i, j)
                arr[i][j] = isi
                # arr[i][j] = isiForOtherLoop
                # downToLeft = [j]
                # downToLeft.sort(reverse=True)
                # print(downToLeft)
                # print(sorted(list([j]), reverse=True))
    # isi = 0
    for i in reversed(range(rows)):
        for j in range(cols):
            isi += 1
            if j == 0:
                if i != rows-1 and i != 0:
                    print(i, 0)
                    arr[i][0] = isi

    for i in range(rows):
        for j in range(cols):
            isi += 1
            if (i != rows - 1 and i != 0 and i != 1) and (j != 0 and j != cols - 1):
                if i != rows - 2:
                    print(i, j)
                    arr[i][j] = isi
                # if i != rows - 3:
                #     print(i, j)

    for i in range(rows):
        for j in reversed(range(cols)):
            isi += 1
            if (i != rows - 1 and i != 0 and i != 1) and (j != 0 and j != cols - 1):
                if i != rows - 3:
                    print(i, j)
                    arr[i][j] = isi
                # end of flow obat nyamuk

    # show the array
    for row in arr:
        print("""
        """, row)


def arrMethod3(isi):
    warna.print_pass("""
    _______________________________________________
    * OBAT NYAMUK
    """)

    assignFlowObtNyamuk()


def myMenuProg():
    warna.print_warn('.\t\t\t_________________________________')
    warna.print_fail('. \t\t\t 1. Method1(horizontal flow assign)')
    warna.print_fail('. \t\t\t 2. Method2(vertical flow assign)')
    warna.print_fail('. \t\t\t 3. Method3(obat nyamuk flow assign)')
    warna.print_warn('.\t\t\t_________________________________')
    warna.print_fail('. \t\t\t [N] or !num in menu for exit')


def myHeaderProg():
    warna.print_pass("====================================")
    warna.print_info("""

Name   : Yogi Arif Widodo
Class  : TI(VA)
default: rows is (5) and cols is (6)

        """)
    warna.print_pass("====================================")


def mySpiralAssign():
    initA = 0
    initB = 0
    isi = 0
    endValue = 0
    bottomValue = 0
    startValue = 0

    twoThree = 0  # 2 and 4 rows
    threeStart = 0  # 3 .. reversed 5..0
    midleStart = 0

    customSize = 0

    # while ( 0 < 5 * 6)
    while (isi < rows * cols):
        for i in range(rows):
            for j in range(cols):
                isi += 1
                if i == 0:  # TOP
                    print(i, j)
                    arr[i][j] = isi + customSize
                if i != 0 and i != rows and j == 5:  # END - RIGHT INIT
                    # print(i, j)
                    # arr[i][j] = isi
                    endValue = isi
                    # print("")

        for i in range(cols):
            for j in reversed(range(rows)):
                endValue -= 1
                # sorted([endValue], reverse=True)
                # wrong testFlow i,j and j,i
                if i == rows:  # END - RIGHT ASSIGN
                    print(i, j)
                    arr[j][i] = endValue + cols + customSize
                    # print("")

        for i in range(rows):
            for j in reversed(range(cols)):
                # print("asd", i, j)
                bottomValue += 1
                if i == rows - 1:  # BOTTOM
                    print(i, j)
                    arr[i][j] = (bottomValue - rows - rows - rows) + customSize
                    startValue = (bottomValue - rows -
                                  rows - rows - 1)
                    # print("")

        for i in reversed(range(rows)):
            startValue += 1
            for j in range(cols):
                # # START - LEFT
                if j == 0 and i != rows and i != 0:
                    print(i, 0)
                    arr[i][0] = startValue + customSize
                    # print("")

        for i in range(rows):
            for j in range(cols):
                isi += 1
                if i == 1 and j != 0 and j != rows:
                    print(i, j)
                    arr[i][j] = isi + 1 - rows - rows - rows - rows
                    twoThree = isi

        for i in range(rows):
            for j in range(cols):
                if i == 2 and j == 4 or i == 3 and j == 4:
                    print(i, j)
                    twoThree += 1
                    arr[i][j] = twoThree + 1 - rows - rows - rows - rows
                    threeStart = twoThree

        # rangeJ = [3..1]
        for i in range(rows):
            for j in reversed(range(cols)):
                if i == 3 and j == 3 or i == 3 and j == 2 or i == 3 and j == 1:
                    print(i, j)
                    threeStart += 1
                    arr[i][j] = threeStart + 1 - rows - rows - rows - rows
                    midleStart = threeStart

        for i in range(rows):
            for j in range(cols):
                if i == 2 and j != 0 and j != rows and j != rows - 1:
                    print(i, j)
                    midleStart += 1
                    arr[i][j] = midleStart + 1 - rows - \
                        rows - rows - rows

    for row in arr:
        print("""
        """, row)


def start():
    myHeaderProg()
    myMenuProg()

    # horizontal & vertical
    # flowAssignTest()
    # spiral
    # mySpiralAssign()

    ioMenu = input('.\n. \t\t\t [*].Choose Num : ')
    if ioMenu == '1':
        arrMethod1(0)
    elif ioMenu == '2':
        arrMethod2(0)
    elif ioMenu == 3:
        # arrMethod3(0)
        mySpiralAssign()
    else:
        warna.print_bold('exit program')


if __name__ == '__main__':
    try:
        start()
    except KeyboardInterrupt as err:
        print(
            "\n[!] By ...: thanks for use my code (c) 2019 github.com/yogithesymbian")
        sys.exit(0)
