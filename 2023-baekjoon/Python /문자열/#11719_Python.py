# 11719 : 그대로 출력하기 2

while True:
    try:
        word = input()
        print(word)
    except: # EOF
        break

# (!) sys.stdin.readline이 안되는 이유
# input()은 EOF를 받을 때 EOFError를 일으키지만 
# sys.stdin.readline은 EOF를 받을 때 빈 문자열을 리턴하기 때문에 오류가 발생하지 않고 틀리게 된다. 