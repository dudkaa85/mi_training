# Запрашиваем информацию у пользователя
username = input("Введите имя пользователя: ").strip().capitalize()
title = input("Введите заголовок заметки: ").strip().capitalize()
content = input("Введите описание заметки: ").strip().capitalize()
status = input("Введите статус заметки (например, 'Активна', 'Выполнена'): ").strip().capitalize()
created_date = input("Введите дату создания заметки в формате 'день-месяц-год': ")
issue_date = input("Введите дату истечения заметки в формате 'день-месяц-год': ")

# Извлекаем день и месяц из дат
created_day_month = created_date[:-5]  # Отрезаем год
issue_day_month = issue_date[:-5]      # Отрезаем год

# Выводим введенные данные
print("\nВы ввели следующие данные:")
print("Имя пользователя:", username)
print("Заголовок заметки:", title)
print("Описание заметки:", content)
print("Статус заметки:", status)
print("Дата создания заметки (без года):", created_day_month)
print("Дата истечения заметки (без года):", issue_day_month)
