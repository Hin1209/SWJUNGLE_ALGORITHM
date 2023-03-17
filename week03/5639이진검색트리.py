import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

tree = {}

preorder = []
while True:
    try:
        n = int(input())
        preorder.append(n)
    except: 
        break
    
def find_tree(start, end):
    if start > end:
        return
    
    div = end + 1
    
    for i in range(start+1, end+1):
        if preorder[start] < preorder[i]:
            div = i
            break
        
    find_tree(start+1, div-1)
    find_tree(div, end)
    print(preorder[start])
    
find_tree(0, len(preorder) - 1)