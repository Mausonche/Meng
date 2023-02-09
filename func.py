from random import *
from priv import PRIVET
from copy import deepcopy


def start():
    print(PRIVET)


# def adds(slovo, perevod):
#     """Добавляет слова в словарь"""
#     with open("slovar.txt", "a", encoding="utf-8") as f:
#         print(f"{slovo} {perevod}", file=f)


def checkrus():
    """Возвращает перемешанный список русских слов"""
    with open("slovar.txt", "r", encoding="utf-8") as f:
        res = []
        for i in f.readlines():
            res.append(i.split()[0])

        return res


def checkeng():
    """Возвращает перемешанный список английских слов"""
    with open("slovar.txt", "r", encoding="utf-8") as f:
        res = []
        for i in f.readlines():
            res.append(i.split()[1])

        return res


def genslovar():
    """Создать словарь (нужно для проверки слов удобной)"""
    return dict(zip(checkrus(), checkeng()))


def genslovareng():
    """Создать словарь (нужно для проверки англ слов удобной)"""
    return dict(zip(checkeng(), checkrus()))


def prorus():
    """Тест с РУССКОГО на АНГЛИЙСКИЙ"""
    s = genslovar()
    t = deepcopy(checkrus())
    shuffle(t)
    while len(t) != 0:
        sl = t.pop(0)
        print(sl)
        print("Напиши это слово по английски!")
        otvet = s[sl]
        while True:
            i = input()
            if i == str(otvet):
                print("Правильно!")
                break
            if i != str(otvet):
                print("Неправильно")


def proeng():
    """Тест с АНГЛИЙСКОГО на РУССКИЙ"""
    s = genslovareng()
    t = deepcopy(checkeng())
    shuffle(t)
    while len(t) != 0:
        sl = t.pop(0)
        print(sl)
        print("Напиши это слово по русски!")
        otvet = s[sl]
        while True:
            i = input()
            if i == str(otvet):
                print("Правильно!")
                break
            if i != str(otvet):
                print("Неправильно")


