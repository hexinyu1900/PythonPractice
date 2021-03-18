"""
    输入一组数据，计算和
"""

def input_list():
    str = input("输入一组数字：")
    xstr = str.split(',')
    xlist=list(map(lambda x: int(x), xstr))
    # print(xstr)
    # for i in range(len(xstr)):
    #     xlist.extend([int(xstr[i])])
    print(xlist)
    return xlist


def sum():
    xlist = input_list()
    new_list = []
    new_list.extend([xlist[0]])
    for i in range(1, len(xlist)):
        new_list.extend([new_list[i-1] + xlist[i]])
    print(new_list)


sum()