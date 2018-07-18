import csv
from itertools import islice

# iterate for 12 months
for month in range(0, 12):
    month = month + 1
    path = "D:/AIRtravel/New Monthly/New 2017/griffith_n_2017m0" + str(month) + ".csv"
    out = "D:/AIRtravel/New Monthly/New 2017/griffith_nn_2017m0" + str(month) + ".csv"
    print(path)
    filereader = csv.reader(
        open(path, mode='r+', encoding="utf-8"), delimiter=',')
    newline = []
    next(filereader)
    for line in filereader:
        # New Amadeus Format (Why do they change?)
        if line[2] == line[3]:
            line[2] = ''
        if len(line[2]) == 0:
            line[1] = ''

        line.insert(0, 2017)
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
