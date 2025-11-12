# 1. Foydalanuvchidan shahar nomini so‘raymiz
shahar = input("Shahar nomini kiriting: ")

# 2. Ob-havo ma’lumotlarini soxta bazadan olamiz
if shahar.lower() == "toshkent":
    temp = 27
    holat = "Quyoshli"
elif shahar.lower() == "samarqand":
    temp = 25
    holat = "Bulutli"
elif shahar.lower() == "buxoro":
    temp = 30
    holat = "Issiq"
elif shahar.lower() == "andijon":
    temp = 24
    holat = "Yomg‘irli"
elif shahar.lower() == "namangan":   # 🔹 Bu joy oldin xato edi
    temp = 28
    holat = "Quyoshli"
else:
    temp = "Noma’lum"
    holat = "Bu shahar bo‘yicha ma’lumot yo‘q"

# 3. Natijani chiqaramiz
print(f"\n🌆 {shahar} shahri uchun ob-havo:")
print(f"Harorat: {temp}°C")
print(f"Holat: {holat}")
