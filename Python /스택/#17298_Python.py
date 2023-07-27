# 17298 : 오큰수
# 오큰수가 아닌 조건 1) 오른쪽에 수가 없다. 2) 오른쪽에 큰 수가 없다.

n = int(input())    # 수열 A의 크기 입력 받음
A = list(map(int, input().split())) # 수열 A 입력 받음
NGE = [0] * n       # NGE를 담을 배열 초기화

# 오큰수 배열 채우기
for i in range(0, n):
    if i == n-1:          # 배열의 마지막 원소의 오큰수는 -1
        NGE[i] = -1
        break
    
    target_idx = -1     # 아직 오큰수의 인덱스가 설정되지 않았음
    for j in range(i+1, n):
        if A[i] < A[j]: # 오른쪽에 수가 있으면서 큰 경우
            if target_idx == -1:    # 가장 왼쪽에 있는 경우 
                target_idx = j
                NGE[i] = A[j]
                break
            else:
                break
        else: # 오른쪽에 수가 있지만 크지 않은 경우
            if j == n-1:    # 오큰수가 없는 경우
                NGE[i] = -1
            else:
                continue

# 출력단
for i in range(n):
    print(NGE[i], end=" ")

# 결과는 잘 나오지만 시간 초과 뜸 ! -> 시간 복잡도를 고려해야 함.