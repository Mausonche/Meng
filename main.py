from func import *
flag = True
while flag:
    start()
    print(
        """Приветствую! 
        Выбирай режим!
        1.Добавление слов
        2.Тест на знание с русского на английский
        3.Тест на знание с английского на русский
        4.Выход"""
    )
    mess = input()
    if mess == "1":
        print("СНАЧАЛА ВВЕДИ СЛОВО НА АНГЛИЙСКОМ, А ПОТОМ НА РУССКОМ")
        """Добавляет слова в словарь"""
        slovo = input()
        perevod = input()
        f = open("slovar.txt", "a", encoding="utf-8")
        print(f"{slovo} {perevod}", file=f)
        f.close()

    if mess == "2":
        prorus()

    if mess == "3":
        proeng()

    if mess == "4":
        flag = False
