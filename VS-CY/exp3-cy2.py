# _*_ coding:utf-8 _*_
import math


def fermat(n):
    # 计算n的平方根，返回一个整数对
    # a为第一个数，b为第二个数
    a = math.ceil(math.sqrt(n))
    # b的平方
    b2 = a * a - n
    b = round(math.sqrt(b2))
    while b * b != b2:
        # a递增
        a += 1
        # b2为a的平方减去n
        b2 = a * a - n
        # b为sqrt(b2)的整数部分
        b = round(math.sqrt(b2))
    # 打印a, b, n
    print(a, b, n)
    # 返回a-b和a+b
    return a - b, a + b


def factorization(n):
    # 记录因子
    factors = []
    # 栈，用于存储待处理的数
    stack = [n]
    # 当栈不为空时
    while len(stack) > 0:
        # 取出栈顶元素
        x = stack.pop()
        # 如果为2，则添加到因子列表中
        if x == 2:
            factors.insert(0, x)
            continue
        # 如果为奇数，则调用fermat函数获取因子
        p, q = fermat(x) if x & 1 == 1 else (2, x // 2)
        # 如果p为1，则将q添加到因子列表中
        if p == 1:
            factors.insert(0, q)
        # 否则，将p和q分别入栈
        else:
            stack.append(p)
            stack.append(q)
    # 返回因子列表
    return factors


if __name__ == '__main__':
    print(factorization(476714679652321667))

