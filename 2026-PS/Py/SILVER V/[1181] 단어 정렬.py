# https://www.acmicpc.net/problem/1181
# 260105 풀이
# 알고리즘: 정렬
# 시간: 564ms

N = int(input())
words = sorted(list(set(input().strip() for _ in range(N))), key=lambda x: [len(x), x])
print(*words, sep='\n')
