# 그리디 알고리즘
# zip(리스트, 리스트) -> 두 리스트는 크기가 같아야 함
N = int(input())
S = 0

list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

list1.sort() # A 배열 정렬
list2 = sorted(list2, reverse=True) # B 배열 역순 정렬

for a, b in zip(list1, list2):
  S += a * b

print(S)