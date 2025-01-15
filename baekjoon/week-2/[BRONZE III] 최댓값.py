# max / min 함수
# 리스트.index(값): 리스트에서 값의 인덱스를 반환
numbers = []
for _ in range(9):
  a = int(input())
  numbers.append(a)

print(max(numbers))
print(numbers.index(max(numbers)) + 1)