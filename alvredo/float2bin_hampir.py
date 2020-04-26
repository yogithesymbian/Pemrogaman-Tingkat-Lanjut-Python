# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 22:21:48 2020

@author: Lenovo
"""

import struct

# getBin = lambda x: x > 0 and str(bin(x))[2:] or "-" + str(bin(x))[3:]

data = "0011111110010100011110101110000101000111101011100001010001111011"
print("{}\n binary : {}".format(len(data), data))

def getBin(x):
    return x >= 0 and str(bin(x))[2:]

dec = -0.02
def floatToBinary64(value):
    val = struct.unpack('Q', struct.pack('d', value))[0]
    print("initGetBin : {}".format(val, '.18f'))
    return getBin(val)

def binaryToFloat(value):
#    hx = hex(int(value, 2))
    return struct.unpack("d", struct.pack("Q", int(value, 2)))[0]

#def floatToBinary32(value):
#    val = struct.unpack('L', struct.pack('f', value))[0]
#    return getBin(val)
#
#def binaryToFloat32(value):
#    return struct.unpack("f", struct.pack("L", int(value, 2)))[0]

# floats are represented by IEEE 754 floating-point format which are
# 64 bits long (not 32 bits)

# float to binary
floatToBin = floatToBinary64(dec)
floatToBin = str(floatToBin).zfill(64)
print("""
    Binary equivalent of {} : {}
    Binary Size : {}"""
        .format(dec, floatToBin, len(floatToBin)))

if data == floatToBin:
    print('\n\tdata is true')

# binary to float <-- sebaiknya tidak perlu comment ini
binToFloat = binaryToFloat(floatToBin)      # jangan gunakan variable name l atau i kecuali kapital
        # variable tersebut sudah jelas binary to float jadi tidak perlu comment
print("""
    Decimal equivalent of {}
    is {}"""
        .format(floatToBin, binToFloat))


# float to binary
#floatToBin32 = floatToBinary32(-0.01)
#print('Binary equivalent of 0.01:')
#print(floatToBin32 + '\n')
#
## binary to float
#fl32 = binaryToFloat32(floatToBin32)
#print('Decimal equivalent of ' + floatToBin32)
#print(fl32)