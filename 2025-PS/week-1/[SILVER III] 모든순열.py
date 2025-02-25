# https://www.acmicpc.net/problem/10974

# 내 답안
# permutations(arr, r)에서 r은 사용하지 않는다면 생략 가능 -> 기본값으로 배열의 길이가 들어감
# 출력문 형태에 유의할 것 (*)
from itertools import permutations

N = int(input())

for per in permutations(range(1, N + 1)):
  print(' '.join(map(str, per)))