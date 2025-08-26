# https://www.acmicpc.net/problem/15903

# 내 답안
# 걸린 시간: 276ms
# 알고리즘: 그리디
import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())
cards = sorted(list(map(int, input().strip().split())))

for _ in range(m):
  a, b = cards[0], cards[1]
  cards = sorted(cards[2:] + [a + b] * 2)
print(sum(cards))

# 우선순위큐(힙)를 사용한 답안
# 걸린 시간: 52ms
import sys, heapq
input = sys.stdin.readline

n, m = map(int, input().strip().split())
cards = list(int(number) for number in input().strip().split())

heapq.heapify(cards)

for _ in range(m):
  a, b = heapq.heappop(cards), heapq.heappop(cards)

  heapq.heappush(cards, a + b)
  heapq.heappush(cards, a + b)

print(sum(cards))