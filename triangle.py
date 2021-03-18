"""
     计算一组数据中能构成三角形的最大周长
"""

# 输出数据列表
str = input("输入一组数字：")
xstr = str.split(',')
xlist = list(map(lambda x: int(x), xstr))

# 排序
xlist.sort(reverse=True)

# 从大到小，三边为一组，判断是否能构成三角形并算出数据
perimeter = 0
for i in range(len(xlist)-2):
    a = xlist[i]
    b = xlist[i+1]
    c = xlist[i+2]
    if b+c > a:
        perimeter = a+b+c
        break

if perimeter == 0:
    print("无数据构成三角形")
else:
    print("三角形的周长最大为：", perimeter)

