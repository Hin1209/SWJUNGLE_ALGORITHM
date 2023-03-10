import sys

input = sys.stdin.readline

ps = input().rstrip()
ps_list = []

for i in ps:
    ps_list.append(i)

def calculate_ps(ps_list):
    stack = []
    res = 0
    for i in range(len(ps_list)):
        if ps_list[i] == '(':
            stack.append('(')
        elif ps_list[i] == '[':
            stack.append('[')
        elif ps_list[i] == ')':
            if len(stack) == 0:
                return 0
            score = 0
            while len(stack) > 0 and stack[-1] != '(':
                if stack[-1] == '[': return 0
                score += stack[-1]
                stack.pop()
            if len(stack) > 0:
                if score:
                    stack.pop()
                    stack.append(2 * score)
                else:
                    stack.pop()
                    stack.append(2)
            else:
                return 0
        elif ps_list[i] == ']':
            if len(stack) == 0:
                return 0
            score = 0
            while len(stack) > 0 and stack[-1] != '[':
                if stack[-1] == '(': return 0
                score += stack[-1]
                stack.pop()
            if len(stack) > 0:
                if score:
                    stack.pop()
                    stack.append(3 * score)
                else:
                    stack.pop()
                    stack.append(3)
            else:
                return 0
    while stack:
        tmp = stack.pop()
        if tmp == '[' or tmp == ']' or tmp == '(' or tmp == ')':
            return 0
        else:
            res += tmp
    return res

print(calculate_ps(ps_list))