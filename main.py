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

prices = [33, 49, 55, 14]

# total price
total = sum(prices)
print("Total Price:", total)


# number of products
number_of_products = len(prices)
print("Count:", number_of_products)

# calculating the average
avg_price = total/number_of_products
print("Average Price:", avg_price)
