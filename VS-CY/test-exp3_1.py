import math
"""string = "abcdefg"
str_lower = string.lower()
str_list = list(str_lower)
str_trans = [ord(i)-ord("a")+1 for i in str_list]
print(str_trans)
str_bin = [bin(i)[2:] for i in str_trans]
max_digits = max(len(num) for num in str_bin)
str_bin_list = list(map(str, str_bin))
print(str_bin_list)
filled_numbers = [num.zfill(max_digits) for num in str_bin_list]
trans_str = "".join(filled_numbers)
trans_num = int(trans_str)
print(filled_numbers)
print(type(trans_num))"""


"""max_digits = 3
trans_str = "001010011100101110111"
trans_numTostr = [trans_str[i:i+max_digits] for i in range(0,len(trans_str),max_digits)]
print(trans_numTostr)
trans_strTonum = [int(i,2) for i in trans_numTostr]
print(trans_strTonum)
trans_numToword = [chr(i+ord("a")-1) for i in trans_strTonum]
print(trans_numToword)
string = "".join(trans_numToword)
print(string)"""

"""num_bin = "001010011100101110111"
n = 1023
L = int(math.log(n,2))-1
num_bin_list = [num_bin[i:i+L] for i in range(0,len(num_bin),L)]
num_bin_list_num = [int(i,2) for i in num_bin_list]
num_str = list(map(str,num_bin_list_num))
max_digits_rsa = max(len(i) for i in num_str)
num_str_fill = [i.zfill(max_digits_rsa) for i in num_str]
m_group_int = list(map(int,num_str_fill))
print(m_group_int)"""

def extended_gcd(a, b):
    """
    计算两个整数a和b的最大公约数g，并找到整数x和y，满足 ax + by = g

    :param a: 第一个整数
    :param b: 第二个整数
    :return: 一个三元组(g, x, y)，其中g是a和b的最大公约数，x和y是贝祖等式ax + by = g的解
    """
    if a == 0:
        return b, 1, 0
    else:
        g, y, x = extended_gcd(b % a, a)
        return g, x - (b // a) * y, y

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
    print("x=",x,"y=",y,"g=",g)
    print("x % phi_n=",x% phi_n,"y % phi_n=",y% phi_n)
    if g != 1:
        raise Exception('e 和 φ(n) 不互素，无法求模逆元')
    else:
        return x % phi_n




phi_n =3120
e=2003
d_inv = mod_inverse(e, phi_n)
d=1067

result = (e*d)%phi_n
print("d_inv=",d_inv)
print(result)


