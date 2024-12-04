# 순열 예시 코드
# 체크 배열 필수 (*)
N = 10
R = 3
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
check = [0] * N   # 원소 사용 여부를 체크
choose = []   # 나열한 원소를 보관

def permutation(level): # level: 선택한 원소의 개수
  if level == R:
    print(choose)
    return

  for i in range(N):
    if check[i] == True:
      continue

    choose.append(lst[i]) # 인덱스가 i인 원소를 선택(추가)
    check[i] = True

    permutation(level + 1)  # 다음 for문으로 들어가는 역할

    check[i] = False  # 인덱스가 i인 원소의 사용이 종료됨
    choose.pop()  # 넣었던 인덱스가 i인 원소를 제거

permutation(0)