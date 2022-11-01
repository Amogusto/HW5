my_f = open('text5.txt', "w", encoding="UTF8")
sum = 0
my_string = input("Введите числа через пробел")
my_f.write(my_string)
my_f.close()
with open('text5.txt', "r", encoding="UTF8") as my_f:
    my_string = my_f.readline().split()
    my_string = map(int, my_string)
    mylist = list(my_string)
    print(mylist)
    for el in mylist:
        sum += el
    print(f'Сумма всех чисел = {sum}')