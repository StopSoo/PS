# 출력 형식을 잘 지키자!
# 입력 값 형태가 이미 오름차순이기 때문에 출력에 대한 오름차순은 신경 쓰지 않아도 됨
def combination(index, level):
  global choose, k, numbers

  if level == 6:
    for c in choose:
      print(c, end=" ")
    print()
    return
  
  for i in range(index, k):
    choose.append(numbers[i])
    combination(i + 1, level + 1) # 다음 원소에 대해 진행
    choose.pop()

while 1:
  choose = [] # 선택한 원소들의 배열
  numbers = list(map(int, input().split()))
  if numbers == [0]:  # 입력이 0이면 종료
    break
  k = int(numbers.pop(0))

  combination(0, 0)
  print()

# 파이썬의 조합 라이브러리를 활용하는 풀이 (*)
from itertools import combinations

while 1:
  numbers = list(map(int, input().split()))

  k = numbers[0]
  arr = numbers[1:]
  if k == 0: break

  for comb in combinations(arr, 6):
    for c in comb:
      print(c, end=" ")
    print()
  print()
