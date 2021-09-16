
        
#Прочитать содержимое ( водну строку), подсчитать длину,  кол-во слов в тексте,
# Заменить точки на восклицательные знаки, сохранить как реферат 2
with open('text.txt', 'r', encoding = 'utf-8') as referat:
    lastline = ''
    for line in referat:
        replaced_line = line.replace(',', '!')
        big_line = lastline + line 
        with open('referat2.txt', 'a', encoding = 'utf-8') as referat2:
            referat2.write(replaced_line)
            print(replaced_line)       
   
        lastline = big_line
    print(f' Длина: {len(big_line)}')# длина
    print(f' Количество слов в тексте: {len(big_line.split())}')# Количество слов
    #print(f'{big_line.replace(',', '!')}')#Замена
    

