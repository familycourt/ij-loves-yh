N = int(input())

callList = list(map(int, input().split()))


calYoung = 0
calMin = 0

#calculate calYoung
for i in range(N):
    tmp = callList[i] // 30 + 1
    calYoung = calYoung + tmp * 10

#calculate calMin
for i in range(N):
    tmp = callList[i] // 60 + 1
    calMin = calMin + tmp * 15

if calMin < calYoung:
    print("M " + str(calMin))
elif calMin > calYoung:
    print("Y " + str(calYoung))
else:
    print("Y M " + str(calMin))
