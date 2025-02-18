# https://www.acmicpc.net/problem/11866

# 내 답안
# 걸린 시간: 56ms
# f-string: print(f'문자열') -> 원하는 대로 formatting 가능
# 뭘 써야 할지 생각이 안 났는데 deque의 rotate가 생각 나서 사용 (!)
from collections import deque

N, K = map(int, input().split())
answer = []
cards = deque([i for i in range(1, N+1)]) # 선언과 동시에 초기화
while len(cards) != 0:
  cards.rotate(-K) # 왼쪽으로 회전
  answer.append(str(cards.pop()))
print(f'<{", ".join(answer)}>')

# 다른 사람들 답안을 보니 % 연산자 써서 인덱스 계산하고 하던데, rotate 쓰는 게 가장 직관적이고 좋을 것 같음 !