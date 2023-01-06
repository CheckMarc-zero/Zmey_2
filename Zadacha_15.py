n = int(input('Введите число n: '))
need_list = []
s_value = 1
for i in range(1, n+1):
    s_value = s_value*i
    need_list.append(s_value)
print('Полученный список (факториал n):')    
print(*need_list,sep=', ')    