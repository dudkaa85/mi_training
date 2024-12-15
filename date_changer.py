# date = input('ведите дату:') # этап 1 задание 2
# print(date)


# import datetime

# now = datetime.datetime.now()
# print(now)#текщая дата
# # дата создание обьекта
# birthday = datetime.date(2024,12, 7)
# print(birthday)

# Запрашиваем информацию у пользователя
username = input("Введите имя пользователя: ")
title = input("Введите заголовок заметки: ")
content = input("Введите описание заметки: ")
status = input("Введите статус заметки (например, 'Активна', 'Выполнена'): ")
created_date = input("Введите дату создания заметки в формате 'день-месяц-год': ")
issue_date = input("Введите дату истечения заметки в формате 'день-месяц-год': ")


# Выводим введенные данные
print("\nВы ввели следующие данные:")
print("Имя пользователя:", username)
print("Заголовок заметки:", title)
print("Описание заметки:", content)
print("Статус заметки:", status)
print("Дата создания заметки:", created_date)
print("Дата истечения заметки:", issue_date)
