# https://www.acmicpc.net/problem/2108

# 내 답안
# 걸린 시간: 424ms
# 처음 풀 때 -> 리스트.count 사용했는데 시간 초과 뜸
# Counter.most_common(개수): 넣은 개수만큼의 최빈값을 리스트로 반환 Ex> [(-2, 1), (1, 1)]: (값, 개수)
from collections import Counter
import sys
input = sys.stdin.readline

N = int(input().strip())
numbers = sorted([int(input().strip()) for _ in range(N)])
counts = Counter(numbers).most_common(2)

print(round(sum(numbers) / N))
print(numbers[N//2])
print(counts[0][0] if len(counts) == 1 or (len(counts) > 1 and counts[0][1] != counts[1][1]) else counts[1][0])
print(str(max(numbers) - min(numbers)))