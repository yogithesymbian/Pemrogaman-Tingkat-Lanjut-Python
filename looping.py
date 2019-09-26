teks = "saya belum mandi kemarin sore"

for i in range(len(teks)):
    print(i, teks[i])

for i in teks:
    print(i, ord(i))

for i in range(0, len(teks), 5):
    print(i, teks[i])

for i in range(0, len(teks)-1, 0, -2):
    print(i, teks[i])