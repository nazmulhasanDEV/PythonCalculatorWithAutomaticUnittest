import csv

with open('./Unit Test Addition.csv', 'r') as addiotion:
    csv_reader = csv.reader(addiotion)
    l = list(csv_reader)
    print(l)
    length = len(l)
    for x in range(1, length):
        if x != 2:
            print(l[x])
            for y in l[x]:
                print(y)
        else:
            break

