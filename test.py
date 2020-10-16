'''
큐, 스택 자료구조를 활용할 때 핵심은 해당 자료구조 내 원소를 하나씩 빼고 추가한다는 것이다.
두 개 이상의 요소를 한 번에 빼거나 넣으면, 정확한 답을 구하기 힘들어진다.
'''

import sys

sys.stdin = open(r"C:\Users\my\Desktop\Documents\파이썬 알고리즘 문제풀이(코딩테스트 대비)\섹션 5\5. 공주구하기\in1.txt")
n, k = list(map(int, input().split()))

input_list = list(range(1, n + 1))

def save_princess(input_list, k):
    
    while True:
        
        for i in range(k-1):
            
            picked = input_list.pop(0)
            input_list.append(picked)
        
        input_list.pop(0)
        if len(input_list) == 1:
            
            result = input_list[-1]
            break
    
    print(result)
    
save_princess(input_list, k)