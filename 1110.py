import sys

N = int(sys.stdin.readline())
#N = int(input())
numTmp = N
if N < 10:
    num1 = 0
else:
    num1 = N//10

num2 = N%10
cnt = 0

while 1 :
    numCal = num1 + num2
    num1 = num2
    num2 = numCal%10
    cnt+=1
    numToCompare = num1*10 + num2
    if numTmp == numToCompare:
        break

print(cnt)
    
    