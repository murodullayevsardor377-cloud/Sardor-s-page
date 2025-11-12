def salom_ber(ism):
    print("Salom,", ism)

ism = input("Ismingizni kiriting: ")
salom_ber(ism)




def kvadrat(son):
    return son ** 2

n = int(input("Son kiriting: "))
print("Kvadrati:", kvadrat(n))





def qoshish(a, b):
    return a + b

x = int(input("Birinchi sonni kiriting: "))
y = int(input("Ikkinchi sonni kiriting: "))
print("Yig'indisi:", qoshish(x, y))




def katta_son(a, b):
    if a > b:
        return a
    else:
        return b

x = int(input("Birinchi sonni kiriting: "))
y = int(input("Ikkinchi sonni kiriting: "))
print("Kattasi:", katta_son(x, y))






def ism_familiya(ism, familiya):
    return ism + " " + familiya

i = input("Ismingizni kiriting: ")
f = input("Familiyangizni kiriting: ")
print("To‘liq ism:", ism_familiya(i, f))








def salom_ber(ism):
    print("Salom,", ism)

salom_ber("Sardor")





def kvadrat(son):
    return son ** 2

print("Kvadrati:", kvadrat(7))



def qoshish(a, b):
    return a + b

print("Yig'indisi:", qoshish(12, 8))




def katta_son(a, b):
    if a > b:
        return a
    else:
        return b

print("Kattasi:", katta_son(5, 9))





def ism_familiya(ism, familiya):
    return ism + " " + familiya

print("To‘liq ism:", ism_familiya("Sardor", "Murodullayev"))


