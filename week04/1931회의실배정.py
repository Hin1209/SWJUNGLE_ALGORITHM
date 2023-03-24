import sys
input = sys.stdin.readline

n = int(input())

office = [list(map(int, input().split())) for _ in range(n)]

office.sort()

cnt = 1
end_time = office[0][1]

for i in range(1, n):
    if end_time <= office[i][0]:
        cnt += 1
        end_time = office[i][1]
    elif office[i][1] < end_time:
        end_time = office[i][1]

print(cnt)