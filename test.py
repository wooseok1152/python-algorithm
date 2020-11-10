import sys

sys.stdin = open(r"C:\Users\user\Desktop\Documents\파이썬 알고리즘 문제풀이(코딩테스트 대비)\섹션 6\5. 바둑이 승차\in1.txt")

def dfs(index):
    
    global check_dog
    global input_list
    global result_weights
    global max_weight
    
    if index == len(input_list):
        
        weight_sum = 0
        for i in range(len(input_list)):
            
            if check_dog[i] == 1:
                
                weight_sum = weight_sum + input_list[i]
        if weight_sum <= max_weight:
            
            result_weights.append(weight_sum)
        return
    check_dog[index] = 1
    dfs(index + 1)
    check_dog[index] = 0
    dfs(index + 1)

max_weight, dog_count = list(map(int, input().split()))
input_list = [int(input()) for i in range(dog_count)]
check_dog = {}
result_weights = []
for i in range(len(input_list)):
    
    check_dog[i] = 0
dfs(0)
print(max(sorted(result_weights)))
