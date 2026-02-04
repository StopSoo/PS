# https://www.acmicpc.net/problem/1764
# 260204 풀이
# 알고리즘: 정렬
# 시간: 76ms

# 내 답안
# 깨달은 점 1. 교집합 함수(intersection)를 사용하려면 리스트를 집합으로 바꿔라
# 깨달은 점 2. 집합에 대해서 sort() 함수는 적용 X, sorted() 함수는 적용된다.
import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
nListen = set(input().strip() for _ in range(N))
nWatch = set(input().strip() for _ in range(M))

nListenWatch = nListen.intersection(nWatch)

print(len(nListenWatch))
print(*sorted(nListenWatch), sep='\n')