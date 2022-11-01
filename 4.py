my_f = open("text4.txt", "r", encoding="UTF8")
my_d = open("text44.txt", "w", encoding="UTF8")
numbers = dict(One = "Один", Two = "Два", Three = "Три", Four = "Четыре")
for line in my_f:
    print(f'{numbers[line.split()[0]]} {line.split()[1]} {line.split()[2]}', file=my_d)
my_f.close()
my_d.close()