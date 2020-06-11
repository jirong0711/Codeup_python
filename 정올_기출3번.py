//메모리 초과일 경우 sys.stdin.readline()으로 읽어주기
//unique한 set다룰 경우에는 list가 아닌 set으로 지정해주면 훨씬 빠른 계산

import sys
d1,d2=map(int,sys.stdin.readline().split())
s=set()
for i in range(d1,d2+1):
    for j in range(i):
        s.add(j/i)
print(len(s))