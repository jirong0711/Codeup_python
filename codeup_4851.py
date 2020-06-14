def cal_game(a, b, R):
    if a == b and a <= R:
        return 1
    elif a == b and a > R:
        return 0
    elif a > b:
        remain = a - b
        if remain <= R - a + 2:
            return 1
        else:
            return 0
    else:
        remain = b - a
        if remain <= R - b + 1:
            return 1
        else:
            return 0


R = int(input())
C = int(input())
arr = []
for i in range(C):
    a, b = map(int, input().split())
    arr.append(cal_game(a, b, R) )

for j in range(C):
    print(arr[j])
