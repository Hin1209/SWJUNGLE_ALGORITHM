import sys

input = sys.stdin.readline

A = input().rstrip()
B = input().rstrip()
text = A + '1' + B
t = 1
n = len(text)

suffixes = []
group = [0] * n
group.append(-1)

for i in range(n):
    suffixes.append(i)
    group[i] = ord(text[i]) - ord('a')

while t < n:
    suffixes.sort(key=lambda x: (group[x], group[min(x+t, n)]))
    new_group = [0] * n
    new_group.append(-1)

    for i in range(1, n):
        if group[suffixes[i-1]] < group[suffixes[i]] or group[min(suffixes[i-1]+t, n)] != group[min(suffixes[i]+t, n)]:
            new_group[suffixes[i]] = new_group[suffixes[i-1]] + 1
        else:
            new_group[suffixes[i]] = new_group[suffixes[i-1]]

    group = new_group
    if new_group[n-1] == n-1:
        break
    t *= 2

pos = [0] * n
for i in range(n):
    pos[suffixes[i]] = i
lcp = [0] * n

k = 0
max_len = 0
for i in range(n):
    if pos[i]:
        j = suffixes[pos[i]-1]
        while i+k < n and j+k < n and text[i+k] == text[j+k]:
            k += 1
        lcp[pos[i]] = k
        if max_len < k:
            if i < len(A) and j > len(A) or i > len(A) and j < len(A):
                max_len = k
                str_pos = (j, j+k)
        if k:
            k -= 1

print(max_len)
print(text[str_pos[0]:str_pos[1]])
