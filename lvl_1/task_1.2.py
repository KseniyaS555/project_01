# Задача 1.2.

# Пункт A. 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]

# Пункт B. 
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}

# Дополнительно для пунктов A и B
# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random
# import random

# Дополнительно 
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime 

print(" Пункт A")
import random
a=random.sample(my_favorite_songs,3)
all_seconds=0
for i in a:
    minutes=int(str(i[1]).partition('.')[0])
    second=int(str(i[1]).partition('.')[2])+minutes*60
    all_seconds+=second
print('Три песни звучат', round(all_seconds/60), "минут")

print('Пункт С для пункта А')
n_words=random.randint(2,4)
out=''
for n in range(1,n_words):
    out+=random.choice(random.choice(my_favorite_songs)[0].split(' '))+' '
print('Генерируем новую песню', out)

print(" Пункт B")
b=dict.items(my_favorite_songs_dict)
c=list(b)
d=random.sample(c,3)
#print(d)
all_seconds=0
for i in d:
    minutes=int(str(i[1]).partition('.')[0])
    second=int(str(i[1]).partition('.')[2])+minutes*60
    all_seconds+=second  
print('Три песни звучат', round(all_seconds/60), "минут")
print('Пункт С для пункта В')
nash_spisok=[]
for x in my_favorite_songs_dict:
    slova=x.split(' ')
    for y in slova:
        nash_spisok.append(y)
words=random.sample(nash_spisok,3)
print('Генерируем новую песню',words[0], words[1], words[2])
# import datetime
# a=6.50
# data_object =datetime.datetime.strftime(a, "%M.%S")
# print(data_object)


#работаю над пунктом D 
