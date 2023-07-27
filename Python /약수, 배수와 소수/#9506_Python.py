# 9506

while True:
    n = int(input())    # 약수를 구할 수
    if n == -1: # 입력 값이 -1이라면 반복문 종료
        break
    
    divisors = []   # 약수들의 배열
    sum = 0     # n이 아닌 약수들의 합을 담을 변수
    for i in range(1, n): # 자신을 제외한 n의 약수 구하기 
        if n % i == 0:
            divisors.append(i)
            sum += i
    if n == sum:    # n이 완전수라면
        print(n, '= ', end="")
        for i in range(len(divisors)-1):
            print(divisors[i], '+ ', end="")
        print(divisors[len(divisors)-1])
    else:   # n이 완전수가 아니라면 
        print(n, 'is NOT perfect.')
    