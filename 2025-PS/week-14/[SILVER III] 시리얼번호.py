# https://www.acmicpc.net/problem/1431

# 내 답안
# 걸린 시간: 36ms
# 문자.isdigit() -> 숫자면 True / 문자면 False 반환
N = int(input())
serial = list(input() for _ in range(N))
serial = sorted(serial, key=lambda x: [len(x), sum(int(i) for i in x if i.isdigit()), x])
print(*serial, sep='\n')