# permutations(arr, r)에서 r은 사용하지 않는다면 생략 가능
# 출력문 형태에 유의할 것 (*)
from itertools import permutations

N = int(input())

for per in permutations(range(1, N + 1)):
  print(' '.join(map(str, per)))