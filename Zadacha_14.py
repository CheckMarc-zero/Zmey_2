n = str(input('Введите число: '))
sum = 0
for i in n:
    if i != ',' and i != '.' and i != '-':
      sum += int(i)
print(f'Сумма цифр числа: {sum}')    