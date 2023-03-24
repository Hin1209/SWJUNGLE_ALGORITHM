import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())

    apply = [list(map(int, input().split())) for _ in range(n)]
    apply.sort()
    cnt = 1
    min_score = apply[0][1]
    for i in range(1,n):
        if min_score > apply[i][1]:
            min_score = apply[i][1]
            cnt += 1
    print(cnt)