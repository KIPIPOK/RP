#Задание 1.4 
pos = input('Введите последовательность целых чисел через пробел: ')
sum = 0
count = 0
current = ''
index = 0

while index < len(pos):
    if pos[index] != ' ':
        current += pos[index]
    else:
        if current:
            sum += int(current)
            count += 1
            current = ''
    index += 1

if current:
    sum += int(current)
    count += 1

print('Сумма всех чисел последовательности:', sum)
print('Количество всех чисел последовательности:', count)