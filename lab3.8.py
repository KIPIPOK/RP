#Задание 3 (Ввести в консоль: python lab3.8.py 1 2 7 10 20)
import sys
array = [int(x) for x in sys.argv[1:]]

# Считаем сумму элементов списка
sum_array = sum(array)
print("Сумма элементов списка:", sum_array)

# Считаем произведение элементов списка
product_array = 1
for num in array:
    product_array *= num
print("Произведение элементов списка:", product_array)

# Заменяем нулевые элементы на среднее арифметическое всех элементов массива
average = sum_array / len(array)
array = [average if num == 0 else num for num in array]
print("Массив с нулевыми элементами заменен на среднее арифметическое:", array)