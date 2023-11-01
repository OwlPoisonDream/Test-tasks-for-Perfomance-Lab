import array
n = int(input("Введите число, задающее максимальный элемент массива "))
m = int(input("Введите число, задающее длину массива "))
num_array = array.array("l", [])
i = 1
mi = 1
road = array.array("l", [1])
while 1:
    if mi == m and i==1:
        num_array.append(i)
        break
    elif mi!=m and i!=n:
        num_array.append(i)
        i+=1
        mi+=1
    elif mi!=m and i==1:
        num_array.append(i)
        i+=1
    elif mi!=m and i==n:
        num_array.append(i)
        i=1
        mi+=1
    elif mi==m and i!=n:
        num_array.append(i)
        mi=1
        road.append(i)
    elif mi==m and i==n:
        num_array.append(i)
        mi=1
        road.append(i)         
print(road)