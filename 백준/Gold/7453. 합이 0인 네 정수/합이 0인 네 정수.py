size = int(input())
A = []
B = []
C = []
D = []
for _ in range(size):
    a, b, c, d = list(map(int, input().split()))
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

hashmap = dict()
target = 0
cnt = 0
for a in A :
    for b in B :
        if (a+b) not in hashmap :
            hashmap[a+b] = 1
        else :
            hashmap[a+b] += 1

for c in C :
    for d in D :
        cd = c+d
        if (target - cd) in hashmap :
            cnt += hashmap[target-cd]

print(cnt)


