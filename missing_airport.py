import csv
from math import cos, asin, sqrt


# calculate distance between two location
def distance(lat1, lon1, lat2, lon2):
    p = 0.017453292519943295  # Pi/180
    a = 0.5 - cos((lat2 - lat1) * p) / 2 + cos(lat1 * p) * cos(lat2 * p) * (1 - cos((lon2 - lon1) * p)) / 2
    return 12742 * asin(sqrt(a))


airport_data = open("C:/Users/s2876731.STAFF/Desktop/NewCO2/airports_preprocess.csv", mode='r+', encoding="utf-8")
airport_reader = csv.reader(airport_data, delimiter=',')
airport_dict = {each[4]: each[2:4] for each in airport_reader}

missingfile = open('C:/Users/s2876731.STAFF/Desktop/NewCO2/missing.csv', mode='r+')
missing_reader = csv.reader(missingfile, delimiter=',')
missing_strip = [row for row in missing_reader]

lat_long = {}
for each in missing_strip:
    for key, value in airport_dict.items():
        if each[0] == key:
            first = value
        if each[1] == key:
            second = value
            lat_long[each[0], each[1]] = first, second

with open('C:/Users/s2876731.STAFF/Desktop/NewCO2/dict.csv', 'w') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    for key, value in lat_long.items():
        origin_latitude = float(value[0][0])
        origin_longitude = float(value[0][1])
        destination_latitude = float(value[1][0])
        destination_longitude = float(value[1][1])
        calculation = distance(origin_latitude, origin_longitude, destination_latitude, destination_longitude)
        writer.writerow([key, value, calculation])

airport_data.close()
missingfile.close()
