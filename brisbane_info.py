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
airport_dict = {each[4]: each[2:4] for each in airport_reader}

# read the brisbane airport information
read_brisbane = csv.reader(open('C:/Users/s2876731.STAFF/Desktop/NewCO2/FlightData_BNE_2017-01.csv', mode='r+'),
                           delimiter=',')
brisbane_location = [row[2:6] for row in read_brisbane]

lat_long = {}
for each_location in brisbane_location:
    first = airport_dict.get(each_location[0])
    second = airport_dict.get(each_location[1])
    third = airport_dict.get(each_location[2])
    fourth = airport_dict.get(each_location[3])

    lat_long[each_location[0], each_location[1], each_location[2], each_location[3]] = first, second, third, fourth

# for key, value in lat_long.items():
#     for each_value in value:
#         if each_value is not None:
#             print(each_value)


with open('C:/Users/s2876731.STAFF/Desktop/NewCO2/bne_viz.csv', 'w') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    for key, value in lat_long.items():
        writer.writerow([key[0], key[1], key[2], key[3], value[0], value[1], value[2], value[3]])

