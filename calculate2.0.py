def calculate():
    price_str = input("请依次输入原价：")
    price_list = price_str.split(',')
    people = len(price_list)
    actual_price = float(input("请输入付款金额："))
    all_price = 0
    for i in range(people):
        all_price += float(price_list[i])
    for j in range(people):
        every_price = float(price_list[j])/all_price*actual_price
        print("实际消费为：%.2f" % every_price)

if __name__ == '__main__':
    calculate()












































