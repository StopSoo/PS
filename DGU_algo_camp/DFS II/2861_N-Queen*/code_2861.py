# N개의 퀸은 N줄에 걸쳐 하나씩 들어가야 한다는 기본 원리를 생각할 것 (!)
# 체크 배열을 사용하는 버전
# ** 복습하기 ** 
n = int(input())
chk = [[0 for _ in range(n)] for _ in range(n)]
cnt = 0

def dfs(k):
  global n, cnt, chk
  
  if k == n:
    cnt += 1
    return
  
  for i in range(n):
    if chk[k][i] > 0: continue
  # 한 지점을 잡고, 가로, 세로, 대각선에 있는 지점들의 값을 1씩 증가시킴.
  # 생각해보면 위에는 체크할 필요 X, 아래쪽만 체크
    for j in range(n):
      if k+j >= n: break
      if i-j >= 0: chk[k+j][i-j] += 1	# 왼쪽 아래로 대각선
      chk[k+j][i] += 1	# 세로
      if i+j < n: chk[k+j][i+j] += 1	# 오른쪽 아래로 대각선
          
    dfs(k+1)
    # 다음 번에도 사용하기 위해 값 복귀시킴
    for j in range(n):
      if k+j >= n: break
      if i-j >= 0: chk[k+j][i-j] -= 1
      chk[k+j][i] -= 1
      if i+j < n: chk[k+j][i+j] -= 1
          
dfs(0)

print(cnt)