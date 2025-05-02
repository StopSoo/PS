# https://www.acmicpc.net/problem/1380

# 내 답안
# 걸린 시간: 32ms
import sys
input = sys.stdin.readline

answers = []
while True:
  N = int(input())
  if N == 0: break # 입력이 0이면 종료.
  
  students = [0] + list(input().strip() for _ in range(N)) # 학생들 이름
  check = [0] * (N+1) # 압수/반환 여부 체크 배열

  for _ in range(N*2-1):
    number, ch = input().strip().split()
    check[int(number)] = (check[int(number)] + 1) % 2 # 압수/반환 여부 체크
  for ind in range(1, N+1):
    if check[ind] == 1: answers.append(students[ind])
# 출력
for i in range(len(answers)):
  print(i+1, answers[i])

# 작성하면서 고친 코드
# 아래 코드에서는 제너레이터가 answers 배열에 들어가게 됨.
answers.append(students[ind] for ind in range(1, N+1) if check[ind] == 1)
# iterable의 모든 요소를 리스트에 추가하기 위해서는 "extends"를 사용한다 (!)
# 위와 같이 리스트 컴프리헨션을 사용하는 방식으로 고친다면 아래와 같이 된다.
# 아래 경우에는 괄호([])를 생략하는 것도 가능하다.
answers.extend([students[ind] for ind in range(1, N+1) if check[ind] == 1])