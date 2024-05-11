import numpy as np
pred_keyword="1110100111"
pred_keyword_list = [int(keyword) for keyword in list(pred_keyword)]
pred_keyword_list_used = pred_keyword_list[:6]
level=3
K = []
for i in range(level):
    K.append(pred_keyword_list_used[i:level+i])
K = np.array(K)
K_inv = np.linalg.inv(K)
k_list = pred_keyword_list_used[-3:]
result = np.dot( k_list,K_inv)%2
result = [int(result[i]) for i in range(len(result))]
for i in range(len(result)):
    if result[i] == 1.:
        if i == 0.:
            result[i] = "a_i"
        else:
            result[i] = "a_{i+"+str(i)+"}"

result = [i for i in result if i!= 0 ]
next_var = "a_{i+"+str(level)+"}"
Iterative_expression = next_var+"⊕".join(result)
print(K)
print(K_inv%2)
print(k_list)
print(np.dot( k_list,K_inv)%2)
print(result)
print(Iterative_expression)
