# 10811 : 바구니 뒤집기
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

array = []
for i in range(N):  # 배열 생성
    array.append(i+1)

for _ in range(M):
    i, j = map(int, input().split())    # 1<=i<=j<=N 
    # 해당 인덱스 부분만 reversed
    array = array[:i-1] + list(reversed(array[i-1:j])) + array[j:]  

# print
for i in range(N):
    print(array[i])

# reversed만 하면 객체가 반환되므로 list로 형 변환이 필요함 !
# 역순 변경하지 않은 부분은 그대로 붙여줘야 함