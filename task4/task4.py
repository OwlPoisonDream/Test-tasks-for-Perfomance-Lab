import os
nums = open(input("Введите путь до файла с целыми числами "), 'r')
count = 0
num = []
for line in nums:
    num.append([int(x) for x in line.split()])
min = int(num[0].pop(0))
max = int(num[-1].pop(0))
num[0].append(min)
num[-1].append(max)
av=0
for i in range(0,len(num)):
    num[i]=int(num[i].pop(0))
    if min > num[i]:
        min = num[i]
    if max < num[i]:
        max = num[i]
    av +=num[i]
av= av // len(num)
for i in range(0,len(num)):
    while 1:
        if num[i]==av:
            break
        elif num[i]>av:
            num[i]-=1
            count+=1
            print(num[i])
        elif num[i]<av:
            num[i]+=1
            count+=1
            print(num[i])
print(count)
    
