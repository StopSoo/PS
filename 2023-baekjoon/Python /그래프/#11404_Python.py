# 11404: 플로이드
import sys
input = sys.stdin.readline

n = int(input())    # 도시의 개수
m = int(input())    # 버스의 개수

# 인접 행렬 초기화 -> 충분히 큰 값으로 !
# distance = [[0] * n] * n -> 아래 방식으로 초기화할 것
# 인덱스랑 입력 받는 번호랑 맞추기 위해 배열을 (n+1)*(n+1) 크기로 초기화 
distance = [[sys.maxsize for j in range(n+1)] for i in range(n+1)]
for i in range(1, n+1):
    distance[i][i] = 0  # 자기 자신에 대해서는 비용이 0

# 입력 받기
for _ in range(m):
    s, e, c = map(int, input().split())
    if distance[s][e] > c:  # 입력 받은 비용이 현재 비용보다 더 작을 때만 업데이트해줘야 함 (!)
        distance[s][e] = c

# 플로이드-워셜 알고리즘
for k in range(1, n+1):
    for s in range(1, n+1):
        for e in range(1, n+1):
            distance[s][e] = min(distance[s][e], distance[s][k] + distance[k][e])

# 출력
for i in range(1, n+1):
    for j in range(1, n+1):
        if distance[i][j] == sys.maxsize:
            print(0, end=' ')
        else:
            print(distance[i][j], end=' ')
    print()

# 내가 놓친 부분1) Line 17 조건 부분
# 내가 놓친 부분2) Line 30 조건 부분