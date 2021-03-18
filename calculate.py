def calculate():
    n=int(input("请输入购买人数："))
    i=0
    all_price=0
    list=[]
    while i<n:
        a=float(input("请输入原价："))
        i=i+1
        list.append(a)
        all_price+=a
    # print(list)
    # print(actual_price)
    actual_price=float(input("请输入总消费："))
    j=0
    while j<n:
        every_price=(float(list[j]))/all_price*actual_price
        print("实际消费为：%.2f" % every_price)
        j=j+1

calculate()
