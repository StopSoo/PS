# https://www.acmicpc.net/problem/1769

# 내 답안
# 걸린 시간: 732ms -> 104ms
# 시간 크게 줄일 수 있었던 부분 -> 처음엔 while True 하고 조건문으로 1 <= len(number) <= 9를 넣었는데 이 부분이 오래 걸렸음.
number = input()
count = 0
while len(number) > 1:
  number = str(sum(map(int, number)))
  count += 1

print(count)
print("YES" if int(number) % 3 == 0 else "NO")