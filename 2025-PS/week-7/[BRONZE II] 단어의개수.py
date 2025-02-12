# https://www.acmicpc.net/problem/1152

# 내 답안
# 찾아보니 공백 하나만 주어지는 입력도 있다고 해서, 공백을 세는 로직은 맞지 않다고 생각이 듬.
# strip([chars]): 선후행 문자가 제거된 문자열의 복사본을 돌려줌. 인자가 생략되면 공백을 제거, 모든 값들의 조합 제거 가능.
# lstrip([chars]): 선행 문자만 지울 때 사용
# rstrip([chars]): 후행 문자만 지울 때 사용
words = input()
print(len(words.split()))