__name__ = "list python"


llist = []
# other type data would inside in list
angka = 10
nama = "saya"
warna = "merah kuning hijau"
pecahan = "234.21"
dlist = [angka, nama, warna]

# list.append(angka)
llist.append(angka)
llist.append(nama)
llist.append(pecahan)
llist.append(dlist)

# print the list
for i in llist:
    # print(i)
    print(i, type(i))
print("""
\n
""")
# take the list
for i in range(len(llist)):
    print(llist.pop())
# llist.pop() # stack

llist[2:]
llist[1:-1]
llist[1:-3]
# llist[0]
llist[0][-1]