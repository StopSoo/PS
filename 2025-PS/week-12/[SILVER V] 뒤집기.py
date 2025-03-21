# https://www.acmicpc.net/problem/1439

# 내 답안
# 걸린 시간: 36ms
S = input()
area_1 = 0
area_0 = 0

for i in range(1, len(S)):
  if S[i-1] == S[i]:
    if i < len(S)-1 and S[i] == S[i+1]: continue
    else:
      if S[i] == '1': area_1 += 1
      else: area_0 += 1
  else:
    # 예외 처리
    if i == 1 and S[i-1] == '1': area_1 += 1
    elif i == 1 and S[i-1] == '0': area_0 += 1

    if i < len(S)-1 and S[i] == S[i+1]: continue
    else:
      if S[i] == '1': area_1 += 1
      else: area_0 += 1

print(min(area_1, area_0))
