import sys

sys.stdin = open(r"C:\Users\user\Desktop\Documents\파이썬 알고리즘 문제풀이(코딩테스트 대비)\섹션 6\1. 재귀함수란(이진수출력)\in1.txt")
input_int = int(input()) 
result = ""

def two(input_int):
    
    global result
    if input_int == 1:
        
        left = input_int%2
        result = result + str(left)
        return
    
    moak = input_int//2
    left = input_int%2
    two(moak)
    result = result + str(left)
    
two(input_int)
print(result)