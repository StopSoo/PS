# 11718 : 그대로 출력하기 

while True:
    try:
        word = input()
        if word == "":
            break
        print(word)
    except:
        break

# 입력의 끝을 나타내기 위해 EOF를 사용한다.
# 파이썬에서는 EOF를 입력으로 받으려고 하면 EOFerror가 발생해서 try ~ except문을 꼭 사용해야 한다. 