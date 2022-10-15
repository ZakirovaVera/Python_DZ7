def view():
    """
    Меню тел. справочника
    return: выбранную операцию со справочником
    """
    point = -1

    print("МЕНЮ - Телефонный справочник")
    print("1. Показать Телефонный справочник")
    print("2. Добавить нового пользователя")
    print("3. Удалить запись")
    print("4. Сохранить в файл")
    print("0. Выход")

    while True:
        try:
            point = int(input("Введите номер пункта меню: "))
            if point in [1, 2, 3, 4, 0]:
                break
        except ValueError:
            print("Введён неправильный пункт меню. Попробуйте ещё раз.")
    return point
