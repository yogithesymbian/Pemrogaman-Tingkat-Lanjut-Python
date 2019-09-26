__name__ = 'adek'
import mylib as my
import mylibcsv as mycsv

maks = 10

ltabel = [['a', 'b', 'a x b', 'a + b', 'a - b']]

for a in range(1, maks+1):
    for b in range(1, maks+1):
        dlist = [a, b, my.kali(a, b), my.tambah(a, b), my.kurang(a, b)]
        # print(dlist)
        ltabel.append(dlist)


namafile = 'contoh.csv'
mycsv.writeSVFile(namafile, ltabel)
print("sudah tersimpan")

print("")