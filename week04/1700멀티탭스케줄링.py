import sys
input = sys.stdin.readline

n, k = map(int, input().split())

e = list(map(int, input().split()))

cnt = 0
table = [[] for _ in range(k+1)]
for i in range(k):
    table[e[i]].append(i)
        
plug = {}
size = n
for i in range(k):
    if size > 0 and not e[i] in plug:
        plug[e[i]] = i
        size -= 1
    elif size >= 0 and e[i] in plug:
        plug[e[i]] = i
    elif size == 0 and e[i] not in plug:
        remove = [0, 0]
        for key in plug.keys():
            exist = False
            for idx in table[key]:
                if idx > plug[key]:
                    exist = True
                    if idx > remove[0]:
                        remove[0] = idx
                        remove[1] = key
                    break
            if not exist:
                remove = [plug[key], key]
                break
        plug.pop(remove[1])
        plug[e[i]] = i
        cnt += 1
print(cnt)
        