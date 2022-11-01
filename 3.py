my_f = open("text3.txt", "r", encoding="UTF8")
sum = 0
mycount = 0
print('Менее 20 тысяч зарабатывают:\n')
for line in my_f:
    sum += float(line.split()[1])
    mycount += 1
    if float(line.split()[1]) < 20000:
        print(line.split()[0])

print(f'\nСредняя зароботная плата сотрудников соствляет: {sum / mycount}')
my_f.close()
