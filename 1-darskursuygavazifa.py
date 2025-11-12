import random

# 1. Foydalanuvchidan shahar nomini so‘raymiz
shahar = input("Shahar nomini kiriting: ")

# 2. Ob-havo holatlari ro‘yxati
holatlar = ["Quyoshli", "Bulutli", "Yomg‘irli", "Shamolli", "Issiq", "Sovuq"]

# 3. 5 kunlik prognoz tayyorlaymiz
print(f"\n🌆 {shahar.title()} shahri uchun 5 kunlik ob-havo prognozi:\n")

for kun in range(1, 6):
    # Har bir kunga tasodifiy harorat va holat tanlaymiz
    temp = random.randint(15, 35)  # 15°C dan 35°C gacha
    holat = random.choice(holatlar)
    print(f"{kun}-kun: {temp}°C, {holat}")







9



ball = int(input("bitta son yozing : "))
if ball >= 100:
    print("A'lo")
elif ball >= 80:
    print("Yahshi")
elif ball >= 60:
    print("Chidasa boladigan darajada")
else:print("(Yomon)")

