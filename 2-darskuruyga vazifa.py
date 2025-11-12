# Sonlarning yig'indisini hisoblash dasturi
# 0 kiritilganda dastur to'xtaydi

umumiy_yigindi = 0
toq_yigindi = 0
juft_yigindi = 0

while True:
    son = int(input("Son kiriting (0 - to'xtatish uchun): "))
    if son == 0:
        break
    umumiy_yigindi += son
    if son % 2 == 0:
        juft_yigindi += son
    else:
        toq_yigindi += son

print("\nNatijalar:")
print(f"Umumiy yig'indi: {umumiy_yigindi}")
print(f"Toq sonlar yig'indisi: {toq_yigindi}")
print(f"Juft sonlar yig'indisi: {juft_yigindi}")
