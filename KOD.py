# This is a test for an IT article writer vacancy
# By the terms of the test you can't use import, but you can hardcode the current date
# Request the user's date of birth and
# tell them how many days are left
# and zodiac sign

# Hardcode the current date
current_day = 27
current_month = 2
current_year = 2024

# Request the user's date of birth
birthdate = input("Введите дату рождения в формате ДД.ММ.ГГГГ: ")

# Divide the date of birth into day, month and year
day, month, year = map(int, birthdate.split('.'))

# Create a list with the number of days in each month, taking into account high-summer years
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if current_year % 4 == 0 and (current_year % 100 != 0 or current_year % 400 == 0):
    days_in_month[1] = 29

# Считаем количество дней до дня рождения
if month < current_month or (month == current_month and day < current_day):
    # Если день рождения уже прошел в этом году, расчитываем дни до следующего дня рождения
    days_left = sum(days_in_month[current_month - 1:]) - current_day + sum(days_in_month[:month - 1]) + day
elif month == current_month and day == current_day:
    # Если сегодня день рождения
    days_left = 0
else:
    # Если день рождения еще не наступил в этом году
    days_left = sum(days_in_month[current_month - 1:month - 1]) - current_day + day

# Выводим количество дней до дня рождения
print("До вашего дня рождения осталось", days_left, "дней.")

# Создаем список с знаками зодиака и соответствующими датами
zodiac_signs = [(1, 19, "Козерог"), (2, 18, "Водолей"), (3, 20, "Рыбы"), (4, 19, "Овен"), (5, 20, "Телец"),
                (6, 20, "Близнецы"), (7, 22, "Рак"), (8, 22, "Лев"), (9, 22, "Дева"), (10, 22, "Весы"),
                (11, 21, "Скорпион"), (12, 21, "Стрелец"), (1, 31, "Козерог")]

# Определяем знак зодиака
for i in range(len(zodiac_signs)):
    if (month, day) <= (zodiac_signs[i][0], zodiac_signs[i][1]):
        print("По гороскопу вы ", zodiac_signs[i][2], ", чтобы это не значило :)")
        break
