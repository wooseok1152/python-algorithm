import sys

sys.stdin = open(r"C:\Users\user\Desktop\Documents\파이썬 알고리즘 문제풀이(코딩테스트 대비)\섹션 5\5. 공주구하기\in1.txt")

length, target = list(map(int, input().split()))
queue = [i for i in range(1, length + 1)]

while True:
    
    for i in range(target-1):
        
        queue.append(queue.pop(0))
    queue.pop(0)
    print(queue)
    if len(queue) == 1:
        
        # print(queue[0])
        break