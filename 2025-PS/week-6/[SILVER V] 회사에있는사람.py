# https://www.acmicpc.net/problem/7785

# 내 답안
# 처음에 시간초과가 나서 set을 사용해서 진행하면 좀 더 효율적이라는 것을 찾음 !!
# set() => add / remove, discard
import sys
input = sys.stdin.readline
print = sys.stdout.write

people = set() # set
N = int(input())
for _ in range(N):
  name, el = input().strip().split()
  if el == "enter": people.add(name)
  else: people.discard(name)
for name in sorted(people, reverse=True): print(name + '\n')