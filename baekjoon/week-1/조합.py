# 조합 예시 코드
# 체크 배열 필요 X
N = 10
R = 5
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
choose = [] # 선택한 원소를 보관

def combination(index, level):
  if level == R:
    print(choose)
    return
  
  for i in range(index, N):
    choose.append(lst[i]) # 인덱스가 i인 원소를 선택(추가)
    combination(i + 1, level + 1) # 다음 for문으로 들어가는 역할
    choose.pop()  # 넣었던 인덱스가 i인 원소를 제거

combination(0, 0)