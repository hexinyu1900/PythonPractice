from collections import Counter
import math

# 定义好数对的长度
n = 2
# 定义列表
A_list = [1, 2, 3, 1, 1, 3]
# 统计列表中每个数字出现的次数，输出为一个字典
dict_number = dict((Counter(A_list)))
print(dict_number)
# 初始化好数对数目为0
sum_number = 0
# 遍历字典
for key, value in dict_number.items():
    # 如果该数字的个数大于n，计算此时的好数对数目A(m,n)/n!
    if value > n:
        x = math.factorial(value)
        y = math.factorial(value-n)
        z = math.factorial(n)
        sum_number += x/y/z
    # 如果该数字的个数等于n，好数对数目加1
    elif value == n:
        sum_number += 1
    else:
        pass
print(int(sum_number))


















