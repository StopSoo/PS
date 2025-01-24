# https://school.programmers.co.kr/learn/courses/30/lessons/181874

# 내 답안
# replace: 변경된 값을 반환, 고로 다시 해당 변수에 값을 넣어줘야 함
def solution(myString):
    result = myString
    for x in result:
        if x.isupper(): 
            result = result.replace(x, x.lower())
    result = result.replace('a', 'A')
    return result

# 간결한 답안
def solution(myString):
  return myString.lower().replace('a', 'A')