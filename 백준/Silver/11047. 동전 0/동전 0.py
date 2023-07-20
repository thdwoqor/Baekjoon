N, K = map(int,input().split())

arr = []

for _ in range(N):
    arr.append(int(input()))

value = K
count = 0

for i in arr[::-1]:
    if value-i < 0:
        continue

    count+=value//i
    value=value%i

print(count)
