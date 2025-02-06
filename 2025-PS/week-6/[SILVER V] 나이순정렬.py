# https://www.acmicpc.net/problem/10814

# 내 답안
# 깨달은점 1) 빈 리스트 초기화 시 리스트 컴프리헨션 사용하기
# 깨달은점 2) 빠른 입출력 사용 안했을 때: 2708ms / 사용했을 때: 152ms ((속도 차이))
import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input().strip())
people = [[] for _ in range(200)] 

for _ in range(N):
  age, name = input().strip().split()
  people[int(age)-1].append(name) # 입력된 순서대로 이름이 추가됨

for i, p in enumerate(people):
  while p: # 배열 안에 이름이 있으면
    print(str(i+1)+' '+p[0]+'\n') # print 안에 하나의 문자열이 들어가야 함
    p.remove(p[0])
