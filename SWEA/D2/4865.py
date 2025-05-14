# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AWTQSs6qQL0DFAVT&categoryId=AWTQSs6qQL0DFAVT&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=PYTHON&select-1=2&pageSize=10&pageIndex=1

# 내 답안
T = int(input())
for i in range(T):
  str1 = input()
  str2 = input()
  dt = dict()
  for ch in str1:
    dt[ch] = str2.count(ch)
  print(f'#{i+1} {max(dt.values())}')