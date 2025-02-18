# https://www.acmicpc.net/problem/28702

# 내 답안
# 걸린 시간: 36ms
# 처음에 풀면서 이렇게 노가다로 푸는 게 맞나 ,,? 했는데 다른 사람들 답안 보니까 맞는 듯
# 문자열.isdigit(): 문자열이 숫자인지 여부를 반환
numbers = [0, 0, 0]
words = [input() for _ in range(3)]
for i, word in enumerate(words):
  if word.isdigit(): numbers[i] = int(word)
for i, num in enumerate(numbers):
  if num != 0:
    answer = num + (3-i)
    if answer%3==0 and answer%5==0: print("FizzBuzz")
    elif answer%3==0 and answer%5!=0: print("Fizz")
    elif answer%3!=0 and answer%5==0: print("Buzz")
    else: print(answer)
    break