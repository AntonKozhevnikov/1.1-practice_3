import random as r
print("Добро пожалов в игру 'УГАДАЙКА'")
print("Задайте уровень сложности: 1 (8 попыток), 2 (5 попыток), 3 (2 попытки)")
diff = int(input())
if diff > 4:
    print("Ты не так понял, сынок... Ещё раз, задаём уровень сложности от 1 до 3")
    diff = int(input()) 
if diff <= 3:
    if diff == 1 : k = 8
    if diff == 2 : k = 5
    if diff == 3 : k = 2
    print("Числа игры в диапазоне от 1 до ...")
    n = int(input())
    b = r.randint(1, n)
    print("Начинаем, первая попытка!")
    while k > 0:
        tr = int(input())
        if tr > b:
            print("Меньше >:(")
            k-= 1
        else:
            print("Больше :/")
            k -= 1
        if tr == b: print("Поздравляю, угадал!")
    if k == 0:
        print("Попытки кончились")
        print("Ответ:", b)
if diff > 3: print("Всё такие не понял")
print("Конец игры") 




