my_f = open("text.txt", "w", encoding="UTF-8")
my_str = "word"
while my_str != "":
    my_str = input("Введите строку: ")
    print(my_str, file=my_f)
my_f.close()
