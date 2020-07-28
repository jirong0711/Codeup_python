//참조 https://home-body.tistory.com/128
n = int(input())
max = 0
max_list = []
for i in range(n+1):
    anw = [n,i]
    j = 0

    while(True):
        a = anw[j] - anw[j+1]
        if a < 0:
            break
        anw.append(a)
        if max < len(anw):
            max = len(anw)
            max_list = result[:]

        j += 1
print(max)
for i in max_list:
    print(i, end=" ")
print()