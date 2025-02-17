# https://www.acmicpc.net/problem/2751

# 내 답안
# 일단 N이 100만까지라서 list 대신 set을 사용한 것까진 ok.
# set을 사용하니 자동으로 오름차순 정렬이 돼서 정렬을 따로 안 했더니 계속 '틀렸습니다'가 나옴. -> 명시적으로 정렬을 해줘야 하는 건가?
import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input().strip())
numbers = sorted(set(int(input().strip()) for _ in range(N)))
for num in numbers: print(str(num) + '\n')