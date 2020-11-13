import sys

sys.stdin = open(r"C:\Users\my\Desktop\Documents\파이썬 알고리즘 문제풀이(코딩테스트 대비)\섹션 8\1, 2. 네트워크 선 자르기")

def dfs(level):
    
    if memo_for_result[level] != 0:
        
        return memo_for_result[level]
    if level == 1 or level == 2:
        
        memo_for_result[level] = level
        return level
    else:
        
        memo_for_result[level] = dfs(level - 1) + dfs(level - 2)
        return memo_for_result[level]
    
input_value = int(input())
memo_for_result = [0] * (input_value + 1)
dfs(input_value)
print(memo_for_result[input_value])
