# Recursive function to return gcd of a and b
def gcd(a,b):

    print("nilai a dan b ", a, b)
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a

# Driver program to test above function
a = 98
b = 56

if(gcd(a, b)):
    print('GCD of', a, 'and', b, 'is', gcd(a, b))
else:
    print('not found')

# This code is contributed by Danish Raza