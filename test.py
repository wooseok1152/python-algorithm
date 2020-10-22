import sys

sys.stdin = open(r"C:\Users\user\Desktop\Documents\파이썬 알고리즘 문제풀이(코딩테스트 대비)\섹션 5\6. 응급실\in1.txt")
n, target = list(map(int, input().split()))
input_list = list(map(int, input().split()))
input_list = [(i, j) for i, j in enumerate(input_list)]

def emergency_room(input_list):
    
    count = 0
    while True:
        
        values_list=  []
        for i in input_list:
            
            values_list.append(i[1])
        biggest_value = max(values_list)
        if input_list[0][1] == biggest_value:
            
            if input_list[0][0] == target:
                
                print(count + 1)
                break
            input_list.pop(0)
            count = count + 1
            
        else :
            
            input_list.append(input_list.pop(0))
        

emergency_room(input_list)