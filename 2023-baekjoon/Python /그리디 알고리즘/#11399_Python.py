#11399

n = int(input())    # 사람의 수
time_per_person = list(map(int, input().split()))   # 각 사람이 필요한 시간
time_acc = [0] * n  # 누적 시간 

def insertion_sort(array):  # 삽입 정렬 
    for end in range(1, len(array)):
        i = end
        while i > 0 and array[i-1] > array[i]:
            array[i-1], array[i] = array[i], array[i-1]
            i -= 1
    return array

time_per_person = insertion_sort(time_per_person)   # sorting

for i in range(0, n):  # 시간 합 계산
    for j in range(0, i+1):
        time_acc[i] += time_per_person[j]

total = 0
i = 0
while (i < len(time_acc)):  # 시간의 합 최솟갑 계산하기 
    total += time_acc[i]
    i += 1 

print(total)

# 제어 변수 초기화랑 설정 잘 하기 