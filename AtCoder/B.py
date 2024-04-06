import math

N = int(input())

x = []
y = []

for i in range(N):
    xtemp, ytemp = list(map(int,input().split()))
    x.append(xtemp)
    y.append(ytemp)

for i in range(N):
    max_num = N+1
    max_distance = 0
    x1 = x[i]
    y1 = y[i]
    for j in range(N-1, -1, -1):
        x2 = x[j]
        y2 = y[j]
        temp_distance = math.sqrt((x1-x2)**2+(y1-y2)**2)
        if temp_distance >= max_distance:
            max_distance = temp_distance
            max_num = j+1
    print(max_num)



