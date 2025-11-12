

import random
a = random.randint(0,1)
while True:
    x = input("tanga yoki gerb tanlang: ")
    if x == "tanga":
        if a == 0:
            print("yutdingiz")
            break
        else:
            print("yutqazdingiz")
    elif x == "gerb":
        if a == 1:
            print("yutdingiz")
            break
        else:
            print("yutqazdingiz")
    else:
        print("noto'g'ri tanlov")
















