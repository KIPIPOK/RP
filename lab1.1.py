#Задание 1.1 Работа с математическими операциями в Python
#Считать с клавиатуры три произвольных числа, найти минимальное среди них и вывести на экран.
a=float(input("Введите первое число: "))
b=float(input("Введите второе число: "))
c=float(input("Введите третье число: "))
v = min(a, b, c)
print("Минимальное число",v)