# 2581

m = int(input())
n = int(input())

prime_num = []  # 소수를 담을 배열
for i in range(m, n+1): # m 이상 n 이하
    flag = True # 해당 수가 소수인지 판별
    if i > 1:
        for j in range(2, i):   # 1을 제외하고 약수가 존재하는지 체크
            if i % j == 0:  # 약수가 하나라도 있으면 flag 변경
                flag = False
                break
        if flag == True:    # 약수가 하나도 없으면 소수 배열에 추가 
            prime_num.append(i)

# print
if len(prime_num) > 0:
    print(sum(prime_num))
    print(min(prime_num))
else:   # 소수 배열의 원소의 개수가 0일 때는 -1을 출력
    print(-1)

# 9번째 조건문 추가가 해결책이였음. 