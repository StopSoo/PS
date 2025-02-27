# https://www.acmicpc.net/problem/1764

# 내 답안
# 걸린 시간: 76ms (빠른 입출력 사용 전: 2564ms)
# 출력 형식을 잘 체크하세욧 !!
# 변수 범위를 보고 크다면 무조건 빠른 입출력을 사용하세욧 !! 
import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
listen = set(input().strip() for _ in range(N))
watch = set(input().strip() for _ in range(M))
both = set(listen & watch)

print(len(both))
for name in sorted(both): print(name)
# 혹은 sep 옵션을 사용해서 다음과 같이 출력 가능
# print(*sorted(both), sep='\n')