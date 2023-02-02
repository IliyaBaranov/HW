import csv
country = []
corruption = []
with open('2019.csv', 'r', encoding='utf8') as csv_file:
    csv_top = csv.reader(csv_file)
    next(csv_top)
    for line in csv_top:
        country.append(line[1])
        corruption.append(line[5])
    for i in range(1, 6):
        x = (corruption.index(max(corruption)))
        print(country[x], max(corruption))
        country.pop(x)
        corruption.pop(x)