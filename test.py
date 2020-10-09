import sys

sys.stdin = open(r"C:\Users\my\Desktop\Documents\파이썬 알고리즘 문제풀이(코딩테스트 대비)\섹션 5\2. 쇠막대기\in1.txt")
input_list = list(input())

def iron_stick(input_list) :
    
    count = 0
    stack = []
    for i, j in enumerate(input_list):
        
        if j == "(":
            
            stack.append(j)
        
        else :
            
            if input_list[i-1] == "(":
                
                stack.pop()
                count  = count + len(stack)
                
            else :
                
                stack.pop()
                count = count + 1
                
    print(count)
    
iron_stick(input_list)