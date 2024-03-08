#Задание 1.2
a=float(input("Введите первое число: "))
b=float(input("Введите второе число: "))
c=float(input("Введите третье число: "))

for nums in[a, b, c]:
    if 1 <= nums <= 50:
        print(nums)