# ' '.join(리스트): 문자열 리스트에만 적용 가능!
N, X = map(int, input().split())
numbers = input().split()

answer = []
for n in numbers:
  if int(n) < X:
    answer.append(n)

print(' '.join(answer))