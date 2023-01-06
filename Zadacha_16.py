print('Введите n:')
n = int(input())
need_list = []
s_value = None
sum = 0
for i in range(1, n+1):
    s_value = round((1+i**(-1))**i,2)
    need_list.append(s_value)
    sum += s_value
print('Полученный список :')    
print(*need_list,sep=', ') 
print('Сумма элементов списка:')
print(sum)
