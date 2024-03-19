# 9012

PS = [] # 괄호 문자열 배열
N = int(input())    # 괄호 문자열의 개수
for i in range(N):  # 문자열 입력 받기
    PS.append(input())
match_dic = {
    ')': '('
}

answers = []    # 답변 리스트 
for i in range(N):
    stack = []
    for j in PS[i]:
        if j not in match_dic.keys():  # (가 들어오면 stack에 추가
            stack.append(j)
        else: # )가 들어오면 짝이 맞는 (를 stack에서 제거
            if not stack:   # 비어 있는 스택에 ) 하나만 추가
                stack.append(j)
                break
            stack.pop()
    if stack:   # 스택이 채워져 있으면 -> 짝이 안 맞았다는 뜻
        answers.append("NO")
    else:       # 스택이 비워져 있으면 -> 다 짝 맞춰서 나갔다는 뜻
        answers.append("YES")

# print
for i in answers:
    print(i)
