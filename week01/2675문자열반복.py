t = int(input())
for i in range(t):
    x, y = input().split()
    r, s = int(x), y
    result = ''
    for i in range(len(s)):
        result += s[i] * r
    print(result)