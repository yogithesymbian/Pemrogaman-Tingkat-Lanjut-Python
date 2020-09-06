import datetime

start = datetime.datetime.now()
# a = 98
# b = 56
a = 131
b = 3220

while a != b:
        if a > b:
            a -= b
        elif a < b:
            b -= a

print("gcd nya ", a)
finish = datetime.datetime.now()
print("start : {} \n finish : {} \n hasil : {}".format(start,finish, finish-start))