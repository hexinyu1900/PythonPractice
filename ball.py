"""
    一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
"""

height = 100
all = 100

for i in range(1, 10):
    # 计算每次落地后反弹的高度
    x = height/(2**i)
    # 第n次落地时经历的长度 = 第n-1次落地经历长度 + 第n-1次反弹*2
    all = all + x*2

print("第10次落地反弹：%.5f" % (100 / (2 ** 10)))
print("第10次落地共经历：%.5f" % all)



