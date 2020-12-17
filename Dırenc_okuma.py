#Direnç Değeri okuma programı
#Harun GÖÇMEN
# Direnç renk kodlarına göre ohm değerini bulma
"""        .. Bilgilendirme Notu ..
    Siyah= 0        Çarpanı = 10^0   tolerans= -
    Kahverengi= 1   Çarpanı = 10^1   tolerans= %1
    Kırmızı = 2     Çarpanı = 10^2   tolerans= %2
    Turuncu = 3     Çarpanı = 10^3   tolerans= -
    Sarı = 4        Çarpanı = 10^4   tolerans= -
    Yeşil = 5       Çarpanı = 10^5   tolerans= %0.5
    Mavi = 6        Çarpanı = 10^6   tolerans= %0.25
    Mor = 7         Çarpanı = 10^7   tolerans= 0.1
    Gri = 8         Çarpanı = 10^8   tolerans= -
    Beyaz = 9       Çarpanı = 10^9   tolerans= -
    Altın=  -       Çarpanı = 0.1    tolerans= %5
    Gümüş =  -      Çarpanı = 0.01   tolerans= %10
4 bantlı , 5 bantlı , 6 bantlı dirençler olabilmektedir.
"""
sayılar = [] #Sayıların renkleri bu listeye eklenecek
sayılardeg = [] #Sayılarun renklerinin değeri bu listeye eklenecek
carpan = [] # arpan rengi buraya eklenecektir.
kac = int(input("Direnç üzerinde kaç tane renk bandı bulunmaktadır yazınız: "))
if(kac==4 or kac==5 or kac==6):  #Eğer girilen direnç değeri 4,5,6 değerlerinden biri ise
    for i in range(kac): # i saymaya 0 dan başlar DİKKATTT !!!
                         # girilen kac değerinin uzunluğunda for döngüsü oluşturuldu.
        renk  = input("lütfen "+ str(i+1) + ". rengi yazınız: ")
        if(i==0):                sayılar.append(renk) #ilk direnc rengini sayılar listesine ekler.
        if(i==1):                sayılar.append(renk) #ikinci direnc değerini sayılar listesine ekler.
        if(i==2 and kac ==4):    carpan.append(renk)  #Eğer 4 bantlı bir sistem ise 3. renk çarpan listesine eklenir.
        if(i==2 and kac>4 ):     sayılar.append(renk) #Eğer bant sayısı 4 ten büyükse 3. renk sayılar listesine eklenir.
        if(i==3 and kac ==5):    carpan.append(renk) #5 batlı bir sistem ise 4. renk carpan listesine eklenir.
        if(i==3 and kac >5):     sayılar.append((renk)) #6 bantlı bir sistem ise 4. renk sayılar listesine eklenecektir.
        if(i==4 and kac==6):     carpan.append(renk) # 6 bantlı bir sistem ise 5. renk carpan listesine eklenir.

    for a in sayılar: # a parametresi sayılar listesinde döner!
        #Sayılar listesine eklenen renklerin değerlerini tespit etmek amacıyla for döngüsü sayılar içerisinde göner.
        # rengine göre sayının değeri sayılardeg listesine aktarılma işlemi aşağıda gerçekleştirilmiştir.
        if (a == "siyah"):       sayılardeg.append(0)
        if (a == "kahve"):       sayılardeg.append(1)
        if (a == "kırmızı"):     sayılardeg.append(2)
        if (a == "turuncu"):     sayılardeg.append(3)
        if (a == "sarı"):        sayılardeg.append(4)
        if (a == "yeşil"):       sayılardeg.append(5)
        if (a == "mavi"):        sayılardeg.append(6)
        if (a == "mor"):         sayılardeg.append(7)
        if (a == "gri"):         sayılardeg.append(8)
        if (a == "beyaz"):       sayılardeg.append(9)

    if(carpan[0]=="siyah"):   carpandeg = 10**0 # çarpan listesindeki renge göre değer ataması yapılır.
    if(carpan[0]=="kahve"):   carpandeg = 10**1
    if(carpan[0]=="kırmızı"): carpandeg = 10**2
    if(carpan[0]=="turuncu"): carpandeg = 10**3
    if(carpan[0]=="sarı"):    carpandeg = 10**4
    if(carpan[0]=="yeşil"):   carpandeg = 10**5
    if(carpan[0]== "mavi"):   carpandeg = 10**6
    if(carpan[0]=="mor"):     carpandeg = 10**7
    if(carpan[0]=="gri"):     carpandeg = 10**8
    if(carpan[0]=="beyaz"):   carpandeg = 10**9

    print(str(sayılar)+ ":  Sayıların renkleridir ..")
    print(str(carpan)+ ":  Çarpanın renkleridir ..")
    print(str(sayılardeg)+ ":  Sayıların değeridir ..")
    print(str(carpandeg)+ ": Çarpan değeridir ..")
    if(kac==4 ): # Eğer bant sayısı 4 ise
        k = ( sayılardeg[0]*10 + sayılardeg[1] ) * carpandeg
    if(kac== 5): # Eğer bant sayısı 5 ise
        k = ( sayılardeg[0]*100+ sayılardeg[1]*10+ sayılardeg[2] ) * carpandeg
    if(kac== 6): # Eğer bant sayısı 6 ise
        k = ( sayılardeg[0]*1000 + sayılardeg[1]*100 + sayılardeg[2]*10+ sayılardeg[3] ) * carpandeg
    print("...... "+str(k) +"ohm direnç değeridir .......")
else:
    print(".....  Yanlış Giriş .....")
