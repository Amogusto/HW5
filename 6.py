my_f = open('text6.txt', 'r', encoding="UTF8")
subjects = {}
for line in my_f:
    mykey = line.split()[0]
    try:
        lect = line.split()[1]
        lect = int(lect[0:lect.find("(")])
    except:
        lect = 0
    try:
        pr = line.split()[2]
        pr = int(pr[0:pr.find("(")])
    except:
        pr = 0
    try:
        lab = line.split()[3]
        lab = int(lab[0:lab.find("(")])
    except:
        lab = 0
    sum = lect + lab + pr
    subjects[mykey] = sum
print(subjects)
