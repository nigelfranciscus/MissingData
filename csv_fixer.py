import csv
from itertools import islice

current_year = 2018

# iterate for 12 months
for month in range(0, 12):
    month = month + 1
    path = "D:/AIRtravel/New Monthly/Latest/griffith_n_"+str(current_year)+"m0" + str(month) + ".csv"
    out = "D:/AIRtravel/New Monthly/Latest/PyProcessed/griffith_nn_"+str(current_year)+"m0" + str(month) + ".csv"
    print(path)
    filereader = csv.reader(
        open(path, mode='r+', encoding="utf-8"), delimiter=',')
    newline = []
    next(filereader)
    for line in filereader:
        # New Amadeus Format (Why do they change?)
        if len(line[2]) == 0:
            line[1] = ''
        if line[2] == line[3]:
            line[2] = ''

        line.insert(0, current_year)
        line.insert(1, month)
        line.insert(6, '')
        line.insert(7, '')
        line.insert(8, '')
        line.pop()
        line.pop()

        newline.append(line)

    with open(out, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for writeline in newline:
            writer.writerow(writeline)
