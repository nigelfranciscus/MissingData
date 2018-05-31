import csv
import json

read_brisbane = csv.reader(open('C:/Users/s2876731.STAFF/Desktop/NewCO2/bne_viz.csv', mode='r+'),
                           delimiter=',')
brisbane_location = [row[4:] for row in read_brisbane]


final = []
for each_location in brisbane_location:
    #print(each_location)

    if len(each_location[1]) == 0 and len(each_location[2]) == 0:
        final.append(("{ latitude: " + each_location[0] + "}", "{latitude :" + each_location[3] + "}", 1))

    if len(each_location[1]) > 0:
        final.append(("{ latitude: " + each_location[0] + "}", "{latitude :" + each_location[1] + "}", 1))

    if len(each_location[2]) > 0:
        final.append(("{ latitude: " + each_location[1] + "}", "{latitude :" + each_location[2] + "}", 2))
        final.append(("{ latitude: " + each_location[2] + "}", "{latitude :" + each_location[3] + "}", 3))

    if len(each_location[2]) == 0:
        final.append(("{ latitude: " + each_location[1] + "}", "{latitude :" + each_location[3] + "}", 3))

# for key in final:
#     key_splitter1 = key[0].split(" ")
#     key_splitter2 = key[1].split(",")
#     print(key[1].split(",")[1])

with open('C:/Users/s2876731.STAFF/Desktop/NewCO2/bne_origin_dest_comp.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    for key in final:
        key_splitter1 = key[0].split(",")
        key_splitter2 = key[1].split(",")
        writer.writerow((key[0], "longitude: "+key_splitter1[1], key[2], "longitude: "+key_splitter2[1]))


