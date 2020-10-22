import sys

sys.stdin = open(r"C:\Users\user\Desktop\Documents\파이썬 알고리즘 문제풀이(코딩테스트 대비)\섹션 5\8. 단어찾기\in1.txt")

n = int(input())
queue = sorted([input() for i in range(n)])
wroten_list = sorted([input() for i in range(n-1)])

for i in wroten_list:
    
    target = queue.pop(0)
    if i != target:
        
        print(target)
        break
