N = int(input())
arr = list(map(int, input().split()))

sum = 0
for i in range(N - 1):
    if arr[i]>0:
        sum += 1

print(sum)
