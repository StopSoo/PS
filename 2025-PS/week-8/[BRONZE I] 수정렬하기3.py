# https://www.acmicpc.net/problem/10989

# 내 답안
# 걸린 시간: 8292ms
# 일반적으로 리스트에 모두 담아서 정렬해서 출력하는 방법은 시간 초과 & 메모리 초과가 나게 됨
# 이 문제의 핵심은 N은 최대 1000만이므로 리스트에 모두 저장하면 시간 초과가 뜨지만,
# 나올 수 있는 수는 최대 10000인 것에 있음 (!)
import sys
input = sys.stdin.readline
print = sys.stdout.write

dic = dict()
N = int(input().strip())
for _ in range(N):
  number = int(input())
  if number in dic.keys():
    dic[number] += 1
  else:
    dic[number] = 1

for key in sorted(dic.keys()):
  for _ in range(dic[key]):
    print(str(key) + '\n')