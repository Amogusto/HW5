my_f = open("text2.txt", "r")
linecounter = 0
for line in my_f:
    linecounter += 1
    leng = len(line.split())
    print(f'длинна строки: {leng} слов \n')
my_f.close()
print(f'\n Всего в файле: {linecounter} строки')