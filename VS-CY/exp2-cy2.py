import numpy as np
def LFSR_vig(pred_keyword, level):
    """
    根据推测出的密钥序列和线性反馈以为寄存器的级数，推算线性以为寄存器的递推关系式
    :param pred_keyword:推测的密钥序列
    :param level:线性移位寄存器的级数
    :return 递推关系的系数
    """
    pred_keyword_list = [int(keyword) for keyword in list(pred_keyword)]
    pred_keyword_list_used = pred_keyword_list[:2*level]
    # 构造矩阵
    K = []
    for i in range(level):
        K.append(pred_keyword_list_used[i:level+i])
    K = np.array(K)
    K_inv = np.linalg.inv(K)%2 #求K的逆矩阵
    k_list = pred_keyword_list_used[-3:]
    k_list = np.array(k_list)
    result = np.dot( k_list,K_inv)%2
    result = [int(result[i]) for i in range(len(result))]
    for i in range(len(result)):
        if result[i] == 1.:
            if i == 0.:
                result[i] = "a_i"
            else:
                result[i] = "a_{i+"+str(i)+"}"
    result = [i for i in result if i!= 0 ]
    next_var = "a_{i+"+str(level)+"}="
    Iterative_expression = next_var+"⊕".join(result)
    return K_inv,result,Iterative_expression


if __name__ == "__main__":
    pred_keyword = "1110100111"
    level=3
    k_inv,result,Iterative_expression = LFSR_vig(pred_keyword, level)
    print(f"K的逆矩阵为：\n{k_inv}\n线性反馈移位寄存器级数：{level},线性移位寄存器的系数：{result}")
    print("输出序列的递推公式：",Iterative_expression)
    


    