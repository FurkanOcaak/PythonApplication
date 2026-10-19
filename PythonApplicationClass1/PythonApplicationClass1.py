"""STRING YAPISI"""

baslık = "title"
vade = 10
faizOrani = 2.34

print(baslık)
print(faizOrani)

print(type(faizOrani))

print("baslık is : " + baslık)

""" SART BLOKLARI """

dolarDun = 4.32
dolarBugun = 4.32

if dolarDun>dolarBugun :
    print("azalış")
    
elif dolarBugun> dolarDun :
    print("artış")
    
elif dolarDun==dolarBugun:
    print("eşit")
    
else : 
    print("mümkün değil")
    
    
""" DIZILER VE DÖGÜLER """

krediler = ["a kredi", "b kredi", "c kredi"]

print(krediler[0] + " alana " + krediler[2] + " %2 indirimli"  )

for kredi in krediler :
    print(kredi)

""""FONKSIYONLAR"""

def kredilerilistele():
    krediler = ["a kredi", "b kredi", "c kredi"]
    for x in krediler:
        print(x)
    
kredilerilistele()








