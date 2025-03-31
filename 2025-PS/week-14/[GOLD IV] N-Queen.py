# https://www.acmicpc.net/problem/9663

# 내 답안
# 걸린 시간: 10528ms (pypy3)
# 퀸들이 서로 공격할 수 없게 놓는다 -> 가로, 세로, 대각선에 놓지 않는다 (!)
# 대각선 체크할 때 -> 왼쪽 대각선은 i-j 값이 같고, 오른쪽 대각선은 i+j 값이 같다 (!)
# 제한 시간이 10초라서 브루트포스도 가능 !!
def find_way(n, row):
  global answer

  if row == n: # 모든 행을 다 돌았을 때 종료
    answer += 1
    return

  for col in range(n):
    # 이미 퀸이 놓인 열, 왼쪽 대각선, 오른쪽 대각선에 놓을 수 없으면 건너뛰기
    if (col in cols) or ((row-col) in left_diag) or ((row+col) in right_diag): continue
    # 퀸 놓기
    cols.add(col)
    left_diag.add(row-col)
    right_diag.add(row+col)
    # 다음 행으로 재귀 호출
    find_way(n, row+1)
    # 퀸 제거
    cols.remove(col)
    left_diag.remove(row-col)
    right_diag.remove(row+col)

N = int(input())
answer = 0 # 경우의 수
cols = set() # 열에 퀸이 놓였는지 체크
left_diag = set() # 왼쪽 대각선에 퀸이 놓였는지 체크 (i-j)
right_diag = set() # 오른쪽 대각선에 퀸이 놓였는지 체크 (i+j)

find_way(N, 0)
print(answer)