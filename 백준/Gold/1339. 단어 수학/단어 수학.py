from collections import Counter

N= int(input())

alphabet = []

arr = []
set_number = {}

for _ in range(N):
    k = input()
    alphabet.append(k)
    for i,j in enumerate(k):
        if j not in set_number:
            set_number[j]=10**(len(k)-i)
        else:
            set_number[j] = set_number[j] + 10**(len(k)-i)

most = {}
result = 0
mm = 9
for i,j in Counter(set_number).most_common():
    most[i]=mm
    mm-=1

for i in alphabet:
    r=0
    for char in i:
        if char in most:
            r = r * 10 + most[char]
    result+=r
print(int(result))

