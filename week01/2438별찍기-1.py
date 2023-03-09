n = int(input())
for i in range(1, n + 1):
    for j in range(i):
        if j < i - 1:
            print("*", end = '')
        else:
            print("*")