# https://www.acmicpc.net/problem/10798

# 내 답안
words = [list(input()) for _ in range(5)]

answer = ""
while True:
  for word in words:
    if word != []:
      answer += word[0]
      words[0] = words[0][1:]
  if words == [[], [], [], [], []]:
    break
print(answer)