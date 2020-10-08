import sys

sys.stdin = open(r"C:\Users\my\Desktop\Documents\파이썬 알고리즘 문제풀이(코딩테스트 대비)\섹션 3\5. 수들의 합\in2.txt")
input_list_num, target = list(map(int, input().split()))
input_list = list(map(int, input().split()))
# print(input_list_num, target)
# print(input_list)

def seq_sum(input_list):
    
    total = 0
    left_location = 0
    right_location = 1
    count = 0
    while True:
        
        total = sum(input_list[left_location : right_location])
        if total < target :
            
            if right_location == len(input_list) and input_list[right_location - 1] == target:
                
                count = count + 1
                break
            
            elif right_location == len(input_list) and input_list[right_location - 1] != target:
                
                break
            
            else :
                
                right_location = right_location + 1
        
        elif total == target:
            
            total = 0
            count = count + 1
            left_location = left_location + 1
            
        elif total > target:
            
            total = 0
            left_location = left_location + 1
            if left_location == right_location :
                
                right_location = right_location + 1
        
        if left_location == len(input_list) - 1:
            
            break
            
    print(count)

    
seq_sum(input_list)