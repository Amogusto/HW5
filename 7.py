import json

with open('text7.txt', 'r', encoding='UTF-8') as my_f:
    mydict = ({}, {})
    count = 0
    sum = 0
    for line in my_f:
        name = line.split()[0]
        form = line.split()[1]
        income = int(line.split()[2]) - int(line.split()[3])
        mydict[0][name] = income
        count += 1
        if income < 0:
            income = 0
            count -= 1
        sum += income
    average_income = int(sum / count)
    mydict[1]["average_profit"] = average_income
    print(mydict)
    with open("text7.json", "w", encoding="UTF8") as my_j:
        json.dump(mydict, my_j)
