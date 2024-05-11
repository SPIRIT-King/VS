def F(input_seq):
    """
    定义线性反馈寄存器中的运算
    :param input_seq:输入序列
    :return result:返回运算结果 
    """
    return (1*input_seq[0])^(1*input_seq[-1])


def LFSR(input_seq, level, F, rounds):
    """
    定义level级的线性反馈寄存器
    :param input_seq:输入序列
    :param level:线性反馈寄存器的级数
    :return:输出的返回序列
    """
    input_len = len(input_seq) #获取输入序列的长度
    if input_len != level:
        print("输入序列长度与线性反馈寄存器级数不匹配，无法计算")
        return 0
    print(f"初始状态：{''.join(map(str,input_seq))}")
    inital_seq = input_seq.copy()
    flag = 1
    Return = []
    for i in range(rounds):
        result = F(input_seq)
        input_seq.append(result)
        Return.append(input_seq.pop(0))
        print(f"第{i+1}轮：{''.join(map(str,input_seq))}，输出为{Return[i]}")
        if inital_seq == input_seq and flag == 1 and i!=0:
            period = i+1
            flag-=1
    print(f"周期为：{period}")
    return Return

if __name__ == "__main__":
    input_seq=[1,0,0,1]
    rounds = 20
    output_seq=LFSR(input_seq, 4, F, rounds)
    print(f"输出序列为{''.join(map(str,output_seq))}")