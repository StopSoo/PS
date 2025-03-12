# https://www.acmicpc.net/problem/5525

# 내 답안
# 걸린 시간: 368ms
# 50점 반만 맞았는데, 도움을 받아 나머지 50점도 채움
# KMP 알고리즘을 참고 (!)
N = int(input()) # O의 개수
M = int(input()) # 문자열 S의 길이
S = input() # 문자열 

count = 0 # 제출할 정답
cnt_o = 0 # 계산한 O의 개수
i = 0
while i <= (M-1):
  if cnt_o == N:
    count += 1
    cnt_o -= 1 # 내가 가장 헷갈린 부분 (!)

  if S[i:i+3] == "IOI":
    cnt_o += 1
    i += 2
  else:
    cnt_o = 0
    i += 1

print(count)