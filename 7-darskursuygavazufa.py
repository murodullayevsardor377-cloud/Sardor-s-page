while True:
    buyruq = input("Buyruq kiriting (chap, o‘ng, oldinga, orqaga, stop): ")
    if buyruq == "chap":
        print("Robot chapga burildi ")
    elif buyruq == "o‘ng":
        print("Robot o‘ngga burildi ")
    elif buyruq == "oldinga":
        print("Robot oldinga yurdi ")
    elif buyruq == "orqaga":
        print("Robot orqaga yurdi ")
    elif buyruq == "stop":
        print("Jarayon to‘xtatildi ")
        break
    else:
        print(" Noto‘g‘ri buyruq! Qayta urinib ko‘ring.")








son = int(input("Son kiriting: "))

while True:
    if son % 3 == 0 and son % 5 == 0:
        print("FizzBuzz")
    elif son % 3 == 0:
        print("Fizz")
    elif son % 5 == 0:
        print("Buzz")
    else:
        print(son)
    break









import random

sirli_son = random.randint(1, 10)

while True:
    taxmin = int(input("1 dan 10 gacha son toping: "))
    if taxmin == sirli_son:
        print(" To‘g‘ri topdingiz!")
        break
    else:
        print(" Xato! Qayta urinib ko‘ring.")










parol = input("Parol kiriting: ")

if len(parol) < 8:
    print("Parol juda qisqa ")
elif len(parol) > 15:
    print("Parol juda uzun ")
else:
    print(" Parol uzunligi to‘g‘ri")










ball = 0

while True:
    harakat = input("Harakat kiriting (+, -, stop): ")
    if harakat == "+":
        ball += 1
        print("Ball:", ball)
    elif harakat == "-":
        ball -= 1
        print("Ball:", ball)
    elif harakat == "stop":
        print("O‘yin tugadi. Yakuniy ball:", ball)
        break
    else:
        print(" Noto‘g‘ri buyruq!")

