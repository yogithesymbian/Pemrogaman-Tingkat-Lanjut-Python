teks = "saya belum mandi kemarin sore"
print("normal", teks)
print("one slicing : ", teks[:]) # seluruh
print("first slice 7 : ", teks[7:])
print("last slice 7 : ",teks[:7])
print("first slice 7 and last 15 : ", teks[7:15])
print("first slice -1 :",teks[-1])
print("first slice -2 : ",teks[-2])
print("double last slice -1 : ",teks[::-1])

print(teks.count("a"))
print(teks.split())
print(teks.split(sep="a"))
print(teks.upper())
print(reversed([teks]))