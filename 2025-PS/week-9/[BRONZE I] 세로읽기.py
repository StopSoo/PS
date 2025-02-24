# https://www.acmicpc.net/problem/10798

# 내 답안
# 걸린 시간: 40ms
# 파이썬 리스트에서 인덱스로 제거: del 요소
words = [list(input()) for _ in range(5)]

answer = ""
while True:
  for word in words:
    if word != []:
      answer += word[0]
      del word[0]
  if words == [[], [], [], [], []]:
    break
print(answer)