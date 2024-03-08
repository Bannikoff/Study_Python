# Це приклад скрипту на Python для PyCharm.

# Натисніть ⌃R, щоб виконати його або замінити своїм кодом.
# Подвійне натискання клавіші ⇧ для пошуку класів, файлів, вікон інструментів, дій та налаштувань.
#
#
# def print_hi(name):
#     # Для налагодження скрипта використовуйте точку переривання в рядку коду нижче.
#         print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
#
#
# # Натисніть зелену кнопку в жолобі, щоб запустити скрипт.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # Див. довідку PyCharm на https://www.jetbrains.com/help/pycharm/
# num = int(input('Number: '))
# print ('Вгадав') if num == 55 else print ('Не вгадав')

def sum_array(arr):
    if arr is None or len(arr) <= 1:
        return 0
    else:
        arr.sort()  # Сортуємо список
        arr.pop(-1)  # Видаляємо найбільший елемент
        arr.pop(0)  # Видаляємо найменший елемент
        return sum(arr)
