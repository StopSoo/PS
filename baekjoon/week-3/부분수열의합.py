from itertools import combinations

N, S = map(int, input().split())
numbers = list(map(int, input().split()))
count = 0

for i in range(1, len(numbers) + 1): # 고를 개수
    for l in combinations(numbers, i): # 조합 리스트 뽑기
        sumRes = sum(l)
        if sumRes == S:
            count += 1

print(count)
