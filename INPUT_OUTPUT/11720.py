import sys

arraySize = sys.stdin.readline()

num = input()

total = 0

for i in map(int, str(num)):
    total += i
    
print(total)
    
     