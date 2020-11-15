input_list = [1,4,2,6,5,3, 8, 9]
memo = [0] * (len(input_list) + 1)
input_list.insert(0, 0)
memo[0] = [0]
memo[1] = [[input_list[1]]]
print("input_list :", input_list, len(input_list))
print("memo :", memo,len(memo), "\n")


for i in range(2, len(input_list)):
    
    picked_max = 0
    result = []
    target = input_list[i]
    max_length = 0
    for j in range(i - 1, 0, -1):
        
        for l in range(len(memo[j])):
            
            if target > memo[j][l][-1]:
                
                picked = memo[j][l][:]
                picked.append(target)
                if len(picked) > max_length:
                    
                    max_length = len(picked)
                if len(picked) == max_length:
                    
                    result.append(picked)
    #         if memo[j][k][-1] > picked_max:
                    
    #             picked_max = memo[j][k][-1]
    # if target > picked_max:
        
        # result.append([target])
    memo[i] = result

print(memo)
memo[0] = [[0]]
final_max_len = len(memo[-1][0])
final_result = []
print(final_max_len)
for i in memo:
    
    if len(i[0]) == final_max_len:
        
        for j in range(len(i)):
            
            final_result.append(i[j])
            
print("final_result :", final_result, "\n")

real_final_result = sorted(final_result, key=lambda x: [x[i] for i in range(final_max_len)])
print(real_final_result)



        