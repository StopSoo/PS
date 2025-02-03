# https://school.programmers.co.kr/learn/courses/30/lessons/120861

# 내 답안
def solution(keyinput, board):
    pos = [0, 0]
    for key in keyinput:
        if key == "left": pos[0] = max(-(board[0]//2), pos[0]-1)
        elif key == "right": pos[0] = min(board[0]//2, pos[0]+1)
        elif key == "up": pos[1] = min(board[1]//2, pos[1]+1)
        elif key == "down": pos[1] = max(-(board[1]//2), pos[1]-1)
    return pos

# 딕셔너리를 사용해서 더해야 할 좌표를 불러올 수도 있음
# -(board[0]//2)처럼 연산자의 우선순위에서 살짝 막혔었는데, abs()를 사용할 수 있다는 것 체크!