
doymak="hayır"
print("Pizzanız Afiyet olsun")
# while doymak=="hayır":
#   cevap=input("bir dilim daha pizza ister misiniz ? : ")
#   if cevap=="hayır":
#       break
#   else:
#       print("bir dilim daha geliyor.. ")

 #Farklı bi bakış
while doymak=="hayır":
    cevap=input("bir dilim daha pizza ister misiniz ? : ")
    if cevap=="evet":
        continue
    else:
        doymak="evet" 

