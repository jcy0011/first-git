with open("chicken.txt") as fh:
    suma = 0
    for line in fh:
        word = line.strip().split('일: ')
        days, suma = int(word[0]), suma + int(word[1])
    print(suma / days)
