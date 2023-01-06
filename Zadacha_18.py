from random import randint
print('Введите через пробел элементы списка:')
input_list = input().split()
out_list = []
i = None
while len(input_list)>0:
    i = randint(0,len(input_list)-1)
    out_list.append(input_list[i])
    input_list.pop(i)
print('Полученный список:')    
print(*out_list,sep=', ')     