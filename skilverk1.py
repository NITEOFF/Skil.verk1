import math

# Artjom Pushkar 29.08.22


#Lidur 1: Nafn

print ("\n")
upphaldsfag = (input("hvad er upphaldsfag? "))
nafnid = (input("hvad er nafnid fitt? "))
print ("\n")
print("Velkomin í " + upphaldsfag + " þetta verður skemmtileg önn hjá okkur " + nafnid)
print ("\n")


# Lidur 2: Heiltölur


print ("\n")
math1 = int(input("tala 1 = "))
math2 = int(input("tala 2 = "))
print ("\n")

print ( "A) " + str(math1*math2) )
print ( "B) " + str(math1-math2) )
print ( "C) " + str(math1//math2) )
print ( "D) " + str(math1%math2) )
print ("\n")


#Lidur 3: Hringur


math3 = int(input("tala 1= "))
math4 = int(input("tala 2= "))
print ("\n")
print (" Ummal = " + str(math3*math4*math.pi ) + " Flatarmal = " + str(math3*math4*math.pi))
print ("\n")


#Lidur 4: Aldur

boarndate1 = int(input("Skrifadu þegar þu faeddist: "))
boarndate2 = int(input("Skrifadu þegar pabbi þinn faeddist: "))
print ("\n")
print("Pabbi þinn var " + str(boarndate1-boarndate2 ) + " gamall")
print ("\n")


#Lidur 5: Meðalaldur


person1 = int(input("aldur 1= "))
person2 = int(input("aldur 2= "))
person3 = int(input("aldur 2= "))
print ("\n")
all_age = person1 + person2 + person3
full_age = all_age/3

print("persona 1 = " + str(person1))
print("persona 2 = " + str(person2))
print("persona 3 = " + str(person3))
print ("\n")
print("Saman = " + str(all_age))
print("Meðalaldur = " + str(full_age))
print ("\n")



#Lidur 6: Miðju tala


n1 = int(input("tala 1: "))
n2 = int(input("tala 2: "))
n3 = int(input("tala 3: "))
print ("\n")
if n1 > n2 and n1 > n3:
    if n2 > n3:
        print("tala 2 er i midju")
    else:
        print("tala 3 er i mdiju")
        
if n3 > n2 and n3 > n1:
    if n1 > n2:
        print("tala 1 er i midju")
    else:
        print("tala 2 er i mdiju")
        
if n2 > n1 and n2 > n3:
    if n1 > n3:
        print("tala 1 er i midju")
    else:
        print("tala 3 er i mdiju")
print ("\n")


# LIDUR 7: Tommur - Sentimetra
tommur = 0
cm = 0
mode = input("C for cm - T for tommur: ")

if mode == "c":
     fjolda_tomma = int(input("Fjolda tomma: "))
     cm = fjolda_tomma*2.54
     tommur = fjolda_tomma
     print(fjolda_tomma, "Tommur =", round(cm, 2), "cm")
elif mode == "t":
     fjolda_cm = int(input("Fjolda cm: "))
     cm = fjolda_cm
     tommur = fjolda_cm/2.54
     print(fjolda_cm, "cm =", round(tommur, 2), "tommur")
else:
     print("Villa!")
print ("\n")


# Lidur 8: Árstíðir
numberr = int(input("Hver er tíminn: "))

if numberr == 1 or numberr == 2 or numberr == 3:
     print("Nú er daginn tekið að lengja")
elif numberr == 4 or numberr == 5:
     print("Vorið er komið og grundirnar gróa")
elif numberr == 6 or numberr == 7 or numberr == 8:
     print("Núna er sumarið komið með blóm í haga")
elif numberr == 9 or numberr == 10:
     print("Núna er haustið gengið í garð")
elif numberr == 11 or numberr == 12:
     print("Núna styttist í jólin")
else: numberr <= 0 or numberr >= 13
print("Rangur innsláttur")
print ("\n")

     
     


# Lidur 9: Talnabil
numv = int(input(" < 0 eða > 10 = "))

if numv <= 0 or numv >= 10:
     print("Gott")
else:
     print("Þessi tala er lægri en 0 eða hærri 10")
print ("\n")


# Lidur 10: nofn
name11 = (input("Skrifaðu nafn: "))
name22 = (input("Sláðu inn annað nafn: "))

if name11 == name22:
     print(name11, "og", name22, "er sama nafnid")
else:
     print(name11, "og", name22, "er ekki somu nofnin")