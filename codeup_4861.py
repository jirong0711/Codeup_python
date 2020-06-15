import math
N,K = map(int,input().split())
arr = [[0 for col in range(6)] for row in range(2)]
count = 0
for i in range(N):
    S,Y = map(int,input().split())
    arr[S][Y-1] += 1

for i in range(6):
    for j in range(2):
        count += math.ceil(arr[j][i]/K)
print(count)