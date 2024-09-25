# 11660_Python

size, count = input().split(" ")    # 표의 크기, 합을 구해야 하는 횟수 입력 


array = []  # 표
for i in range(int(size)):
    value = input()                 # 한 행 입력
    array.append(value.split(" "))  # split 하면 리스트를 반환 

for i in range(int(count)):
    value = input()                 # 합을 구할 시작 위치와 끝 위치 입력
    x1, y1, x2, y2 = value.split(" ")
    
    sum = 0
    for j in range(int(x1)-1, int(x2)):
        for k in range(int(y1)-1, int(y2)):
            sum += int(array[j][k])
    print(sum)

# Question 1) split해서 리스트로 반환되면 원소들을 바로 int로 바꿀 수는 없는지 ..?
# Answer 1) map 함수를 사용하여 해결할 수 있다 ! --> map(int, input().split())

# Question 2) Ex> for _ in range(3): --> 반복 변수를 사용하지 않으면서 반복