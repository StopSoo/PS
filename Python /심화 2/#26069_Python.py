# 26069
import sys
input = sys.stdin.readline

N = int(input())    # 사람들이 만난 기록의 수 
persons = set(['ChongChong'])    # 무지개 댄스 유무 구분 리스트를 집합으로 형 변환 -> 중복X

for i in range(N):
    person1, person2 = input().split()  # 사람 두 명 입력 받기
    # 총총을 만났을 때 + 총총에게 전염된 사람을 만났을 때
    if person1 in persons:
        persons.add(person2)
    elif person2 in persons:
        persons.add(person1)

print(len(persons))

# 중복 제거 -> 문자열을 집합으로 하면 안됨. 문자열이 담긴 리스트를 집합으로 해야함 ! 