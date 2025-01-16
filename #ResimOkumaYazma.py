#Resim Okuma Yazma

import cv2 #opencv 

#Görseli Alır
img = cv2.imread('mi.jpeg')
cv2.imshow('Profil', img)

#Görseli Direkt Gri Alır.
#img = cv2.imread('mi.jpeg',cv2.IMREAD_GRAYSCALE) # =img = cv2.imread('mi.jpeg',0)
#cv2.imshow('Profil', img)

#resmi kapatma
cv2.waitKey(0) #event gelene kadar resim durur
cv2.destroyAllWindows()

#koşula bağlı  kapanma istersek
# kInp = cv2.waitKey(0) 
# if kInp == ord('a'): 
#     print('a tusunua basıldı')
# else:
#     print('Baska tusa basıldı')
# cv2.destroyAllWindows()

#resmi kaydetme
img = cv2.imread('mi.jpeg',cv2.IMREAD_GRAYSCALE)
cv2.imwrite('mi2.jpeg',img) #mi2 de kaydedildi

