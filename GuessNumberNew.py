"""
    猜数字
"""

# 输入
guess = [1, 2, 3]
answer = [1, 2, 1]
print("guess =", guess, ", answer =", answer)

# 判断猜中的次数
number = list(map(lambda x, y: x == y, guess, answer)).count(True)
print(number)

# 解释说明
if number == 0:
    print("小A一次都没猜对")
elif number == 1:
    print("小A猜中了一次")
elif number == 2:
    print("小A猜中了两次")
else:
    print("小A全部猜中了")
