import random

guess = []
answer = []
number = 0
for i in range(3):
    A = random.randint(1, 3)
    B = random.randint(1, 3)
    guess.append(A)
    answer.append(B)
    if A == B:
        number += 1
        continue
print("guess =", guess, ", answer =", answer)
print(number)
if number == 0:
    print("小A一次都没猜对")
elif number == 1:
    print("小A猜中了一次")
elif number == 2:
    print("小A猜中了两次")
else:
    print("小A全部猜中了")
