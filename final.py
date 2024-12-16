# Создаем словарь для хранения информации о заметке
note = {}


# Сбор данных от пользователя
note["username"] = input("Введите имя пользователя: ").strip().capitalize()
note["content"] = input("Введите описание заметки: ").strip().capitalize()
note["status"] = input("Введите статус заметки (например, 'Активна', 'Выполнена'): ").strip().capitalize()
note["created_date"] = input("Введите дату создания заметки в формате 'день-месяц-год': ")
note["issue_date"] = input("Введите дату истечения заметки в формате 'день-месяц-год': ")


# Добавляем заголовки в список внутри словаря
note["titles"] = []
for i in range(3):
    title = input(f"Введите заголовок заметки {i + 1}: ")
    note["titles"].append(title.strip().capitalize()) # убираем все пробелы чтоб сделать первую букву заглавной


# Выводим собранные данные
print("\nСобранная информация о заметке:")
for key, value in note.items():
    print(f"{key.capitalize()}: {value}")
