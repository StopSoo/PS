# https://school.programmers.co.kr/learn/courses/30/lessons/81301?language=python3

# 내 답안
def solution(s):
    answer = ''
    num_dict = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    for i, ch in enumerate(s):
        if ch.isdigit(): answer += ch
        else: 
            for num in num_dict:
                if s[i:i+len(num)] == num: 
                    answer += num_dict[num]
                    break
    return int(answer)

# 배우고 싶은 간단한 풀이
# 항상 생각하는 거지만 replace를 잘 활용하자!
num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def solution(s):
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)