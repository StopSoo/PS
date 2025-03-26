# https://www.acmicpc.net/problem/9019

# 내 답안
# 처음에 DFS로 풀이하려다보니 안 풀렸음,, 바로 BFS로 바꿔서 풀이. 하지만 방문 배열을 사용하지 않아 문제가 생김.
# 처음에 문제를 제대로 이해하지 못해 놓친 점: 십진수라 4자리 중 빈 자리는 0으로 채운다는 점 (!)
# 다음으로 풀다가 잘못 짠 점: -인덱싱
# L, R 연산에서 숫자가 4자리가 아닐 때 오작동할 가능성이 있고, 0을 고려하는 방식이 꽤나 복잡해서 아래 코드는 탈락 ..
from collections import deque

T = int(input())
deq = deque()
for _ in range(T):
  a, b = input().split() # 문자로 받기
  deq.append((a, ''))

  while deq:
    number, ans = deq.popleft()
    if int(number) == int(b):
      print(ans)
      break

    deq.append(('0'*(4 - len(str(int(number) * 2 % 10000))) + str(int(number) * 2 % 10000), ans+'D'))
    deq.append(('0'*(4 - len(str(int(number)-1))) + str(int(number)-1) if int(number) >= 1 else '9999', ans+'S'))
    deq.append((number[1:] + number[0] if len(number) == 4 else '0'*(4 - len(number)-1) + number + '0', ans+'L'))
    deq.append((number[-1] + number[-4:-1] if len(number) == 4 else number[-1] + '0'*(4 - len(number)-1) + number, ans+'R'))

# 답안
# 걸린 시간: 8004ms (pypy3)
# 0을 체크하는 방식에 집중할 것 (!)
from collections import deque

def bfs(a, b):
  deq = deque([(a, "")])  # (현재 숫자, 명령어 문자열)
  visited = set()  # 방문한 숫자를 저장할 집합
  visited.add(a)  # 처음 숫자 방문 체크

  while deq:
    number, ans = deq.popleft()

    if number == b:
      return ans  # 정답 반환
    # D 연산 (2배 후 10000으로 나눈 나머지)
    D = (number * 2) % 10000
    if D not in visited:
      visited.add(D)
      deq.append((D, ans + 'D'))
    # S 연산 (n-1, 단 0이면 9999)
    S = 9999 if number == 0 else number - 1
    if S not in visited:
      visited.add(S)
      deq.append((S, ans + 'S'))
    # L 연산 (왼쪽 회전)
    L = (number % 1000) * 10 + number // 1000
    if L not in visited:
      visited.add(L)
      deq.append((L, ans + 'L'))
    # R 연산 (오른쪽 회전)
    R = (number % 10) * 1000 + number // 10
    if R not in visited:
      visited.add(R)
      deq.append((R, ans + 'R'))

T = int(input())
for _ in range(T):
  a, b = map(int, input().split())
  print(bfs(a, b))
