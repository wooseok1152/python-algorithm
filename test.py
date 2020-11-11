import sys

sys.stdin = open(r"C:\Users\my\Desktop\Documents\파이썬 알고리즘 문제풀이(코딩테스트 대비)\섹션 6\5. 바둑이 승차\in1.txt")

def dfs(level, level_sum):
    
    global check_dog
    global input_list
    global max_weight
    global target
    
    if level_sum > max_weight : 
        
        return
    if level == len(input_list):
        
        if level_sum <= max_weight and level_sum >= target:
            
            target = level_sum
        return
    check_dog[level] = 1
    level_sum = level_sum + input_list[level]
    print(check_dog, level_sum)
    dfs(level + 1, level_sum)
    check_dog[level] = 0
    level_sum = level_sum - input_list[level]
    print(check_dog, level_sum)
    dfs(level + 1, level_sum)

    
max_weight, dog_count = list(map(int, input().split()))
input_list = [int(input()) for i in range(dog_count)]
check_dog = {}
target = 0
for i in range(len(input_list)):
    
    check_dog[i] = 0
print(check_dog, "\n")
dfs(0, 0)
print("\n",target)