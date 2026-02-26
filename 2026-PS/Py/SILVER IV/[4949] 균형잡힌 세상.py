# https://www.acmicpc.net/problem/4949
# 260226 풀이
# 알고리즘: 스택
# 시간: 224ms

while True:
    question = input()
    if question == '.': break
    if not question.endswith('.'): # 문자열이 온점으로 끝나야 한다는 조건
        print("no")
        continue
    
    stack = []  
    for ch in question:
        if ch == '(' or ch == '[': stack.append(ch)
        elif ch == ')':
            if not stack or stack[-1] != '(':
                print("no")
                break
            else: stack.pop()
        elif ch == ']':
            if  not stack or stack[-1] != '[': 
                print("no")
                break
            else: stack.pop()
    else:
        if stack: print("no")
        else: print("yes")

# 깨달은 점
# 1. 애초에 문제 조건을 잘 체크하자 (빠뜨리는 것 없이)
# 2. 조건문 작성할 때 예외 조건을 항상 먼저 체크하자