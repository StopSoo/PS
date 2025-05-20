# https://www.acmicpc.net/problem/1780

# 내 답안
# 알고리즘/해결 전략: 재귀 방식으로 구현된 분할 정복.
# 시간 초과 나는 코드 !!
# 시간 초과 난 이유: 재귀 함수를 호출할 때마다 새로운 부분 배열을 생성해서 넘기기 때문.
import sys
input = sys.stdin.readline

def check_paper(n, arr):
  answer = [0, 0, 0]
  if all(x == -1 for row in arr for x in row): return [1, 0, 0]
  elif all(x == 0 for row in arr for x in row): return [0, 1, 0]
  elif all(x == 1 for row in arr for x in row): return [0, 0, 1]
  else: 
    answer = [a + b for a, b in zip(answer, check_paper(n // 3, [row[:n//3] for row in arr[:n//3]]))]
    answer = [a + b for a, b in zip(answer, check_paper(n // 3, [row[n//3:n//3 * 2] for row in arr[:n//3]]))]
    answer = [a + b for a, b in zip(answer, check_paper(n // 3, [row[n//3 * 2:] for row in arr[:n//3]]))]
    answer = [a + b for a, b in zip(answer, check_paper(n // 3, [row[:n//3] for row in arr[n//3:n//3 * 2]]))]
    answer = [a + b for a, b in zip(answer, check_paper(n // 3, [row[n//3:n//3 * 2] for row in arr[n//3:n//3 * 2]]))]
    answer = [a + b for a, b in zip(answer, check_paper(n // 3, [row[n//3 * 2:] for row in arr[n//3:n//3 * 2]]))]
    answer = [a + b for a, b in zip(answer, check_paper(n // 3, [row[:n//3] for row in arr[n//3 * 2:]]))]
    answer = [a + b for a, b in zip(answer, check_paper(n // 3, [row[n//3:n//3 * 2] for row in arr[n//3 * 2:]]))]
    answer = [a + b for a, b in zip(answer, check_paper(n // 3, [row[n//3 * 2:] for row in arr[n//3 * 2:]]))]
  return answer

N = int(input())
papers = list(list(map(int, input().strip().split())) for _ in range(N))

print(*check_paper(N, papers))

# 시간 초과를 해결한 코드
# 걸린 시간: 5680ms
# all()을 사용하는 것보다 이중for문을 사용해서 중간에 탈출하는 것이 더 효율적이다 (!)
import sys
input = sys.stdin.readline

def check_paper(n, arr, x=0, y=0):
  answer = [0, 0, 0]
  first = arr[x][y]
  same = True
  for i in range(x, x + n):
    for j in range(y, y + n):
      if arr[i][j] != first:
        same = False
        break
    if not same: break
  if same: # 구역 내 모든 값이 같으면 개수 갱신 후 탈출
    answer[first + 1] += 1  # -1 => 0, 0 => 1, 1 => 2
    return answer

  size = n // 3
  for dx in range(3):
    for dy in range(3):
      sub = check_paper(size, arr, x + (dx * size), y + (dy * size))
      answer = [a + b for a, b in zip(answer, sub)]
  return answer

N = int(input())
papers = [list(map(int, input().split())) for _ in range(N)]

print(*check_paper(N, papers))