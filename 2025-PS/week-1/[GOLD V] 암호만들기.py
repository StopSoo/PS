# 체크해야 할 조건: "최소 한 개의 모음과 최소 두 개의 자음으로 구성"
from itertools import combinations

L, C = map(int, input().split())
chs = list(input().split())
answer = []

first = []  # 모음 
second = [] # 자음
for ch in chs:
  if ch in ['a', 'e', 'i', 'o', 'u']:
    first.append(ch)
  else:
    second.append(ch)

while 1:
  for count in range(1, L-1):  # 모음의 개수를 체크(자음이 최소 2개여야 하므로)
    for comb1 in combinations(first, count):
      for comb2 in combinations(second, L-count):
        choose = [] 
        for c1 in comb1:
          choose.append(c1)
        for c2 in comb2:
          choose.append(c2)    

        choose.sort()
        word = ""
        for c in choose:
          word = word + c
        answer.append(word)
  break

answer.sort()
for ans in answer:
  print(ans)

# 라이브러리를 사용하는 더 효율적인 코드
# list() 하지 않아도 split()을 통해 리스트화됨 (*)
# arr.sort(): arr을 직접 정렬시킴 / sorted(arr): arr은 변화시키지 않고, 정렬한 배열을 반환함 
from itertools import combinations

vows = ['a', 'e', 'i', 'o', 'u']
# 조건을 충족하는지 체크하는 함수
def is_possible(word):
  global L, C, arr

  vow = 0 # 모음의 개수
  for w in word:
    vow += (w in vows)
  con = L - vow # 자음의 개수

  return (vow >= 1 and con >= 2)

L, C = map(int, input().split())
arr = input().split() 
arr.sort()

for word in combinations(arr, L):
  if is_possible(word):
    print(''.join(word))