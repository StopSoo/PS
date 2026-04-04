# https://school.programmers.co.kr/learn/courses/30/lessons/67256
# 260404 풀이

def solution(numbers, hand):
    answer = ''
    pos = {1: [0, 0], 2: [0, 1], 3: [0, 2], 4: [1, 0], 5: [1, 1], 6: [1, 2], 7: [2, 0], 8: [2, 1], 9: [2, 2], 0: [3, 1]}
    left_y, left_x = 3, 0
    right_y, right_x = 3, 2
    
    for number in numbers:
        if number in [1, 4, 7]:
            answer += 'L'
            left_y, left_x = pos[number]
        elif number in [3, 6, 9]:
            answer += 'R'
            right_y, right_x = pos[number]
        else:
            l_dist = abs(pos[number][0] - left_y) + abs(pos[number][1] - left_x)
            r_dist = abs(pos[number][0] - right_y) + abs(pos[number][1] - right_x)
            if (l_dist == r_dist and hand == "right") or l_dist > r_dist:
                answer += 'R'
                right_y, right_x = pos[number]
            elif (l_dist == r_dist and hand == "left") or l_dist < r_dist:
                answer += 'L'
                left_y, left_x = pos[number]     
    
    return answer