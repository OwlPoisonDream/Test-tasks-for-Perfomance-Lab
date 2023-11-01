import math
circle = open(input("Введите путь до файла с параметрами окружности"),'r')
point = open(input("Введите путь до файла с параметрами точек"), 'r')
cir = []
points = []
existence = "Не лежит"
for line in circle:
    cir.append([float(x) for x in line.split()])
for line in point:
    points.append([float(x) for x in line.split()])
radius = float(str(cir[1]).replace('[', '').replace(']',''))
coordinates = cir[0]
a = float(coordinates[0])
b = float(coordinates[1])
for i in range(0,len(points)):
    point=points[i]
    x=float(point[0])
    y=float(point[1])
    answer = float(math.sqrt(((x-a)**2)+((y-b)**2)))
    if answer==radius:
        existence = "0	- точка лежит на окружности"
    if answer<radius:
        existence = "1	- точка внутри "
    if answer>radius:
        existence = "2	- точка снаружи "
    i+=1
    print(existence)
