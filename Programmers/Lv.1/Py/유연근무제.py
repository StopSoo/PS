# https://school.programmers.co.kr/learn/courses/30/lessons/388351

def solution(schedules, timelogs, startday):
  answer = 0
  for i in range(len(schedules)):
    check = True # 일주일 모두 제대로 출근했는가
    for j, timelog in enumerate(timelogs[i]):
      if (j + startday - 1) % 7 + 1 in [6, 7]: continue
      
      h, m = schedules[i] // 100, schedules[i] % 100
      if m + 10 >= 60:
        h += 1
        m = (m + 10) % 60
      else:
        m += 10
      standard_time = h * 100 + m
      if timelog > standard_time: 
        check = False
        break
    
    if check: answer += 1
          
  return answer

# 리뷰
# 1. 이게 안되겠어? 하는 것도 다시 짚고 넘어가자
# 2. 조건을 작성하며 꼼꼼히 체크하자
# 3. 하드코딩은 지양하자