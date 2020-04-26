import struct

a = b'\x3f\xd5\x55\x55\x55\x55\x55\x55'
n = struct.unpack(b'>d', a)
print(format(n[0], '.18f'))