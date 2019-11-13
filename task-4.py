hauer1 = input("Ведите часы минуты и секунды через пробел: ").split()
hauer1_1 = int(hauer1[0])*60*60
hauer1_2 = int(hauer1[1])*60
hauer1_3 = int(hauer1[2])
sec1 = hauer1_1+hauer1_2+hauer1_3
hauer2 = input("Ведите часы минуты и секунды через пробел: ").split()
hauer2_1 = int(hauer2[0])*60*60
hauer2_2 = int(hauer2[1])*60
hauer2_3 = int(hauer2[2])
sec2 = hauer2_1+hauer2_2+hauer2_3
raz = sec1-sec2
print("Разница в секундах:", abs(raz))