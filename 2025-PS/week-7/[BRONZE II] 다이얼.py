# https://www.acmicpc.net/problem/5622

# 내 답안
times = ['', '', '', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ'] # 소요 시간을 인덱스로

alpha = input().upper() # 모두 대문자만
answers = [time for a in alpha for time, t in enumerate(times) if a in t]
print(sum(answers))