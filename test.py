import sys

sys.stdin = open(r"C:\Users\my\Desktop\Documents\파이썬 알고리즘 문제풀이(코딩테스트 대비)\섹션 5\9. 아나그램(구글)\in1.txt")

input_list = [input() for i in range(2)]
# print(input_list)

first = list(input_list[0])
second = list(input_list[1])

first_set = list(set(first))
second_set = list(set(second))

first_dict = {}
second_dict = {}

for i in first_set:
    
    count = first.count(i)
    first_dict[i] = count
    
for i in second_set:
    
    count = second.count(i)
    second_dict[i] = count
    
if first_dict == second_dict :

    print("YES")
    
else :
    
    print("NO")