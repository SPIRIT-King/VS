import random
import math

def check_gcd(e,phi_n):
    """
    对随机生成的e进行互素检测

    :prama e:随机生成的e
    :prama phi_n:小于n且与n互素的自然数的个数
    :return: 如果e与phi_n互素，返回True；否则返回False
    """
    if math.gcd(e,phi_n) == 1:
        return True
    else:
        return False

def is_prime(n):
    """
    检测一个数是否为素数

    :param n: 需要检测的数
    :return: 如果n是素数，返回True；否则返回False
    """
    # 如果n小于等于1，则返回False
    if n <= 1:
        return False
    # 如果n小于等于3，则返回True
    if n <= 3:
        return True
    # 如果n能被2或3整除，则返回False
    if n % 2 == 0 or n % 3 == 0:
        return False
    # 初始化i为5
    i = 5
    # 当i的平方小于等于n时，循环
    while i * i <= n:
        # 如果n能被i或i+2整除，则返回False
        if n % i == 0 or n % (i + 2) == 0:
            return False
        # i加6
        i += 6
    # 循环结束后，返回True
    return True

def ext_gcd(a, b): #扩展欧几里得算法    
    """
    计算两个整数a和b的最大公约数g，并找到整数x和y，满足 ax + by = g

    :param a: 第一个整数
    :param b: 第二个整数
    :return: 一个三元组(x, y, gcd)，其中gcd是a和b的最大公约数，x和y是贝祖等式ax + by = g的解
    """
    if b == 0:          
        return 1, 0, a     
    else:         
        x, y, gcd = ext_gcd(b, a % b) #递归直至余数等于0(需多递归一层用来判断)        
        x, y = y, (x - (a // b) * y) #辗转相除法反向推导每层a、b的因子使得gcd(a,b)=ax+by成立         
        return x, y, gcd

def mod_inverse(e, phi_n):
    """
    计算整数e关于模phi_n的模逆元d，即找到一个整数d，使得 (e * d) % phi_n = 1

    :param e: 需要求模逆元的整数
    :param phi_n: 模数，应当是e的互质整数
    :return: 整数e关于模phi_n的模逆元d
    :raises Exception: 如果e和phi_n不互质，则抛出异常，因为不存在模逆元。
    """
    x, y, g = ext_gcd(e, phi_n)
    if g != 1:
        raise Exception('e 和 φ(n) 不互素，无法求模逆元')
    else:
        return x % phi_n

def e_d_gere(p,q):
    """
    基于给定的p和q，生成d

    :param p:给定的素数
    :param q:给定的素数
    :return d:生成的私钥d
    """
    # 使用欧拉公式计算与n互素的自然数的个数
    phi_n = (p-1)*(q-1)
    e_select = []
    for i in range(1,phi_n):
        if check_gcd(i,phi_n) and is_prime(i):
            e_select.append(i)
    # 从e_select中随机选择一个数作为e
    e = random.choice(e_select)
    d = mod_inverse(e, phi_n)
    return e,d

def transferToNum(string):
    """
    将字符转换为十进制数字，并按照n进行分组

    :param string: _description_
    :return: _description_
    """
    print("1.将字符先转换为二进制，之后进行分组转换为十进制：")
    # 将字符串转换为小写
    str_lower = string.lower()
    # 去除字符串中的空格
    str_lower = ''.join(str_lower.split())
    print(">>>去除空格后的字符串：",str_lower)
    # 将字符串转换为列表
    str_list = list(str_lower)
    print(">>>将字符转换为列表：",str_list)
    str_trans = [ord(i)-ord("a")+1 for i in str_list]
    print(">>>将字符转换为十进制数字：",str_trans)
    # 计算每个字符的二进制表示
    str_bin = [bin(i)[2:] for i in str_trans]
    # 计算最大位数
    max_digits = max(len(num) for num in str_bin)
    # 将二进制字符串转换为相同长度的字符串
    str_bin_list = list(map(str, str_bin))
    filled_numbers = [num.zfill(max_digits) for num in str_bin_list]
    print(">>>将二进制字符串转换为相同长度的字符串：",filled_numbers)
    trans_num = "".join(filled_numbers)
    print(">>>将二进制字符串拼接起来：",trans_num)
    return trans_num, max_digits

def grouping(num_bin, n):
    """
    将二进制字符串num_bin按照n进行分组

    :param num_bin: 二进制字符串
    :param n: 其值为p与q的积，用来确定分组的大小
    :return: 分组后的将二进制转换为十进制的列表
    """
    print("2.将二进制字符串按照n进行分组：")
    # 计算分组大小L
    L = int(math.log(n,2))-1
    print(">>>分组大小L：",L)
    # 将二进制字符串按照n进行分组
    num_bin_list = [num_bin[i:i+L] for i in range(0,len(num_bin),L)]
    print(">>>将二进制字符串按照n进行分组：",num_bin_list)
    # 将二进制字符串转换为十进制整数
    num_bin_list_num = [int(i,2) for i in num_bin_list]
    print(">>>将二进制字符串转换为十进制整数：",num_bin_list_num)
    # 将十进制整数转换为字符串
    num_str = list(map(str,num_bin_list_num))
    print(">>>将十进制整数转换为字符串：",num_str)
    return L, num_str

def transferToStr(trans_str,max_digits):
    """
    将二进制字符串trans_str根据max_digits进行分组

    :param trans_str: 需要转换的二进制字符串
    :param max_digits: 分组的大小
    :return: 返回将二进制字符串根据分组大小分组后转换的字符串
    """
    print("3.将二进制字符串根据max_digits进行分组并转换为十进制再转换为字符：")
    # 将二进制字符串根据max_digits进行分组
    trans_numTostr = [trans_str[i:i+max_digits] for i in range(0,len(trans_str),max_digits)]
    print(">>>将二进制字符串根据max_digits进行分组：",trans_numTostr)
    # 将二进制字符串转换为十进制整数
    trans_strTonum = [int(i,2) for i in trans_numTostr]
    print(">>>将二进制字符串转换为十进制整数：",trans_strTonum)
    # 将十进制整数转换为字符
    trans_numToword = [chr(i+ord("a")-1) for i in trans_strTonum]
    print(">>>将十进制整数转换为字符：",trans_numToword)
    # 将字符连接为字符串
    string = "".join(trans_numToword)
    print(">>>将字符连接为字符串：",string)
    return string

def RSA_encrypt(n,m,e):
    """
    使用RSA算法对明文进行加密

    :param n: p与q的乘积
    :param m: 明文
    :param e: 公钥
    :return: L, m_encrypt, max_digits, max_digits_rsa, max_digits_rsa_encrypt
    """
    # 将m中的每个字符转换为二进制
    m_bin, max_digits = transferToNum(m)
    # 对生成的二进制进行分组
    L, m_group = grouping(m_bin, n)
    m_group_int = list(map(int,m_group))
    
    print("3.使用RSA算法对明文进行加密：")
    m_encrypt = [pow(i,e,n) for i in m_group_int]
    m_encrypt_str = list(map(str,m_encrypt))
    max_digits_rsa_encrypt = max(len(i) for i in m_encrypt_str)
    m_encrypt_str_fill = [i.zfill(max_digits_rsa_encrypt) for i in m_encrypt_str]
    print(">>>加密后的密文列表：",m_encrypt_str_fill)
    
    m_encrypt_str = "".join(m_encrypt_str_fill)
    print("···>最后加密的结果为：",m_encrypt_str)
    return L, m_encrypt_str, max_digits, max_digits_rsa_encrypt

def RSA_decrypt(L,m_encrypt,d,n,max_digits,max_digits_rsa_encrypt):
    """
    使用RSA算法对密文进行解密

    :param L: 分组大小
    :param m_encrypt: 密文
    :param d: 私钥
    :param n: p与q的乘积
    :param max_digits: 分组大小
    :param max_digits_rsa_encrypt: 分组大小
    :return: m_decrypt_string
    """
    print("1.使用RSA算法对密文进行解密：")
    m_split = [m_encrypt[i:i+max_digits_rsa_encrypt] for i in range(0,len(m_encrypt),max_digits_rsa_encrypt)]
    print(">>>将加密后的密文拆分为列表：",m_split)
    m_decrypt = [pow(int(i),d,n) for i in m_split]
    print(">>>对加密后的密文进行解密：",m_decrypt)
    print("2.将解密后的数字转化为二进制：")
    m_decrypt_bin = [bin(i)[2:] for i in m_decrypt]
    print(">>>将解密后的数字转化为二进制：",m_decrypt_bin)
    m_decrypt_bin_fill = [i.zfill(L) for i in m_decrypt_bin]
    print(">>>将解密后的二进制填充为相同位数：",m_decrypt_bin_fill)
    m_decrypt_str = "".join(m_decrypt_bin_fill)
    print(">>>将解密后的二进制进行拼接：",m_decrypt_str)
    m_decrypt_string = transferToStr(m_decrypt_str,max_digits)
    return m_decrypt_string
                     



if __name__ == "__main__":
    m = "hello world"
    p = 61
    q = 53
    n = p*q
    e,d = e_d_gere(p,q)
    print(f"参数设置：p={p},q={q},n={n},e={e},d={d},m={m},phi_n={(q-1)*(p-1)}")
    # 使用RSA对m进行加密
    print("一、使用RSA对m进行加密：")
    L, m_encrypt_str, max_digits, max_digits_rsa_encrypt = RSA_encrypt(n,m,e)
    # 对加密后的密文进行解密
    print("二、对加密后的密文进行解密：")
    m_decrypt = RSA_decrypt(L,m_encrypt_str,d,n,max_digits,max_digits_rsa_encrypt)
    print("···>最后解密的结果为：",m_decrypt)
