'''1회 복습'''

import sys

sys.stdin = open(r"C:\Users\user\Desktop\Documents\파이썬 알고리즘 문제풀이(코딩테스트 대비)\섹션 4\2. 랜선자르기\in1.txt")

input_count, target = list(map(int, input().split()))
input_list = [int(input()) for i in range(input_count)]
min_value = 1
max_value = max(input_list)
mid_value = (min_value + max_value)//2

while True:
    
    if min_value > max_value:
        
        break
    count = 0
    for i in input_list:
        
        divided_result = i//mid_value
        count = count + divided_result
    if count < target:
        
        max_value = mid_value - 1
        mid_value = (min_value + max_value)//2
        
    else:
        
        min_value = mid_value + 1
        mid_value = (min_value + max_value)//2
    
print(mid_value)