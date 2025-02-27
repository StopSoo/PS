# https://school.programmers.co.kr/learn/courses/30/lessons/81302#qna
# 2021 카카오 채용연계형 인턴십

# 답안 1
def safety(room):
  checked = [[0]*5 for i in range(5)] # 1의 사회적 거리가 되는 칸을 표시하는 배열
  for y in range(5):
    for x in range(5):
      if room[y][x] == 'P':
        success = bubble(y, x, room, checked)
        if not success: return 0
  return 1

def bubble(y, x, room, checked):
  _dy = [0, 0, 0, 1, -1]
  _dx = [0, 1, -1, 0, 0]

  for direction in range(5): # self + WASD
    dy, dx = _dy[direction], _dx[direction]
    if dy != 0 and dy == dx: 
      continue
    if 0 <= y+dy < 5 and 0 <= x+dx < 5: # if valid block
      if checked[y+dy][x+dx]:         # 사람 or 빈 테이블로 표시해둔 곳에 다시 방문 -> 사회적 거리가 2 이하
        return False
      elif room[y+dy][x+dx] == 'X':   # 파티션은 무시
        continue
      checked[y+dy][x+dx] = 1         # 빈 테이블 or 사람 (사회적 거리 체크 가능 위치)
  return True

def solution(places):
  return [safety(room) for room in places]

# 답안 2: 경우의 수가 적으므로 직접 체크
def check(place):
  for irow, row in enumerate(place):
    for icol, cell in enumerate(row):
      if cell != 'P':
        continue
      # 사람인 경우 아래 케이스들을 체크
      if irow != 4 and place[irow + 1][icol] == 'P':
        return 0
      if icol != 4 and place[irow][icol + 1] == 'P':
        return 0
      if irow < 3 and place[irow + 2][icol] == 'P' and place[irow + 1][icol] != 'X': # 사람과 사람 사이에 테이블
        return 0
      if icol < 3 and place[irow][icol + 2] == 'P' and place[irow][icol + 1] != 'X': # 사람과 사람 사이에 테이블
        return 0
      if irow != 4 and icol != 4 and place[irow + 1][icol + 1] == 'P' and (place[irow + 1][icol] != 'X' or place[irow][icol + 1] != 'X'):
        return 0
      if irow != 4 and icol != 0 and place[irow + 1][icol - 1] == 'P' and (place[irow + 1][icol] != 'X' or place[irow][icol - 1] != 'X'):
        return 0
  return 1

def solution(places):
  return [check(place) for place in places]
