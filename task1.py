# Напишите программу, удаляющую из текста все слова, содержащие "абв".

text = "Абв гдеу абвцшцд жовдаввабв"
list = text.split(' ')
print(list)

i = len(list)-1

while i>=0:
    if 'абв' in list[i] or 'Абв' in list[i]:
        list.remove(list[i])
    i-=1
print(list)
