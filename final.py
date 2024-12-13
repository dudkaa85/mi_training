import datetime
now = datetime.datetime.now() #дата изменения или же сейчас
creation_date = datetime.date(2024,12,11)#дата создания

note = [input("введите имя"),input("введите заметку "),input("введите статус")]
note.append(creation_date)
note.append(now)
title = ['Заголовок 1','заголовок 2']

print(note,title)


