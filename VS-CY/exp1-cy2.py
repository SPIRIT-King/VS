import math
def find_sub_loc(ciphertext,subtext):
    """
    找到规定密文中subtext出现的位置
    :param ciphertext: 密文
    :param subtext:子串
    :return sub_loc_arr:存储着子串在给定的密文中出现的所有位置的索引
    """
    start = 0
    end = len(ciphertext)
    sub_loc_arr = []
    sub_loc_index = 0
    while True:
        try:
            sub_loc = ciphertext.index(subtext,start,end)
        except ValueError:
            break
        sub_loc_arr.append(sub_loc)
        start = sub_loc_arr[sub_loc_index]+len(subtext)
        sub_loc_index+=1
    return sub_loc_arr

def trans_relative_loc(sub_loc_arr):
    """
    将子串的位置转换成相对于第一个子串位置的相对位置
    :paras sub_loc_arr:存储着子串出现的所有位置的索引
    :return trans_relative_loc_arr:返回转换后的子串的相对位置
    """
    first_sub_loc = sub_loc_arr[0]
    counts = len(sub_loc_arr)-1
    trans_relative_loc_arr = []
    for i in range(counts):
        trans_relative_loc_arr.append(sub_loc_arr[i+1]-first_sub_loc)
    return trans_relative_loc_arr

def sub_loc_gcd(sub_loc_arr):
    """
    返回子串位置的最大公因数
    :param sub_loc_arr:存储着子串出现的所有位置的索引
    :return subtext_gcd:所有位置的最大公因数
    """
    iters = len(sub_loc_arr)
    subtext_gcd = math.gcd(sub_loc_arr[0],sub_loc_arr[1])
    for i in range(iters-2):
        subtext_gcd = math.gcd(sub_loc_arr[i+2],subtext_gcd)
    return subtext_gcd

def IC_ciphertext(ciphertext,exp_max_length):
    """
    分别计算密钥长度为1～exp_max_length对应密文子串的IC值和平均IC值
    :param ciphertext:给定的密文
    :param exp_max_length:给定的最大的密文的长度
    """
    trans_list_str = list(ciphertext)
    keylength=1
    save_result=[]
    while keylength<exp_max_length+1:
        IC = 0
        print(f"当密钥长度为{keylength}时",end='')

        for i in range(keylength):
            Numerator = 0
            div_arr = trans_list_str[i::keylength]
            L = len(div_arr)
            for letter in set(div_arr):
                letter_count = div_arr.count(letter)
                Numerator += letter_count * (letter_count-1)
            IC += Numerator/(L * (L-1))
            print(f" IC(子串{i+1})={IC:.4f}",end='')

        Average=IC / keylength
        print(f" avg={Average:.4f}")
        if abs(Average-0.065)<0.003:
            save_result.append((keylength,Average))

        keylength += 1
    return save_result

def keyword(ciphertext,keylength):
    """
    通过给定的密文和密钥长度，使用拟重合指数法确定密钥
    :param ciphertext:给定的密文
    :param keylength:由前面得出的密钥长度
    :return Key:通过拟重合指数法得出密文
    """
    trans_list_str = list(ciphertext)
    statis_standard = {'A':0.082,'B':0.015,'C':0.028,'D':0.043,'E':0.127,'F':0.022,'G':0.020,'H':0.061,'I':0.070,'J':0.002,'K':0.008,'L':0.040,'M':0.024,'N':0.067,'O':0.075,'P':0.019,'Q':0.001,'R':0.060,'S':0.063,'T':0.091,'U':0.028,'V':0.010,'W':0.023,'X':0.001,'Y':0.020,'Z':0.001}

    while True:
        key_result = []

        for i in range(keylength):
            print(f">>>查找第{i+1}个密钥字母<<<")
            div_arr = trans_list_str[i::keylength]
            QC_Max = 0
            keyletter = ""

            for m in range(26):
                QC = 0

                for letter in set(div_arr):
                    P_letter = div_arr.count(letter) / len(div_arr)
                    k = chr((ord(letter)-65-m)%26+65)
                    P_standard = statis_standard[k]
                    QC = QC + P_letter * P_standard
                
                print(f"QC(i={chr(m+65)})={QC:.4f} ",end="")
                if QC > QC_Max:
                    QC_Max = QC
                    keyletter = chr(m+65)
            print(f"\n>>第{i+1}个密钥字母为:{keyletter},对应的重合互指数为:{QC_Max:.4f}")
            key_result.append(keyletter)
        Key = "".join(key_result)
        break
    return Key

def vigenere_decrypt(ciphertext, key):  
    """  
    使用维吉尼亚密码，使用给定的密钥对给定的密文进行解密，生成解密之后的明文  
  
    :param ciphertext: 给定的密文  
    :param key: 给定的密钥  
    :return plaintext: 使用维吉尼亚密码解密后的明文  
    """  
    plaintext = ""  
    key_index = 0  
      
    for char in ciphertext:  
        char = char.upper()  
        key_char = key[key_index % len(key)].upper()  # 确保key_index不会超出密钥长度  
          
        # 解密操作是加密操作的逆过程  
        decrypted_value = (ord(char) - ord('A') - (ord(key_char) - ord('A'))) % 26  
        decrypted_char = chr(decrypted_value + ord('A'))  
          
        plaintext += decrypted_char  
          
        key_index += 1  
          
    return plaintext.lower() 
    


ciphertext = "CHREEVOAHMAERATBIAXXWTNXBEEOPHBSBQMQEQERBWRVXUOAKXAOSXXWEAHBWGJMMQMNKGRFVGXWTRZXWIAKLXFPSKAUTEMNDCMGTSXMXBTUIADNGMGPSRELXNJELXVRVPRTULHDNQWTWDTYGBPHXTFALJHASVBFXNGLLCHRZBWELEKMSJIKNBHWRJGNMGJSGLXFEYPHAGNRBIEQJTAMRVLCRREMNDGLXRRIMGNSNRWCHRQHAEYEVTAQEBBIPEEWEVKAKOEWADREMXMTBHHCHRTKDNVRZCHRCLQOHPWQAIIWXNRMGWOIIFKEE"
subtext = "CHR"
print("第一步：使用Kasiski测试确定密钥长度")
sub_loc_arr = find_sub_loc(ciphertext,subtext) #找到所有子串在密文中出现的位置
print("1.查找的子串位置的索引数组为：",sub_loc_arr)
trans_relative_loc_arr = trans_relative_loc(sub_loc_arr) #将将索引位置转换为相对于第一次出现位置的数组
print("2.将索引位置转换为相对于第一次出现位置的数组为：",trans_relative_loc_arr)
subtext_gcd = sub_loc_gcd(sub_loc_arr) #求出子串出现的所有位置的最大公因数
print("3.第一次出现到其他各次出现的距离的最大公因数为：",subtext_gcd)
print(">>>故由Kasiski测试法可知密钥字的长度可能是：",subtext_gcd)
print("4.下面使用重合指数法验证结论的正确性：")
save_result = IC_ciphertext(ciphertext,10)
keylength = save_result[0][0]
print(">>>保存的结果为：",save_result)
print(">>>所以推测的密钥的长度为：",keylength)
print("第二步：使用拟重合指数法确定密钥字")
keyword = keyword(ciphertext,keylength)
print(">>>推测的密钥为：",keyword)
plaintext = vigenere_decrypt(ciphertext, keyword)  
print(f"解密后的明文: {plaintext}")

