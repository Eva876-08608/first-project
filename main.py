# car = {"price": 2000000, "model": "Tesla", "city": "Moscow"}
# print(car)

# apple = {58, 690, 1, 3, 8, 1, 58}
# print(apple)

# number = int(input())
# if number > 20:
#     print("вы взрослый " + "ваш возраст: " + str(number))
# elif number < 20:
#     print("вы не совсем взрослый " + "ваш возраст: " + str(number))
# else:
#     print("вам ровно: " + str(number))

# day = "Fruday"
# if day == "Sunday":
#     print("today is Sunday")
# elif day == "Monday":
#     print("start work")
# elif day == "Fruday":
#     print("start relax")

# задача на четность и не четность
# x = 13
# if x % 2 == 0:
#     print("x is even")
# else:
#     print("x is odd")
# цикл for in
# проводник по вагонам

# eat = {"eat": "яблолко", "eat1": "капуста", "eat2": "чеснок"}
# for shop in eat.values():
#     print(shop)
# x = 1
# while x < 10:
#    if x == 5:
#        continue
#    print(x)
#    x += 1

# x = [1, 2, 3, 4]
# for number in x:
#     if number == 3:
#         continue
#     print(number)
# print(list(range(5)))
# for x in range(10,31,2):
#     print(x)

# def watering_beds():
#     print(45)
#     print("hello")
#     print(True)
# watering_beds()
# watering_beds()
# def hello(name):
#     print(name)
#
# hello("Eva")
# def r(height, width):
#     print(height * width)
# r(40, 2)

# def registration(name, surname, age):
#     print("ваше имя - ", name, ".Ваша фамилия - ", surname, ".Ваш возраст - ", age)
# registration("Eva", "Pobed", "13")
#
# создать 3 функции
# 1 модель марку год пр. машины
# 2 порода возраст собаки больше 20 одна фраза, меньше 20 другая фраза
# 3 время года фразы: лето-... и тд.

# def car( brand, model, year):
#     print("Марка машины - ", brand, ", Модель машины - ", model, ", Год производства - ", year)
# car("Kia", "Spectra", "2011")

# def dog( breed, age):
#      print("Порода собаки - ", breed)
#      if age > 20:
#          print("Взрослая, возраст - ", age)
#      else:
#          print("Не совсем взрослая, возраст - ", age)
# dog("Лабрадор", 30)

# def seasons( winter, spring, summer, autumn):
#     print("Зима - ", winter, "Весна - ", spring, "Лето - ", summer, "Осень - ", autumn)
# seasons("холодно.", "тепло.", "жарко.", "хорошо.")

# def seasons(time):
#     if time == "winter":
#         print("Зимой холодно")
#     elif time == "spring":
#         print("Собираем чемоданы")
#     elif time == "autumn":
#         print("Пора покупать зонт")
#     elif time == "summer":
#         print("Море ждет")
#     else:
#         print("Некорректно введено время года ")
# seasons("hji")

# def Hello():
#     return "Hello"
# x = Hello()
# print(x)

# def double(number):
#     return number * 2
# x = double(5)
# print(x)

# def summ(a, b):
#     return a + b
# def multiply(a, b):
#     return a * b
# def split(a, b):
#     return a // b
# def operation(a, b, operation):
#     result = operation(a, b)
#     print(result)
# operation(30, 5, split)

# def s(logika):
#     return str(logika)
# x = s(True)
# type(x)
# print(type(x))
# print(type(True))

# def kvadrat(number, n):
#     result = 0
#     for g in n:
#         result = number * number
#     return result
# x = kvadrat(3, 2)
# print(x)

# def number(num):
#     a = ""
#     for x in str(num):
#
#         a += str(int(x) ** 2)
#     return a
#
# f = number(465643)
# print(f)

# a = 2 + 3 + 4
# b = "2" + "3" +"4"
# print(a)
# print(b)

# def revert (number):
#
#     return str(number)
# x = revert(34)
# print(type(x))
#
# fruits = ["apple", "lime", "lemon"]
# fruits[2] = "orange"
# fruits.append("banana")
# print(fruits)


# z = []
# for w in range(51):
#     if w%2 == 0:
#         z.append(w)
# print(z)

# print([w for w in range(101) if w%2 == 0]) это генератор списка

# def d(r):
#     t = []
#     for i in r:
#         if i in "eEyYuUiIoOaA":
#             t.append(i)
#     return len(t)
#
# x = d("ghekhOljaiuAU")
# print(x) подсчет гласных

# x = "hzdhoigdhbonh"
# v = x.count("h")
# print(v)

# def ggg(a):
#     a1 = a.count("x")
#     a2 = a.count("o")
#     if a1 == a2:
#         return True
#     else:
#         return False
# r = ggg("xxxoookdfhlfo")
# print(r) подсчет и сравнение букв

# x = "dfhgpdfyhj"
# print(x[-4:] + x[1] + x[3:6])

# def hideCard(n):
#     print( (len(n) - 4) * "#" + n[-4:])
# hideCard("98765") скрывать номер карты

# x = "1 2 3 4"
# def number(a):
#     a1 = a.split()
#     max = a1[0]
#     min = a1[0]
#     for i in a1:
#         if int(i) > int(max):
#             max = int(i)
#         elif int(i) < int(min):
#             min = int(i)
#     print(max, min)
# number("9 20 5 4 15 6")
#нахождение максимального и минимального элемента в строке

# x = [1, 2, 3, 4, 5]
# print(min(x))

# print(int("1"* 2)**2)

# n = 700
# m = 7000
# r = m // n
# ost = m % n
# if ost == 0:
#     print(r)
# elif ost > 0:
#     print(r + 1)
# расчет дней в пути

# "apple milk banana oil"
# "apple milk ananab oil"
# def t(st):
#     otvet = ""
#     v = st.split()
#     for i in v:
#         if len(i) > 5:
#             otvet = otvet + i[::-1] + " "
#         else:
#             otvet = otvet + i + " "
#     print(type(otvet))
# t("apple milk banana oil")
# переворачивание элементов в строке

# def t(st):
#     return " ".join([i[::-1] for i in st.split() if len(i) > 5])
# p = t("appleghfb milknbmmn banana ugjjgj ")
# print(p)
# переворачивение в строке через генератор
#  y = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# x = [1, 2, 3, 4, 5]
# # одномерный
# y = [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]]
# print(y[2][2])
#------------- генерация матрецы m n ---------------
# import random
# m = int(input("введите высоту:"))
# n = int(input("введите ширину:"))
# print(f"генерируем матрицу шириной - {n} и высотой - {m}")
# matrix = []
# for i in range(m): #создает строки в матрице
#     matrix.append([])
#     for j in range(n): #в каждую строку добавляет элементы
#         matrix[i].append(random.randint(1, 9))
# #----------------------------------------------------
# #------------- вывод матрицы в консоль --------------
#
# for i in range(m):
#     for j in range(n):
#         print(matrix[i][j], end=" ")
#     print()
#----------------------------------------------------
# print()
# print()
# for i in range(m):
#     for j in range(n):
#         if i == j:
#             matrix[i][j] = 0
#             print(matrix[i][j], end=" ")
#         else:
#             print(matrix[i][j], end=" ")
#     print()
# print()
# print()
# for i in range(m):
#     for j in range(n):
#         if i == j:
#             matrix[i][j] = 0
#             print(matrix[i][j], end=" ")
#         else:
#             matrix[i][j] = abs(i - j)
#             print(matrix[i][j], end=" ")
#     print()

import random
# m = int(input("введите высоту:"))
# n = int(input("введите ширину:"))
# print(f"генерируем матрицу шириной - {n} и высотой - {m}")
# matrix = []
# for i in range(m): #создает строки в матрице
#     matrix.append([])
#     for j in range(n): #в каждую строку добавляет элементы
#         matrix[i].append(0)
#
# for i in range(m):
#     for j in range(n):
#         if i + j == m - 1: #побочная диогональ матрицы
#             matrix[i][j] = 1
#             print(matrix[i][j], end=" ")
#         elif i + j >= m:
#             matrix[i][j] = 2
#             print(matrix[i][j], end=" ")
#         else:
#             print(matrix[i][j], end=" ")
#     print()
# name = ["Alex", "Jacob", "Kate", "Eva", "Tom"]
# def likes(name):
#     if len(name) == 0:
#         print("Никто тебя не лайкнул(")
#     elif len(name) == 1:
#         print(f"{name[0]} лайнул(-а) вас" )
#     elif len(name) == 2:
#         print(f"{name[0]},{name[1]} лайнули вас" )
#     else:
#         print(f"{name[0]} , {name[1]} и еще {len(name) - 2} лайнули вас")
# likes(name)
# лайки соц сеть

# m = int(input("введите высоту:"))
# n = int(input("введите ширину:"))
# ki = int(input("введите строку коня:"))
# kj = int(input("введите столбец коня:"))
# print(f"генерируем матрицу шириной - {n} и высотой - {m}")
# matrix = []
# for i in range(m):
#     matrix.append([])
#     for j in range(n):
#          matrix[i].append(".")
# matrix[ki][kj] = "K"
# for i in range(m):
#      for j in range(n):
#          if (abs((i-ki)*(j-kj)) == 2):
#              matrix[i][j] = "*"
#              print(matrix[i][j], end=" ")
#          else:
#              print(matrix[i][j], end=" ")
#      print()
#---жиза ход конем--

# min = 1000
# max = 80
# n = int(input("введите кол-во проехавших машин:"))
# for i in range(n):
#     a = int(input("введите скорость:"))
#     if a < min:
#         min = a
#     if a > max:
#         print(True)
#     else:
#         print(False)
# print(min)

# z = 0
# numbers = 5
# for i in range(numbers):
#     x = int(input("введите число:"))
#     if (x%4 == 0) and (x%6 == 0):
#         z += x
# print(z)

# a = int(input())
# b = int(input())
# c = int(input())
# if a == b and b == c:
#     print("треугольник равносторонний")
# elif a == b or b == c:
#     print("треугольник равнобедренный")
# else:
#     print("треугольник разносторонний")

# n = int(input("введите высоту треугольника"))
# for i in range(n + 1):
#     for j in range(i):
#         print(i, end = " ")
#     print("")

# v = int(input('введите кол-во чисел'))
# sum = 0
# for i in range(v):
#     r = int(input("введите число"))
#     if r%10 == 4:
#         sum += r
# print(sum)
# ------определение чисел заканчивающихся на 4 -------

# print(ord("b"))
# print(chr(109))
# -------------------------------------------------------
# def position(s):
#     m = ""
#     for i in s.lower():
#         if i.isalpha():
#             m += str(ord(i)-(ord("a")-1))
#     print(m)
#
#
# position("HELLO")
# ---------перевод строки в порядковые номера букв--------

# --------------------------------------------------------------
# rezept = {"spagetty": 400,"chesnok": 0.4,"eggs": 4,"parmezan": 50,"becon": 200,"butter": 20,"water": 2}
# our_prodyks = {"becon": 100,"spagetty": 0,"eggs": 2,"parmezan": 45,"butter": 20,"chesnok": 0.4,"water": 1}
# # def cakes(r,p):
# for i in rezept:
#     if i in our_prodyks:
#         if our_prodyks[i] >= rezept[i]:
#             print(i + " ингридиент подошел")
#         else:
#             print(i + " ингридиент не подошел")
#     else:
#         print("у вас нет нужного ингридиента")
#         break
# ------------нестардантное сравнивание рецептов-------------------
# m = []
# n = {"s":"ug","ug":"z","v":"s","z":"v"}
# for i in n:
#     if i == "ug" and n[i] == "z" or i == "ug" and n[i] == "v" or i == "z" and n[i] == "ug" or i == "v" and n[i] == "ug" or i == "s" and n[i] == "z" or i == "s" and n[i] == "v" or i == "z" and n[i] == "s" or i == "v" and n[i] == "s":
#         m.append(i)
#         m.append(n[i])
#
# print(m)

# ---------------определение сезона-------------
# def sezons(n):
#     if n == 12 or n == 1 or n == 2:
#         return "winter"
#     elif n == 3 or n == 4 or n == 5:
#         return "spring"
#     elif n == 6 or n == 7 or n == 8:
#         return "summer"
#     elif n == 9 or n == 10 or n == 11:
#         return "autumn"
#     else:
#         return "error"
# m = sezons(int(input()))
# print(m)
# -----------------------из ОГЭ СЛОЖНАЯ----------------
# chkpu = []
# nidt = 0
# i = int(input())
# while i != 0:
#     if (i % 2 != 0) and (i % 3 == 0):
#         chkpu.append(i)
#         nidt += 1
#     i = int(input())
# print(chkpu, nidt)
# ******************************************************
# -------------------------чистильщик ссылок----------------------------------
# def url(a):
#     n = a.replace("https://", "").replace("http://", "").replace("www.", "")
#     m = n.split(".")
#     print("доменное имя сайта - " + m[0])
#     print("зона регистрации сайта - "+"."+m[1])
# url("www.google.com")
# -----------------------------------------------------------------------------

# -------------------------------------------------------------------------------
# import random
# print("привет, как тебя зовут?")
# name = str(input())
# print(name + ", угадай число от 1 до 1000 (за 9 попыток)")
# randNumber = random.randint(1,1000)
# print("число загадано, введите свое число:")
# for i in range(9):
#     number = int(input())
#     if number < randNumber:
#         print("ваше число меньше загаданного")
#     elif number > randNumber:
#         print("ваше число больше загаданного")
#     else:
#         print("вы угадали число!")
#         break
# if number == randNumber:
#     print("победа!")
# else:
#     print("вы проиграли(  " + "было загадано число: " + str(randNumber))
# -------------------------------игра отгадай число-------------------------------

# -------------------------------------------------------------
# А я в 7-8 классе!
# n = 0
# for i in range(100, 1000):
#     t = str(i)
#     sum1 = int(t[0]) + int(t[1])
#     sum2 = int(t[1]) + int(t[2])
#     mi = str(min(sum1, sum2))
#     ma = str(max(sum1, sum2))
#     f = mi + ma
#     if f == "1011":
#         n += 1
#         print(i)
# print(n)
# --------------5 задание из ЕГЭ--------------------------------

# ---------------------------------------------------------------
# import string
# import secrets
# import time
# letters = string.ascii_letters
# numbers = string.digits
# spec_simbols = string.punctuation
# alphabet = letters + numbers + spec_simbols
# parol = ""
# for j in range(5):
#     time.sleep(2)
#     print("Генерирую пароль ", end = "")
#     time.sleep(2)
#     for u in range(5):
#         print(".", end = "")
#         time.sleep(1)
#     for i in range(8):
#         parol += secrets.choice(alphabet)
#     print()
#     print(parol)
#     parol = ""
# ------------ГЕРЕРАТОР ПАРОЛЕЙ (ЭФФЕКТ ЗАГРУЗКИ)---------------

# -------------------------------------------------------------------
# kids = int(input("введите кол-во сдающих экзамен : "))
# for i in range(1,kids + 1):
#     ocenka = int(input("введите кол-во решенных задач для " + str(i) + " ученика : "))
#     if ocenka < 5:
#         print("ученик " + str(i) + " получил оценку : 2")
#     elif ocenka == 10:
#         print("ученик " + str(i) + " решил все задачи")
#     else:
#         print("вы сдали!")
# ---------------------ложно-сложная задача----------------------------

# x = open("fgo.txt", "r")
# print(x)
# РАБОТА С НЕСКОЛЬКИМИ ФАЙЛАМИ

# --------------------------ОЖИДАНИЕ ЯНДЕКС ЛИЦЕЙ--------------------
# # ЗАДАЧА 1
# print("Привет Яндекс")
# # ЗАДАЧА 2
# x = "hello"
# print(x)
# # ЗАДАЧА 3
# a = int(input())
# b = int(input())
# c = str(a) + ":" + str(b)
# print(c)
# # ЗАДАЧА 4
# if input() == "ok":
#     print("верно")
# else:
#     print("неверно")
# ЗАДАЧА 5
# y, i = input(), input()
# if y > i:
#     print(y+i)
# else:
#     print((y+i)*2)
# ЗАДАЧА 6
# x = int(input("введите число: "))
# y = int(input("введите число: "))
# z = input("введите знак: ")
# if x > y and z == "+":
#     print(x + y)
# elif x < y and z == "*":
#     print(x * y)
# elif x == 2 or y == 7 or x == 3 and y == 5:
#     print((x+y)*2)
# else:
#     print("нет такого события")
# ЗАДАЧА 7
# a = int(input())
# b = int(input())
# c = int(input())
# i = float(input())
# print((a*b*c)/i)
# ЗАДАЧА 8
# import math
# a = int(input())
# b = int(input())
# sum1 = (a*a) + b*b
# n = math.sqrt(sum1)
# print(n)
# ЗАДАЧА 9
# import math
# r = int(input())
# c = int(input())
# v = 4/3 * math.pi * pow(r, 3)
# z = v * c
# print(z)
# # ЗАДАЧА 10
# x = [2,3,4,6,4,7,2]
# h = 0
# for i in range(len(x) - 1):
#     if i == len(x) - 1 or i == len(x) - 2:
#         print("попытка" + str(i))
#         break
#     elif x[i] < x[i + 1] and x[i + 1] > x[i + 2]:
#         print("попытка" + str(i) + "h = " + str(h))
#         h += 1
#
# print(h)
# СЛОЖНАЯ ЗАДАЧА РЕШЕНА
# ЗАДАЧА 11
# import math
# a = str(input())
# print(round(len(a) / len("parrot")))
# ЗАДАЧА 12
# m = int(input())
# h = int(input())
# h1 = h * 60
# y = 0
# if y == 90:
#     print("прямой")
# elif y > 90:
#     print("тупой")
# elif y < 90:
#     print("острый")
# elif y == 180:
#     print("развернутый")
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# ЗАДАЧА 10
# x = str(input()).upper()
# price = {0.5:"ЬЪ",
#          1:"AEIOULNSTRЛМНО",
#          2:"DGBCMPАБВГД",
#          3:"FHVWYПРСТУ",
#          4:"KJZQЕЖЗИК",
#          5:"ФХЦ",
#          6:"ЧШЩ",
#          7:"ЭЮЯ"}
# sum = 0
# for i in x:
#     for j in price:
#         if i in price[j]:
#             sum += j
#             break
# print(sum)
# ЗАДАЧА11
# x = [5,"h",-2,7, 9,-1,6.5, "привет", 4, "hello"]
# y = []
# z = []
# v = []
# v1 = []
# y1 = []
# for i in x:
#     if type(i) == int and i > 0:
#         y.append(i)
#     elif type(i) == int and i < 0:
#         y1.append(i)
#     elif type(i) == str:
#         z.append(i)
#     elif type(i) == float and i > 0:
#         v.append(i)
#     elif type(i) == float and i < 0:
#         v1.append(i)
# print(y)
# print(z)
# print(v1)
# print(v)
# print(y1)



# Дз
# print("Ввод")
# x = int(input())
# y = int(input())
# print("Вывод")
# if y == 0:
#     print("Не делится!")
# elif  x / y :
#     z = x // y
#     ost = x % y
#     print("Каждому по " + str(z))
#     print("Осталось " + str(ost))

# Дз
# z = 0
# y = 0
# while True:
#     x = int(input())
#
#     if x == 0:
#         print("мячик упал в ямку")
#         break
#     elif x > z:
#         y += 1
#         z = x
# print(y - 1)
# дз
# n = int(input("стоимость отправки 1-ого смс"))
# m = int(input("ограничение длины одного сообщения"))
# sms = str(input("введите смс "))
# d = len(sms) // m
# ost = len(sms) % m
# if len(sms) // m and ost == 0:
#     print("конечная стоймость: " + str(n * d) + " руб")
# elif len(sms) / m and ost > 0:
#     print("конечная стоймость: " + str(n * d + n) + " руб")











