# https://www.acmicpc.net/problem/2630

# 내 답안
# 걸린 시간: 64ms
# 재귀 / 분할 정복
# 2차원 배열 슬라이스 방법 체크 (!)
def count_wb(N, blocks):
  global count_w, count_b

  if all(all(x == 1 for x in row) for row in blocks): # 모두 파란색이라면
    count_b += 1
    return
  elif all(all(x == 0 for x in row) for row in blocks): # 모두 하얀색이라면
    count_w += 1
    return
  else: # 색이 다르다면
    if N//2 >= 1:
      count_wb(N//2, [row[:N//2] for row in blocks[:N//2]]) # 2사분면
      count_wb(N//2, [row[:N//2] for row in blocks[N//2:]]) # 3사분면
      count_wb(N//2, [row[N//2:] for row in blocks[:N//2]]) # 1사분면
      count_wb(N//2, [row[N//2:] for row in blocks[N//2:]]) # 4사분면
    else: return

N = int(input())
blocks = [list(map(int, input().split())) for _ in range(N)]

count_w, count_b = 0, 0 # 제출할 정답
count_wb(N, blocks) # 재귀함수 실행
print(count_w)
print(count_b)