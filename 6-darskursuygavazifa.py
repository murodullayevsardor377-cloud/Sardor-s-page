umumiy = 0

while True:
    metr = int(input("Necha metr yugurdingiz? "))
    if metr == 0:
        print("Yugurish tugadi")
        break
    umumiy += metr

print("Umumiy yugurilgan masofa:", umumiy, "metr")



umumiy = 0

while True:
    narx = int(input("Mahsulot narxini kiriting: "))
    if narx < 0:
        print("Xarid tugadi")
        break
    if narx == 0:
        continue
    umumiy += narx

print("Umumiy summa:", umumiy, "so'm")




n = int(input("n sonini kiriting: "))
sanoq = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        sanoq += 1

print("Juft sonlar soni:", sanoq)





umumiy = 0

while True:
    yo_lovchi = int(input("Yo'lovchilar sonini kiriting: "))
    if yo_lovchi == -1:
        print("Kirish tugadi")
        break
    umumiy += yo_lovchi
    if umumiy >= 50:
        print("Avtobus to'ldi")
        break

print("Umumiy yo'lovchilar soni:", umumiy)






print(i)


n = int(input("Son kiriting: "))

for i in range(n, 0, -1):
    if i == 3:
        continue


