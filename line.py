coordinates = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7)]

x1 = coordinates[0][0]
x2 = coordinates[1][0]
y1 = coordinates[0][1]
y2 = coordinates[1][1]
xlist = []

if x1 == x2:
    for i in range(2, len(coordinates)):
        if coordinates[i][0] == x1:
            xlist.append(coordinates[i])
elif y1 == y2:
    for i in range(2, len(coordinates)):
        if coordinates[i][1] == y1:
            xlist.append(coordinates[i])
else:
    for i in range(2, len(coordinates)):
        if (coordinates[i][0]-x1)/(x2-x1) == (coordinates[i][1]-y1)/(y2-y1):
            xlist.append(coordinates[i])

if len(xlist) == len(coordinates)-2:
    print(True)
else:
    print(False)


