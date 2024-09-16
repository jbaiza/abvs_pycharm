# uzdevums 2

print('Ievadi divus skaitlus, un es saskaitisu tos')




while True:
    number1 = input('skaitlis 1: ')
    try:
        int(number1)
    except ValueError:
        try:
            float(number1)
        except ValueError:
            print('Ievadi skaitli ludzu')
        else:
            number1 = float(number1)
            break
    else:
        number1 = float(number1)
        break
while True:
    number2 = input('skaitlis 2: ')
    try:
        int(number2)
    except ValueError:
        try:
            float(number2)
        except ValueError:
            print('Ievadi skaitli ludzu')
        else:
            number2 = float(number2)
            break
    else:
        number2 = float(number2)
        break

print(number1 + number2)


