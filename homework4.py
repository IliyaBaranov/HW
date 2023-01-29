while True:
    try:
        user_id = input('Enter id code: ')
        int(user_id)
        if len(user_id) != 11:
            raise Exception

    except ValueError:
        print('Code you entered is not numeric.')
        continue
    except Exception:
        if len(user_id) > 11:
            print('Code is too long')
        else:
            print('Code is too short')
        continue
    else:
        # print(f'Your code is {user_id}')
        while True:
            user_choice = input("Please choose:\n1.Gender\n2.Date of birth\n"
                                "3.Region\n4.Validate\n5.Change ID\n0.Exit\n-->")
            if user_choice == '1':
                str(user_id)
                if str(user_id[0]) == 1 or 3 or 5 or 7 or 9:
                    print('You are male')
                else:
                    print('You are female')
            elif user_choice == '2':
                    if (int(user_id[0]) >= 0) and (int(user_id[0]) < 2):
                        print('Your date is ' + user_id[5:7] + '.' + user_id[3:5] + '.' + '18' + user_id[1:3])
                    if (int(user_id[0]) >= 2) and (int(user_id[0]) < 5):
                        print('Your date is ' + user_id[5:7] + '.' + user_id[3:5] + '.' + '19' + user_id[1:3])
                    if (int(user_id[0]) >= 5) and (int(user_id[0]) < 7):
                        print('Your date is ' + user_id[5:7] + '.' + user_id[3:5] + '.' + '20' + user_id[1:3])
                    if (int(user_id[0]) >= 7) and (int(user_id[0]) < 9):
                        print('Your date is ' + user_id[5:7] + '.' + user_id[3:5] + '.' + '21' + user_id[1:3])
                        quit()
            elif user_choice == '3':
                lst1 = [1, 11, 21, 151, 161, 221, 271, 371, 421, 471, 491, 521, 571, 601, 651]
                lst2 = [10, 19, 150, 160, 220, 270, 370, 420, 470, 490, 520, 570, 600, 650, 700]
                lst3 = ['Больница Курессааре',
                        'Женская клиника Тартуского университета',
                        'Восточно-Таллиннская центральная больница, Родильный дом Пелгулинна (Таллинн)',
                        'Больница Кейла',
                        'Больница Рапла, Больница Локса, Больница Хийумаа (Кярдла)',
                        'Центральная больница Ида-Виру (Кохтла-Ярве,бывший Йыхви)',
                        'Клиника Маарьямыйза (Тарту), Йыгеваская больница',
                        'Нарвская больница',
                        'Пярнуская больница',
                        'Больница Хаапсалу',
                        'Больница Ярваского уезда (Пайде)',
                        'Больница Раквере, Больница Тапа',
                        'Больница Валга',
                        'Больница Вильянди',
                        'Больница Южной Эстонии (Выру), Больница Пылва']
                # print(len(lst1))
                # print(len(lst2))
                # print(len(lst3))
                if len(lst1) == len(lst2) == len(lst3):
                    # print('Spiski vernie')
                    for x in range(len(lst1)):
                        if lst1[x] <= int(user_id[-4:-1]) and lst2[x] >= int(user_id[-4:-1]):
                            print('Your hospital is ' + lst3[x])
                            break
                else:
                    print('List mismatch')
                    quit()
            elif user_choice == '4':
                lst4_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
                lst4_2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
                sum = 0
                sum2 = 0
                # Проверка по первому весу уровня
                for y in range(len(lst4_1)):
                    sum = int(lst4_1[y]) * int(user_id[y])
                    sum2 = sum2 + sum
                print('(First method) Your security code is ', sum2 - (sum2 // 11) * 11)
                # Проверка по второму весу уровня
                for y in range(len(lst4_2)):
                    sum = int(lst4_2[y]) * int(user_id[y])
                    sum2 = sum2 + sum
                print('(Second method) Your security code is ', sum2 - (sum2 // 11) * 11)
            elif user_choice == '5':
                break
            elif user_choice == '6':
                quit()
            else:
                print('Choice is out of range')
