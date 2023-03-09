import sys
input = sys.stdin.readline

n, m = map(int, input().split())
card = list(map(int, input().split()))

near = int(1e9)
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            tmp_sum = card[i] + card[j] + card[k]
            if tmp_sum > m:
                continue
            if tmp_sum <= m:
                near = min(near, m - tmp_sum)
print(m - near)