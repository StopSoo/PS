# https://www.acmicpc.net/problem/11478

# 내 답안
# 걸린 시간: 468ms
word = input()
answers = set()
for l in range(1, len(word)+1): # 문자열의 길이
  for s in range(len(word)-l+1): # 시작 인덱스
    answers.add(word[s:s+l])
print(len(answers))