from operator import index

bolalar =[ "ali" , "ayu" , "man" ]
qizlar =[ "muhtasar", "mubina", "jasmina"]
Atalash =[ "ali", "jasmina" , "muhtasar" ]

print(bolalar)
print(qizlar)
print(Atalash)

bolalar = [ "ali" , "ayu" , "man" ]

print(bolalar[0])  #birinchi element
print(bolalar[2])  #uchinchi element
print(bolalar[-1])  #ohirgi element


bolalar = [ "ali" , "ayu" , "man" ]

bolalar[1] = "jasmina"
print(bolalar)




bolalar = [ "ali" , "ayu" , "man" ]

bolalar.append("ikkichi")                     # ohiriga qoshadi
bolalar.insert(0,"ikkichi")   # 1-indexga qosahadi
bolalar.remove("man")                     # "man"i ochiradi
ohirgi = bolalar.pop()                      # ohirgi elementni ochiradi

print(bolalar)
print("ohirgi element: ", ohirgi)



bolalar = [ "ali" , "ayu" , "man" ]
for bola in bolalar:
    print("Men yahshi koraman:", bola)




    bolalar = [ "ali" , "ayu" , "man" , "san"]
    print(len(bolalar))




    bolalar = []
    for i  in range(3):
     bola = input(f"{i + 1}-bola kiriting: ")
     bolalar.append(bola)
     print("siz kiritgan royhat:", bolalar)



print("1-bola", bolalar[0])
print("ohirgi bola:",bolalar[-1])




yangi_bola = input("yangi bola kiriting: ")
bolalar.append(yangi_bola)
print("Yangilangan royhat:", bolalar)




index = int( input("Qaysi elementni ozgartirmoqchisiz (0,1,2...): "))
yangi = input("Yangi qiymatni kiriting: ")
bolalar[index] = yangi
print("Yangilanagan royhat:", bolalar)



ochirish = input("O'chiriladigan elementni kiriting: ")
bolalar.remove(ochirish)
print("O'chirilgandan keyin:", bolalar)


print("Ro'yhatdagi elementlar soni:", len(bolalar))















