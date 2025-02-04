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