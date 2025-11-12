mevalar = ["olma", "banan", "shaftoli", "gilos"]
sonlar = [1, 2, 3, 4, 5]
aralash = ["Salom", 25, True, 3.14]

print(mevalar)
print(sonlar)
print(aralash)


mevalar = ["olma", "banan", "shaftoli", "gilos"]

print(mevalar[0])   # birinchi element
print(mevalar[2])   # uchinchi element
print(mevalar[-1])  # oxirgi element


mevalar = ["olma", "banan", "shaftoli", "gilos"]

mevalar[1] = "anor"
print(mevalar)



mevalar = ["olma", "banan", "shaftoli"]

mevalar.append("gilos")   # oxiriga qo‘shadi
mevalar.insert(1, "anor") # 1-indexga qo‘shadi
mevalar.remove("banan")   # "banan"ni o‘chiradi
oxirgi = mevalar.pop()    # oxirgi elementni o‘chiradi

print(mevalar)
print("Oxirgi element:", oxirgi)



mevalar = ["olma", "banan", "shaftoli"]

for meva in mevalar:
    print("Men yaxshi ko‘raman:", meva)




mevalar = ["olma", "banan", "shaftoli", "gilos"]
print(len(mevalar))



mevalar = []

for i in range(3):
    meva = input(f"{i+1}-mevani kiriting: ")
    mevalar.append(meva)

print("Siz kiritgan ro‘yxat:", mevalar)




print("1-meva:", bolalar[0])
print("Oxirgi meva:", bolalar[-1])




yangi_meva = input("Yangi bola kiriting: ")
mevalar.append(yangi_meva)
print("Yangilangan ro‘yxat:", mevalar)



index = int(input("Qaysi elementni o‘zgartirmoqchisiz (0,1,2...): "))
yangi = input("Yangi qiymatni kiriting: ")
mevalar[index] = yangi
print("Yangilangan ro‘yxat:", mevalar)




ochirish = input("O‘chiriladigan elementni kiriting: ")
mevalar.remove(ochirish)
print("O‘chirilgandan keyin:", mevalar)




print("Ro‘yxatdagi elementlar soni:", len(mevalar))






