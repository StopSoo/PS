# https://www.acmicpc.net/problem/19583

# 내 답안
# 걸린 시간: 200ms
# dt[name]처럼 딕셔너리에서 값 가져올 때 dt.get(값)으로 안전하게 값 가져오기!
# EOF 입력 처리는 항상 나를 당황하게 해 ;;
import sys
input = sys.stdin.readline

start, end, streaming = input().strip().split()
start_h, start_m = map(int, start.split(":"))
end_h, end_m = map(int, end.split(":"))
stream_h, stream_m = map(int, streaming.split(":"))

dt = dict()
while True:
  temp = input()
  if not temp: break # 입력이 없으면 끝내기
  temp = temp.strip()
  if not temp: continue # 빈 줄일 경우 무시
  
  time, name = temp.split()
  h, m = map(int, time.split(":"))
  if h * 60 + m <= start_h*60 + start_m: # 입장한 사람 체크
    dt[name] = 1 
  if end_h*60 + end_m <= h * 60 + m <= stream_h*60 + stream_m: # 퇴장한 사람 체크
    if dt.get(name) == 1: dt[name] = 0

print(sum(1 if val == 0 else 0 for val in dt.values()))
