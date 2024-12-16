# Запрашиваем у пользователя информацию
username = input("Введите имя пользователя: ").strip().capitalize()
content = input("Введите описание заметки: ").strip().capitalize()
status = input("Введите статус заметки (например, 'Активна', 'Выполнена'): ").strip().capitalize()
created_date = input("Введите дату создания заметки в формате 'день-месяц-год': ")
issue_date = input("Введите дату истечения заметки в формате 'день-месяц-год': ")

# Запрашиваем заголовок заметки
titles = []
num_titles = int(input("Сколько заголовков заметки вы хотите ввести? "))
for i in range(num_titles):
    title = input(f"Введите заголовок {i + 1}: ".strip().capitalize())
    titles.append(title)


# Выводим все данные
print("\nВы ввели следующие данные:")
print("Имя пользователя:", username)
print("Заголовок заметки:", title)
print("Описание заметки:", content)
print("Статус заметки:", status)
print("Дата создания заметки:", created_date)
print("Дата истечения заметки:", issue_date)
