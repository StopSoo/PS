# 10988
import sys
input = sys.stdin.readline

word = list(input())    # 단어 입력 받기 
trash = word.pop()  # 개행 문자 제거

# 팰린드롬 판별
flag = True
while len(word) > 1:    
    if word.pop(0) == word.pop():
        continue
    else:   # 팰린드롬이 아닐 경우
        flag = False    
        break

# print
if flag == True:
    print(1)
else:
    print(0)
