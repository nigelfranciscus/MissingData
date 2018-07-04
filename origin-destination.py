import csv
import json

read_airport = csv.reader(open('C:/Users/s2876731.STAFF/Desktop/Flights/akl_viz.csv', mode='r+'),
                          delimiter=',')
location = [row[4:] for row in read_airport]

final = []
for each_location in location:

    # 1 = Green, 2 = Blue, 3 = Yellow
    # A-D pair
    if len(each_location[1]) == 0 and len(each_location[2]) == 0:
        final.append(("{ latitude: " + each_location[0] + "}", "{latitude :" + each_location[3] + "}", 1))

    # A-B pair
    if len(each_location[1]) > 0:
        final.append(("{ latitude: " + each_location[0] + "}", "{latitude :" + each_location[1] + "}", 1))

    # B-C and C-D pair
    if len(each_location[2]) > 0:
        final.append(("{ latitude: " + each_location[1] + "}", "{latitude :" + each_location[2] + "}", 3))  # B-C
        final.append(("{ latitude: " + each_location[2] + "}", "{latitude :" + each_location[3] + "}", 2))  # C-D

    # B-D pair
    if len(each_location[2]) == 0:
        final.append(("{ latitude: " + each_location[1] + "}", "{latitude :" + each_location[3] + "}", 3))

# for key in final:
#     key_splitter1 = key[0].split(" ")
#     key_splitter2 = key[1].split(",")

# TODO Need to remove headers (missing longitude-latitude causing the splitter [1] to be missing
# TODO Need to fix the read_airport result by adding long_lat1 - long_lat4 and remove the bracket and ""


with open('C:/Users/s2876731.STAFF/Desktop/Flights/akl_origin_dest_comp.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    for key in final:
        # print(key[1])
        key_splitter1 = key[0].split(",")
        key_splitter2 = key[1].split(",")
        if len(key_splitter1) > 1 and len(key_splitter2) > 1:
            writer.writerow(
                (key_splitter1[0], "longitude: " + key_splitter1[1], key_splitter2[0], "longitude: " + key_splitter2[1], key[2]))
