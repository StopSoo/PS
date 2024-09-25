# 10867 : 중복 빼고 정렬하기
# 입력
N = int(input())
list_n = list(map(int, input().split()))  

list_n = list(set(list_n))    # 중복 제거
list_n.sort()   # 정렬

# 출력
print(' '.join(map(str, list_n)))

# 출력 형태 익숙해지기 !