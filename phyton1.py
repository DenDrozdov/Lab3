print('Вы оказались в лесу\n')
print('Вы можете предпринять следующие действия:')
a = 636363
while True:
    
    print('1. Осмотреться\n2. Пытаться выйти из леса\n')
    vvod = input('Ваши действия?\n')
    if vvod not in '12':
        print('Выберите одно действие\n')
        print('Вы можете предпринять следующие действия:')
