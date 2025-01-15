# sorted(iterable, key, reverse=False)
n = int(input())  # 선수의 수
people = [list(map(int, input().split())) for _ in range(n)]
# 채점 기준대로 넣어서 정렬
scores = [[p * q * r, p + q + r, number] for number, p, q, r in people]
scores = sorted(scores)

print(scores[0][2], scores[1][2], scores[2][2])

# 람다 함수를 사용하는 방법
n = int(input())
infos = [list(map(int, input().split())) for _ in range(n)]

def comp(x):  # 정렬 기준
  return [x[1] * x[2] * x[3], x[1] + x[2] + x[3], x[0]]

infos = sorted(infos, key=comp)

for b, p, q, r in infos[:3]:
  print(b, end=' ')