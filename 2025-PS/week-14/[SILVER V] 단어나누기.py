# https://www.acmicpc.net/problem/1251

# 내 답안
# 걸린 시간: 36ms
# 처음에 그리디 알고리즘 썼는데 시간초과 나서 별 짓을 다 하다가 결국 브루트포스로 ...
# 문제 조건) 세 단어로 나누어야 함. 한 단어의 길이는 1 이상.
word = input()
answers = []
for fir in range(1, len(word)-1):
  answer = ''
  answer += word[:fir][::-1]
  for sec in range(fir+1, len(word)):
    answer += word[fir:sec][::-1] + word[sec:][::-1]
    answers.append(answer)
    answer = word[:fir][::-1] # 복구

print(sorted(answers)[0])