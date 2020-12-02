while True:
    mass = 'йцукенгшщзхъфывапролджэячсмитьбю1234567890.,!?ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ_'
    string = input("Введите незашифрованый текст: ")
    key = int(input("Введите ключ шифрования: "))
    result = ''
    a = 1
    for i in string:
        if i in mass:
            result += mass[mass.index(i) + (key * a) - (len(mass) * ((mass.index(i) + (key * a)) // len(mass)))]
            a += 1

        else:
            result = "Символ " + i + " не входит в алфавит"
            break

    print(result)