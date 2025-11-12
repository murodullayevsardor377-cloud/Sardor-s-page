sonlar = []

for i in range(5):
    son = int(input(f"{i+1}-sonni kiriting: "))
    sonlar.append(son)

print("Kiritilgan sonlar:", sonlar)
print("Yig‘indi:", sum(sonlar))







sonlar = []

for i in range(5):
    son = int(input(f"{i+1}-sonni kiriting: "))
    sonlar.append(son)

print("Juft sonlar:")
for s in sonlar:
    if s % 2 == 0:
        print(s)






sonlar = [4, 11, 9, 20, 15, 5, 30]

for son in sonlar:
    if son > 10:
        print(son)






ismlar = []

for i in range(5):
    ism = input(f"{i+1}-ismni kiriting: ")
    ismlar.append(ism)

print("Katta harflarda:")
for ism in ismlar:
    print(ism.upper())






sonlar = []

for i in range(5):
    son = int(input(f"{i+1}-sonni kiriting: "))
    sonlar.append(son)

print("Eng katta son:", max(sonlar))
print("Eng kichik son:", min(sonlar))









sonlar = []

for i in range(5):
    son = int(input(f"{i+1}-sonni kiriting: "))
    sonlar.append(son)

orta = sum(sonlar) / len(sonlar)
print("O‘rtacha qiymat:", orta)









sonlar = [3, -4, 7, -1, 0, -6, 5]

for son in sonlar:
    if son < 0:
        print(son)







sonlar = [2, 4, 6, 8]
kvadratlar = []

for s in sonlar:
    kvadratlar.append(s ** 2)

print("Kvadratlar:", kvadratlar)









ismlar = ["Ali", "Guli", "Hasan", "Umid"]
ism = input("Ism kiriting: ")

if ism in ismlar:
    print("Bu ism ro‘yxatda bor!")
else:
    print("Bu ism ro‘yxatda yo‘q!")










sonlar = [1, 2, 3, 4, 5]
sonlar.reverse()
print("Teskari tartib:", sonlar)









