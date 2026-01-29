# https://www.acmicpc.net/problem/2108
# 260129 풀이
# 알고리즘: 구현

# 내 답안
# 시간: 시간 초과 !!!!!!!!!!! (이유: count 때문이라고 생각)
import sys
input = sys.stdin.readline 

N = int(input())
numbers = sorted(list(int(input().strip()) for _ in range(N)))
counts = [numbers.count(num) for num in numbers]
frequent_numbers = list(set(numbers[i] for i, count in enumerate(counts) if count == max(counts)))
frequent_numbers.sort()

print(round(sum(numbers) / N))
print(numbers[N // 2])
print(frequent_numbers[1] if len(frequent_numbers) >= 2 else frequent_numbers[0])
print(numbers[-1] - numbers[0])

# 시간 초과 안 나는 답안
# 시간: 316ms
from collections import Counter
import sys
input = sys.stdin.readline

N = int(input().strip())
numbers = sorted([int(input().strip()) for _ in range(N)])
counts = Counter(numbers).most_common(2) # 최빈값들 중 2개

print(round(sum(numbers) / N))
print(numbers[N//2])
print(counts[0][0] if len(counts) == 1 or (len(counts) > 1 and counts[0][1] != counts[1][1]) else counts[1][0])
print(str(max(numbers) - min(numbers)))