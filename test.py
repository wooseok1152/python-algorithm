import sys

sys.stdin = open(r"C:\Users\my\Desktop\Documents\파이썬 알고리즘 문제풀이(코딩테스트 대비)\섹션 5\5. 공주구하기\in3.txt")
n, k = list(map(int, input().split()))

input_list = list(range(1, n + 1))

def save_princess(input_list, k):
    
    while True:
        
        if len(input_list) >= k:
            
            input_list.pop(k-1)
            for i in range(k-1):
                
                input_list.append(input_list.pop(0))
            
        else:
            
            if k % 2 == 0:
                
                result = input_list[1]
                print(result)
                break
            
            else:
                
                result = input_list[-1]
                print(result)
                break
            
save_princess(input_list, k)