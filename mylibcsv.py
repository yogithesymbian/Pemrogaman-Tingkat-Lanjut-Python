import csv

# write csv file
def writeSVFile(filename, llist):
    with open(filename, "w", newline="") as ofile:
        writer = csv.writer(ofile, delimiter=',')
        for newdata in llist:
            writer.writerow(newdata)
    ofile.close
