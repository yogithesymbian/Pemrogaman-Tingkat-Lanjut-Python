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