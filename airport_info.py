from __future__ import division
import csv
from math import cos, asin, sqrt


# calculate distance between two location
def distance(lat1, lon1, lat2, lon2):
    p = 0.017453292519943295  # Pi/180
    a = 0.5 - cos((lat2 - lat1) * p) / 2 + cos(lat1 * p) * cos(lat2 * p) * (1 - cos((lon2 - lon1) * p)) / 2
    return 12742 * asin(sqrt(a))


# Read the airport location data
airport_reader = csv.reader(
    open("C:/Users/s2876731.STAFF/Desktop/NewCO2/airports_preprocess.csv", mode='r+', encoding="utf-8"), delimiter=',')
# Build key-value for IATA code and lat-long pair
airport_dict = {each[4]: each[2:4] for each in airport_reader}

# read the brisbane airport information
# read_brisbane = csv.reader(open('C:/Users/s2876731.STAFF/Desktop/Flights/FlightData_AKL_2017-01.csv', mode='r+'),
#                            delimiter=',')
# brisbane_location = [row[2:6] for row in read_brisbane]
# print(brisbane_location)

# lat_long = {}
# for each_location in brisbane_location:
#     first = airport_dict.get(each_location[0])
#     second = airport_dict.get(each_location[1])
#     third = airport_dict.get(each_location[2])
#     fourth = airport_dict.get(each_location[3])
#
#     lat_long[each_location[0], each_location[1], each_location[2], each_location[3]] = first, second, third, fourth
#
# # for key, value in lat_long.items():
# #     for each_value in value:
# #         if each_value is not None:
# #             print(each_value)
#
#
# with open('C:/Users/s2876731.STAFF/Desktop/Flights/akl_viz.csv', 'w', newline='') as csv_file:
#     writer = csv.writer(csv_file, delimiter=',')
#     for key, value in lat_long.items():
#         writer.writerow([key[0], key[1], key[2], key[3], value[0], value[1], value[2], value[3]])

read_top400 = csv.reader(open('Top400carbonroutes.csv', mode='r+'), delimiter=',')
next(read_top400)

lat_long = {}
lower = 0.5
upper = 5
minimum = 6.976
maximum = 39.704
for each_data in read_top400:
    first = airport_dict.get(each_data[0])
    second = airport_dict.get(each_data[1])
    ton = float(each_data[3])/1000000
    # normalization
    lineThickness = lower + (ton - minimum)*(upper-lower)/(maximum-minimum)

    lat_long[each_data[0], each_data[1], round(lineThickness, 3)] = first, second

for key, value in lat_long.items():
    print("{" + "origin:{ latitude: " + value[0][0] + ", longitude: " + value[0][1] + "}, destination: { latitude: " +
           value[1][0] + ", longitude: " + value[1][1] + "}, strokeWidth: " + str(key[2]) +
           " strokeColor: 'red', arcSharpness: 0.1 },")



# with open('C:/Users/s2876731.STAFF/Desktop/Flights/akl_viz.csv', 'w', newline='') as csv_file:
#     writer = csv.writer(csv_file, delimiter=',')
#     for key, value in lat_long.items():
#         writer.writerow([key[0], key[1], key[2], key[3], value[0], value[1], value[2], value[3]])
