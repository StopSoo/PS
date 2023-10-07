# 2501

n, k = map(int, input().split()) # 약수를 구할 수와 몇 번째 약수를 출력할 것인지

divisors = []   # 약수를 담을 배열 선언
for i in range(1, n+1):     # n의 약수 구하기 
    if n % i == 0:
        divisors.append(i)

# print
if k <= len(divisors):
    print(divisors[k-1])
else:
    print(0)