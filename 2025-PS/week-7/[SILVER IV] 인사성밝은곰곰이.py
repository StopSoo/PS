# https://www.acmicpc.net/problem/25192

# 내 답안
# 집합의 원소 개수도 len()을 사용
# 빠른 입출력 사용 전: 2556ms / 사용 후: 80ms
import sys
input = sys.stdin.readline

answer = 0
count = int(input().strip())
people = set()
for i in range(count):
  chat = input().strip()
  if chat == "ENTER": 
    answer += len(people)
    people = set() # 집합 비우기
  else: people.add(chat)
  
  if i == (count-1): answer += len(people)

print(str(answer) + '\n')