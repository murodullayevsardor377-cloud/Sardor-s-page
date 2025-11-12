print("Kalkulator dasturi")
print("Amallar: + - * /")
# foydalanuvchidan sonlarni olish
a = float(input("1- sonni kiriring"))
b =float(input("2- sonni kiriring"))
c = float(input("3- sonni kiriring"))
d = float(input("4- sonni kiriring"))
# amalni tanlash
amal = input("Amalni tanlang: (+, -, *, /): ")
# hisoblash
if amal == "+":
    print("Natija:", a + b + c + d, )
elif amal =="-":
    print("Natija:", a - b - c - d, )
elif amal == "*":
    print("Natija:", a * b * c * d, )
elif amal == "/":
   if b != 0:
       print("Natija:", a / b / c / d, )
   else:
       print("Natija:", a / b / c / d, )
else:
    print("Noto'g'ri amal kiritildi!")

















