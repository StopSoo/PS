# https://www.acmicpc.net/problem/1541

# 내 답안 (but 완성되지 않음. 시간이 너무 오래 걸렸고, 경우의 수도 너무 많아서 풀이가 잘못됐다고 생각이 듬.)
equation = input()
count_op_m = equation.count('-')
count_op_p = equation.count('+')
count_num = (count_op_m + count_op_p) + 1

if count_op_m == 0 and count_op_p != 0: # + 기호만 있을 때
  print(eval(equation))
elif count_op_m != 0 and count_op_p == 0: # - 기호만 있을 때
  ind_op_m = equation.index("-")
  next_ind_op_m = equation[ind_op_m+1:].find("-")
  if next_ind_op_m == -1: # - 기호가 1개일 때
    equation = equation[:ind_op_m] + '-' + '(' + equation[ind_op_m+1:] + ')'
    print(eval(equation))
  else: print(eval(equation))
else: # +, - 둘 다 있을 때
  ind_op_m = equation.index("-")
  ind_op_p = equation[ind_op_m+1:].find("+") + len(equation[:ind_op_m+1])
  next_op_m = equation[ind_op_p+1:].find('-')
  next_op_p = equation[ind_op_p+1:].find('+')
  print(ind_op_m, ind_op_p, next_op_m, next_op_p)
  if min(next_op_m, next_op_p) != -1: next_op_ind = min(next_op_m + len(equation[:ind_op_m+1]) + len(equation[ind_op_m+1:ind_op_p+1]), next_op_p + len(equation[:ind_op_m+1]) + len(equation[ind_op_m+1:ind_op_p+1]))
  elif next_op_m == -1 and next_op_p == -1: next_op_ind = -1
  elif next_op_m == -1: 
    next_op_ind = next_op_p + len(equation[:ind_op_m+1]) + len(equation[ind_op_m+1:ind_op_p+1])
  elif next_op_p == -1: 
    next_op_ind = next_op_m + len(equation[:ind_op_m+1]) + len(equation[ind_op_m+1:ind_op_p+1])
  
  if next_op_ind == -1:
    equation = equation[:ind_op_m] + '-' + '(' + equation[ind_op_m+1:ind_op_p] + '+' + equation[ind_op_p+1:] + ')'
    print(equation)
    print(eval(equation))
  else: # -, + 후에 연산자가 있다면
    equation = equation[:ind_op_m] + '-' + '(' + equation[ind_op_m+1:ind_op_p] + '+' + equation[ind_op_p+1:next_op_ind] + ')' + equation[next_op_ind:]
    print(equation)
    print(eval(equation))
