# 1517_commentary
# N이 최대 500,000이므로 절대 N^2의 시간 복잡도를 가진 알고리즘으로는 풀 수 없다.
# 하지만 버블 정렬의 시간 복잡도는 N^2이므로 버블 정렬로는 풀 수 없다.  
# 따라서 O(nlogn)의 시간 복잡도를 가지는 병합 정렬을 사용해야 한다. 

import sys
input = sys.stdin.readline

result = 0  # swap 횟수를 담을 변수

N = int(input())    # 수열 원소의 개수
A = list(map(int, input().split())) # 수열 입력 받기
A.insert(0, 0)  # index를 1부터 시작하기 위해 추가
tmp = [0] * int(N+1)    # 정렬을 위한 임시 배열

# 병합 정렬을 재귀 형태로 구현
def merge_sort(s, e):
    global result   # 전역 변수
    if e-s < 1: # 원소가 없을 경우
        return
    m = int(s + (e-s)/2)    # 가운데 값 
    merge_sort(s, m)
    merge_sort(m+1, e)

    for i in range(s, e+1): # 원본 배열에서 임시 배열로 단순 복사
        tmp[i] = A[i]
    
    # 투 포인터
    k = s   # 실제 A 배열에서 데이터가 들어가야 하는 위치 인덱스 
    index1 = s
    index2 = m+1
    while index1 <= m and index2 <= e:
        if tmp[index1] > tmp[index2]:   # 앞 그룹의 값이 뒤 그룹의 값보다 크다면 
            A[k] = tmp[index2]
            result += index2 - k    # swap 횟수 = 앞에 남아 있는 원소의 개수 (!)
            k += 1
            index2 += 1
        else:   # 뒤 그룹의 값이 앞 그룹의 값보다 크다면
            A[k] = tmp[index1]
            k += 1
            index1 += 1
    # 한 쪽 그룹이 끝난 경우 나머지를 뒤에 다 붙여주면 됨
    while index1 <= m:
        A[k] = tmp[index1]
        k += 1
        index1 += 1
    while index2 <= e:
        A[k] = tmp[index2]
        k += 1
        index2 += 1

merge_sort(1, N)
print(result)