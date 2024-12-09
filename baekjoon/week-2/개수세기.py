# 리스트.count(비교할 값) -> 굳이 for문 사용하지 않아도 간단하게 해결!
N = int(input()) # 리스트 원소 개수
numbers = list(map(int, input().split()))
v = int(input())  # 비교할 수

print(numbers.count(v))