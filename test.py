'''
후위표기식에선 우선 순위가 높은 연산자를 앞쪽에 배치해야한다.
연산자 우선순위 : 1. 곱하기, 나누기 2. 더하기, 빼기 3. 여는 괄호
연산자와 여는 괄호를 stack에 append하고, 피연산자는 string에 더해간다.
'''

import sys

sys.stdin = open(r"C:\Users\my\Desktop\Documents\파이썬 알고리즘 문제풀이(코딩테스트 대비)\섹션 5\3. 후위표기식 만들기\in1.txt")
input_list = list(input())
def make_postfix(input_list):
    
    result = ""
    stack_for_operator = []
    first_operator = ["*", "/"]
    second_operator = ["+", "-"]
    flag = 0
    for i in input_list:
        
        if i != "+" and i != "-" and i != "*" and i != "/" and i !="(" and i !=")":
            
            result = result + i
            
        else:

            if len(stack_for_operator) == 0:

                stack_for_operator.append(i)
                if i == "(":
                    
                    flag = 1

            else:
                
                if flag == 0:
                    
                    if i in second_operator:

                        for j in range(len(stack_for_operator)):

                            result = result + stack_for_operator.pop()

                        stack_for_operator.append(i)

                    elif i in first_operator:

                        while stack_for_operator[-1] in first_operator:

                            result = result + stack_for_operator.pop()

                        stack_for_operator.append(i)
                        
                    elif i == "(":
                        
                        stack_for_operator.append(i)
                        flag = 1
                        
                elif flag == 1:
                    
                    if i in second_operator:
                        
                        while stack_for_operator[-1] != "(":
                        
                            result = result + stack_for_operator.pop()
                        
                        stack_for_operator.append(i)
                        
                    elif i in first_operator:
                        
                        stack_for_operator.append(i)
                        
                    if i == ")":
                        
                        while stack_for_operator[-1] != "(":
                            
                            result = result + stack_for_operator.pop()
                        
                        if stack_for_operator[-1] == "(":
                            
                            stack_for_operator.pop()
                            flag = 0
        
    for i in range(len(stack_for_operator)):
        
        result = result + stack_for_operator.pop()
        
    print(result)
    
make_postfix(input_list)
