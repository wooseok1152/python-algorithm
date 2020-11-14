import sys

sys.stdin = open(r"C:\Users\my\Desktop\Documents\파이썬 알고리즘 문제풀이(코딩테스트 대비)\섹션 8\6. 가장 높은 탑 쌓기(LIS 응용)\in1.txt")

input_count = int(input())
input_list = [tuple(list(map(int, input().split()))) for i in range(input_count)]
input_list.insert(0, (0,0,0))
memo = [0] * len(input_list)
memo[1] = input_list[1]
# print("input_list :", input_list, len(input_list))
# print("memo :", memo, len(memo), "\n")

for i in range(2, len(input_list)):
    
    max_ = (0, 0, 0)
    target = input_list[i]
    for j in range(i - 1, 0, -1):
        
        if target[0] < memo[j][0] and target[2] < memo[j][2]:
            
            candidate = (target[0], target[1] + memo[j][1], target[2])
            if candidate[1] > max_[1]:
                
                max_ = candidate
        else:
            
            if target[1] > memo[j][1] :
                
                candidate = target
                if candidate[1] > max_[1]:
                
                    max_ = candidate
            else:
                
                candidate = memo[j]
                if candidate[1] > max_[1]:
                
                    max_ = candidate  
    memo[i] = max_
memo[0] = (0, 0, 0)
# print(memo)
result = []
for i in memo:
    
    result.append(i[1])
# print(result)
print(max(result))