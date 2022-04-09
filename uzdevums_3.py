#uzdevums 3

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

if number1 < 0:
    print('Skaitlis ir negativs ')
elif number1 == 0:
    print('skaitlis ir nulle ')
else:
    print('skaitlis ir pozitivs')

