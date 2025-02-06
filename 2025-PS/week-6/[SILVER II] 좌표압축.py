# https://www.acmicpc.net/problem/18870

# 내 답안 -> 답 잘 나옴 but 시간 초과 
import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input().strip())
numbers = list(map(int, input().strip().split()))
new_numbers = sorted(set(numbers))
print(' '.join([str(new_numbers.index(num)) for num in numbers]) + '\n')

# 다른 사람 답안 참고해서 풀기
# bisect_left(리스트, 값): 해당 값이 리스트에 있을 때 해당 index를 반환
# 하지만 별로 빠르진 않음
from bisect import bisect_left
N = int(input())
numbers = list(map(int, input().split()))
new_numbers = sorted(set(numbers))
for number in numbers:
  print(bisect_left(new_numbers, number), end=' ')