import csv
from math import cos, asin, sqrt


def distance(lat1, lon1, lat2, lon2):
    p = 0.017453292519943295  # Pi/180
    a = 0.5 - cos((lat2 - lat1) * p) / 2 + cos(lat1 * p) * cos(lat2 * p) * (1 - cos((lon2 - lon1) * p)) / 2
    return 12742 * asin(sqrt(a))


airport_data = open("C:/Users/s2876731.STAFF/Desktop/airports_preprocess.csv", mode='r+', encoding="utf-8")
airport_reader = csv.reader(airport_data, delimiter=',')
airport_dict = {each[4]: each[2:4] for each in airport_reader}
#print(airport_dict.keys())


missingfile = open('C:/Users/s2876731.STAFF/Desktop/NewCO2/missing.csv', mode='r+')
missing_reader = csv.reader(missingfile, delimiter=',')
missing_strip = [row for row in missing_reader]
# print(missing_strip)

# key = [key for key in airport_dict.keys()]
# for each_missing in missing_reader:
#     if each_missing[1] == key:
#         print(each_missing[1])
#         origin_latitude = airport_dict.values()
#         print(origin_latitude)

lat_long = {}

for each in missing_strip:
    for key, value in airport_dict.items():
        if each[0] == key:
            a = value
        if each[1] == key:
            b = value
            lat_long[each[0], each[1]] = a, b


# print(lat_long)
for key, value in lat_long.items():
    print(key, value)


# with open('C:/Users/s2876731.STAFF/Desktop/NewCO2/dict.csv', 'w') as csv_file:
#     writer = csv.writer(csv_file)
#     for key, value in lat_long.items():
#         writer.writerow([key, value])


airport_data.close()
missingfile.close()
