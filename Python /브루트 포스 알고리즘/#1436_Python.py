# 1436 : 영화감독 숌

N = int(input())    # 사용자로부터 입력 받는 수

# 초기화
number = 666
count = 1

# 종말의 수가 들어있는지 체크하는 함수
def check_six(number):
    number_str = str(number)    # 숫자를 문자열로 변환
    for i in range(0, len(number_str)-2):
        if number_str[i] == number_str[i+1] == number_str[i+2] == '6':  # 종말의 수라면
            return True
        else:
            continue
    return False

while True:
    if count == N:  # N번째 수가 되면 출력
        print(number)
        break

    number += 1 # 다음 수로 이동
    if check_six(number) == True: # 종말의 수라면
        count += 1
    else:   # 종말의 수가 아니라면
        continue