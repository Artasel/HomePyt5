# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета(или сколько вы зададите). Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет(или сколько вы зададите). Тот, 
# кто берет последнюю конфету - проиграл.
# Предусмотрите последний ход, ибо там конфет остается меньше.

# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"

from random import randint

def First_Step(cho, boo):
    choice = randint(0, 2)
    if choice == 0:
        print("Выпал орел!")
        choice == "орел"
    else:
        print("Выпала решка!")
        choice = "решка"
    if cho == choice:
        print("Вы выиграли, ваш ход первый!")
        boo = True
    else:
        print("Вы проиграли, ходит первым бот!")
        boo = False
    return boo

def I_Take():
    while True:
        try:
            number = int(input("Сколько берете конфет, хозяин?!: "))
            if number > 0 and number < 29:
                return number
            else:
                print("Можно брать не больше 28 конфет и не меньше одной!")
        except:
            print("Неверный ввод!")

x = 202

step = True
while True:
    choic = input("Выберите, орел или решка?: ")
    if choic == "орел" or choic == "Орел" or choic == "решка" or choic == "Решка":
        step = First_Step(choic, step)
        break
    else:
        print("Неверный ввод!")

print("Забрать за один ход можно не больше 28 конфет, тот, кто берет последнюю конфету - проиграл.")

if step:
    take = "I"
else:
    take = "bot"

while x > 0:
    print(f"На столе {x} конфет.")
    if take == "I":
        number = I_Take()
        x -= number
        take = "bot"
    else:
        if x != 1:
            if x <= 29:
                tak = x - 1
            else:
                tak = randint(1, 29)
        else:
            tak = 1
        print(f"Бот забирает {tak} конфет")
        x -= tak
        take = "I"

if take == "I":
    print("Вы победили, о Великий!!!")
else:
    print("Бот победил Вас, о Великий!!!")