# https://www.acmicpc.net/problem/1620

# 내 답안
import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
animals = dict()
for i in range(1, N+1): animals[i] = input().strip() # 딕셔너리 생성

for _ in range(M):
  q = input().strip()
  if q.isdigit(): print(animals[int(q)])
  else: 
    for key, name in list(animals.items())[::-1]:
      if name == q: 
        print(key)
        break

# 다른 사람이 작성한 답안
# 걸린 시간: 232ms
# 풀이 포인트) 해시맵에서 키에 대응하는 값을 가져오는 것은 O(1) -> 키와 인덱스가 바뀐 딕셔너리를 만든다.
# -> 인덱스를 찾는 것은 O(N)의 시간 복잡도가 필요.
# 알아둘 포인트) dict[key]: 키가 없으면 error 발생 / dict.get(key, default): 키가 없으면 default(기본값은 None) 반환
import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())

dt = {}
for i in range(1, N+1): dt[i] = str(input().strip())

inverted_dt = {v: k for k, v in dt.items()}

for _ in range(M):
  q = input().strip()
  if q.isdigit() and 1 <= int(q) <= N: print(dt.get(int(q)))
  else: print(inverted_dt.get(q))