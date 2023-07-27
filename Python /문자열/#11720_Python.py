count = int(input()) # 숫자의 개수를 입력 받음
number = input() # 숫자를 입력 받음

sum = 0 # 합을 계산할 변수
for i in range(count):
    sum += int(number[i])
    
print(sum)

# 파이썬 for문 C++과 헷갈리지 마시고 !
# 형 변환은 단순하게 해주면 됨 !
# 누적 변수 초기화 잊지 마시고 !
