# 11399_commentary

n = int(input())    # 사람의 수
A = list(map(int, input().split()))   # 각 사람이 필요한 시간
S = [0] * n  # 누적 시간 

# 삽입 정렬
for i in range(1, n):
    insert_point = i    # 삽입할 값의 인덱스
    insert_value = A[i] # 삽입할 값

    for j in range(i-1, -1, -1):
        if A[j] < A[i]: # 삽입할 값보다 작은 값이 나오면
            insert_point = j+1  # 그 작은 값의 오른쪽에 삽입
            break
        if j == 0:  # 삽입할 값보다 작은 값이 없다면 
            insert_point = 0    # 맨 처음에 삽입
    
    for j in range(i, insert_point, -1):
        A[j] = A[j-1]
    A[insert_point] = insert_value

# 합 배열 구하기
S[0] = A[0]
for i in range(1, n):
    S[i] = S[i-1] + A[i]

# 시간 합의 최솟갑 구하기
sum = 0
for i in range(0, n):
    sum += S[i]

print(sum)