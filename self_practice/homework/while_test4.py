import random

answer=random.randint(1,100)
print("숫자를 맞춰봐")
num=int(input("몇일까?"))


while num:
    if num < answer:
        print("숫자가 작습니다.")
        num=int(input("다시 맞춰봐"))
    if num > answer:
        print("숫자가 큽니다.")
        num=int(input("다시 맞춰봐"))
    if num==answer:
        print(num, "정답입니다.")
        break