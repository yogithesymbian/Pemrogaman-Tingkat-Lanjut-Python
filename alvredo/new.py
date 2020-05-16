import struct

def getBin(x):
    return x >= 0 and str(bin(x))[2:]


# dec = -1.1242302
dec = "1011111111110001111111001101100011001110011000101100111100000010"

def floatToBinary64(value):
    val = struct.unpack('Q', struct.pack('d', value))[0]
    return getBin(val)


def binaryToFloat(value):
    return struct.unpack("d", struct.pack("Q", int(value, 2)))[0]


binToFloat = binaryToFloat(dec)         # dec is binary with str format
                                        # should refactor the variabel
print("""
    Binary equivalent of {}
    is {}"""
        .format(dec, binToFloat))

# float to binary
# floatToBin = floatToBinary64(dec)
# floatToBin = str(floatToBin).zfill(64)

# print("""
#     Binary equivalent of {} : {}
#     Binary Size : {}"""
#         .format(dec, floatToBin, len(floatToBin)))