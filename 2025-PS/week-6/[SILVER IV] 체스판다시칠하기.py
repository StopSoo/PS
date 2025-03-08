# https://www.acmicpc.net/problem/1018

# 내 답안
# 푸는 데 30분 걸림
def check(h, w, array):
  ans1 = ['BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB']
  ans2 = ['WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW']

  answers = []
  for i in range(0, h-7): # 높이 시작 인덱스
    for j in range(0, w-7): # 너비 시작 인덱스
      count1 = 0 # ans1과 다른 정사각형 개수
      count2 = 0 # ans2와 다른 정사각형 개수
      for idx_r, row in enumerate(array[i:i+8]): # 행 순회 인덱스
        for idx_c, e in enumerate(row[j:j+8]): # 열 순회 인덱스
          if e != ans1[idx_r][idx_c]: count1 += 1
          if e != ans2[idx_r][idx_c]: count2 += 1
      answers.append(min(count1, count2))
  return min(answers)

N, M = map(int, input().split())
array = []
for i in range(N): array.append(input())
print(check(N, M, array))

# 보충) ans1, ans2 배열을 저렇게 수작업으로 구현해도 되지만, 다음과 같이 구현할 수도 있다.
# 인덱스 합의 짝홀 여부에 따라 값을 설정하는 방식 (!)
chess1 = [['' for _ in range(8)] for _ in range(8)]
chess2 = [['' for _ in range(8)] for _ in range(8)]

for i in range(8):
  for j in range(8):
    chess1[i][j] = ('W' if (i+j)%2 == 0 else 'B')
    chess2[i][j] = ('B' if (i+j)%2 == 0 else 'W')

# 추가로, 정답과 다른 부분의 개수 체크하는 로직은 저렇게 함수로 따로 뺴는 것이 가독성 면에서 훨씬 좋다.