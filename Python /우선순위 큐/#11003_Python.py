# 11003 : 최솟값 찾기
# 슬라이딩 윈도우와 정렬 -> but, sort를 사용하면 시간 복잡도 측면에서 무조건 걸림
# 슬라이딩 윈도우를 덱으로 구현하여 정렬의 효과를 볼 수 있다는 게 포인트 !
from collections import deque
import sys
input = sys.stdin.readline

N, L = map(int, input().split())    # 데이터 개수, 슬라이딩 윈도우 크기
mydeque = deque()   # 데이터를 담을 덱 자료구조
now = list(map(int, input().split()))    # 주어진 숫자 데이터를 가지는 리스트
result = []

mydeque.append([1, now[0]]) # 배열의 첫 원소 추가
result.append(mydeque[0][1])

for i in range(1, N):
    if mydeque[-1][1] > now[i]:  # 덱의 마지막 원소 값이 새로 들어올 값보다 크다면
        mydeque.pop() # 해당 노드 제거 -> 어차피 최소값 아님 !
        mydeque.append([i+1, now[i]])
        while i+1 - L >= mydeque[0][0]:    # 슬라이딩 윈도우 범위를 벗어난 상태일 경우 계속 popleft
            mydeque.popleft()
    else:   # 슬라이딩 윈도우 범위 체크
        if i+1 - L < mydeque[0][0]:   # 슬라이딩 윈도우 안에 있다면
            mydeque.append([i+1, now[i]])
        else:   
            mydeque.popleft()   # 슬라이딩 윈도우 밖에 있는 원소 제거
    result.append(mydeque[0][1])    # 현재 덱에 맨 앞에 있는 원소가 최소값 (!)

# 출력
for i in range(N):
    print(result[i], end=" ")

# 내가 짠 코드는 예시에는 맞게 나오나 어디선지 틀린 풀이임 !
# 보완할 부분
# 1. 덱의 마지막 원소 -> 인덱스 -1
# 2. result 리스트 사용하지 말고 for문 한 번 돌 때마다 print하기

# 맞는 풀이
import sys
from collections import deque

input = sys.stdin.readline

N, L = map(int,input().split())
mydeque = deque()
now = list(map(int, input().split()))

for i in range(N):
    while mydeque and mydeque[-1][1] > now[i]:  # 덱이 비어있지 않고 덱의 마지막 원소가 다음에 들어올 값보다 크다면
        mydeque.pop()
    mydeque.append([i, now[i]])
    if mydeque[0][1] <= i-L:    # 윈도우 범위를 벗어나면
        mydeque.popleft()
    print(mydeque[0][1], end=" ")