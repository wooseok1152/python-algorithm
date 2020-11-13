'''1회 복습'''
'''연산자가 stack에 들어가고, 피연산자가 문자열에 합해진 다는 것을 명심하자'''

import sys

sys.stdin = open(r"C:\Users\user\Desktop\Documents\파이썬 알고리즘 문제풀이(코딩테스트 대비)\섹션 5\3. 후위표기식 만들기\in3.txt")

input_list = list(input())
result = ""
stack = []
conductor = ["+", "-", "*", "/", "(", ")"]
# print(input_list)
while True:
    
    if len(input_list) == 0:
        
        for i in range(len(stack)):
            
            result = result + stack.pop()
        print(result)
        break
    else:
        
        target = input_list.pop(0)
        if target not in conductor:
            
            result = result + target
        else:
            
            if len(stack) == 0:
                
                stack.append(target)
            elif target == "(":
                
                stack.append(target)
            elif stack[-1] == "(":
                
                stack.append(target)
            elif (target == "+" or target == "-") and (stack[-1] == "+" or stack[-1] == "-" or stack[-1] == "*" or stack[-1] == "/"):
                
                result = result + stack.pop()
                stack.append(target)
            elif (target == "*" or target == "/") and (stack[-1] == "+" or stack[-1] == "-"):
                
                stack.append(target)
            elif (target == "*" or target == "/") and (stack[-1] == "*" or stack[-1] == "/"):
                
                result = result + stack.pop()
                stack.append(target)
            elif target == ")":
                
                while True:
                    
                    if stack[-1] != "(":
                        
                        result = result + stack.pop()
                    else:
                        
                        stack.pop()
                        break