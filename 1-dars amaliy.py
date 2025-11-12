print("amaliy mashhulot")

ism = "Ali"
yosh = 21
print("uning ismi:", ism)
print("yoshi:", yosh)

c = 313232
d = 3920303
print("kopaytma:", c * d)
print("ayirma:", c - d)
print("bo'luvchi:",c / d)
print("yig'indi:",c + d )

ism = input("ismini kirit aqlli bola:")
print("Salom,",ism)



print("Kalkulyator dasturi")
print("Amallar: +  -  *  /")

# foydalanuvchidan sonlarni olish
a = float(input("1-sonni kiriting: "))
b = float(input("2-sonni kiriting: "))

# amalni tanlash
amal = input("Amalni tanlang (+, -, *, /): ")

# hisoblash
if amal == "+":
    print("Natija:", a + b)
elif amal == "-":
    print("Natija:", a - b)
elif amal == "*":
    print("Natija:", a * b)
elif amal == "/":
    if b != 0:
        print("Natija:", a / b)
    else:
        print("Xato: 0 ga bo‘lish mumkin emas!")
else:
    print("Noto‘g‘ri amal kiritildi!")











