n, x = list(map(int, input().split()))
lis = list(map(int, input().split()))
for i in range(len(lis)):
    if lis[i] < x:
        print(lis[i])