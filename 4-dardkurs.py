# from xml.dom.minidom import ProcessingInstruction
#
# yigindi = 0
# son = int(input("Son kirit: "))
# f = 0
# j =0
# z = 0
# v = 0
# for telefon in range(1, son + 1):
#     if telefon % 2 == 0:
#         f += telefon
#         z+= 1
#
#     elif telefon % 2 == 1:
#         j += telefon
#         v+= 1
# print("Juft sonlar yigindisi: ", f)
# print("toq sonlar yigindisi: ", j)
# print("Juft sonlar soni:", z)
# print("toq sonlar soni: ", v)
#


toq_sonlar_soni = 0
juft_sonlar_soni = 0
toq_yigindi = 0
juft_yigindi = 0

while True:
    son = int(input("Son kiriting (0 - to‘xtatish): "))

    if son == 0:
        break  # 0 kiritilganda dastur to‘xtaydi

    if son % 2 == 0:
        juft_sonlar_soni += 1
        toq_yigindi += son
    else:
        toq_sonlar_soni += 1
        juft_yigindi += son

print("/n Natija:")
print(f"Toq sonlar soni: {toq_sonlar_soni}")
print(f"Toq sonlar yig‘indisi: {toq_yigindi}")
print(f"Juft sonlar soni: {juft_sonlar_soni}")
print(f"Juft sonlar yig‘indisi: {juft_yigindi}")



















