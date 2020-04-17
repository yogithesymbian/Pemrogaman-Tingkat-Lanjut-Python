import datetime

start = datetime.datetime.now()

# Recursive function to return gcd of a and b
def gcd(a,b):

    # print("nilai a : {} dan nilai b : {}".format(a,b))
    # Everything divides 0
    if (b == 0):
         return a
    return gcd(b, a%b)

# Driver program to test above function
a = 98
b = 56
if(gcd(a, b)):
    print('GCD of', a, 'and', b, 'is', gcd(a, b))
else:
    print('not found')

finish = datetime.datetime.now()
print("start : {} \n finish : {} \n hasil : {}".format(start,finish, finish-start))
# This code is contributed by Danish Raza