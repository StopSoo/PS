#17298 

n = int(input())    # 배열의 원소의 개수 
ans = [0] * n       # 오큰수를 저장하는 배열 
A = list(map(int, input().split()))     # 값들이 들어있는 배열
myStack = []        # 인덱스를 저장할 스택

for i in range(n):
    # 인덱스를 -1로 하면 스택에서 top인 원소를 반환
    # 오큰수 조건 : 스택이 비어 있지 않고, 새로 들어온 값이 top에 있는 값보다 크다면
    while myStack and A[myStack[-1]] < A[i]: 
        ans[myStack.pop()] = A[i]   # 정답 리스트에 오큰수 저장
    myStack.append(i)   # 인덱스를 저장

while myStack:  # 스택이 빌 때까지
    ans[myStack.pop()] = -1

result = ""
for i in range(n):
    result += str(ans[i]) + " "

print(result)

# but 백준에서는 시간 초과가 뜸