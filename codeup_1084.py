#코드업_기본100제_1084
import sys

r,g,b = map(int,sys.stdin.readline().split())
sum = 0
for i in range(r):
    for j in range(g):
        for k in range(b):
            print(i,j,k)
            sum += 1
print(sum)