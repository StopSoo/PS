# https://www.acmicpc.net/problem/10825

# 내 답안
# 걸린 시간: 412ms
import sys
input = sys.stdin.readline

N = int(input())
students = []
for _ in range(N):
  name, k, e, m = input().strip().split()
  students.append([name, int(k), int(e), int(m)])

students = sorted(students, key=lambda x: [-x[1], x[2], -x[3], x[0]])
for i in range(N): print(students[i][0])

# 만약 dict를 사용한다면, 27번째 줄과 같이 dic.items()를 정렬 후 다시 dict()를 해주면 됨!
import sys
input = sys.stdin.readline

N = int(input().rstrip())
dic = {}
for _ in range(N):
  name, a,b,c = map(str, input().rstrip().split())
  dic[name] = (int(a), int(b), int(c))

dic = dict(sorted(dic.items(), key=lambda x:(-x[1][0], x[1][1], -x[1][2], x[0])))
for k in dic.keys(): print(k)