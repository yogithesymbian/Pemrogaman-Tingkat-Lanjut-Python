import csv

def readTextFile(filename):
    text = ""
    f = open(filename, 'r')
    for line in f:
        text += line

    f.close()
    return text

def writeTextFile(filename, text):
    f = open(filename, 'w')
    for item in text:
        f.write(item)
    f.close()

def writeCSVFile(filename, llist):
    with open(filename, 'w', newline="") as ofile:
        writer = csv.writer(ofile, delimiter=",")
        for newdata in llist:
            writer.writerow(newdata)

# fungsi menghitung mse
def hitungMAE(teks1, teks2):
    #bandingkan ukuran kedua file
    if len(teks1) == len(teks2):
        print("[MAE] Kedua file memiliki ukuran yang sama")

        #hitung nilai mse
        jmlchar = len(teks1)
        jmlabs = 0

        #hitung jumlah absolute
        for i in range(jmlchar):
            # print(teks1[i], teks2[i], ord(teks1[i]), ord(teks2[i]))
            jmlabs = jmlabs + abs(ord(teks1[i]) - ord(teks2[i]))
            # print("tes : ", jmlkuadrat)

        mae = jmlabs / jmlchar

        return mae
    else:
        return -1

# fungsi menghitung MSE
def hitungMSE(teks1, teks2):
    #bandingkan ukuran kedua file
    if len(teks1) == len(teks2):
        print("[MSE] Kedua file memiliki ukuran yang sama")

        #hitung nilai mse
        jmlchar = len(teks1)
        jmlkuadrat = 0

        #hitung jumlah absolute
        for i in range(jmlchar):
            # print(teks1[i], teks2[i], ord(teks1[i]), ord(teks2[i]))
            jmlkuadrat = jmlkuadrat + abs(ord(teks1[i]) - ord(teks2[i]))**2
            # print("tes : ", jmlkuadrat)

        mse = jmlkuadrat / jmlchar

        return mse
    else:
        return -1
