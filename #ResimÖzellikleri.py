#Resim Özellikleri
import cv2

img = cv2.imread('fish.jpg')
img_gray = cv2.imread('fish_gray.jpg',0) #resmi gri yap
cv2.imwrite('fish_gray.jpg',img_gray) 

#item -> herhangi pikselin renk değeri çekilebilir 
#img.item(y,x,color)
print('Blue:' , img.item(150,100,0)) #Blue: 11
print('Green:' , img.item(150,100,1))#Green: 30
print('Red:' , img.item(150,100,2))#Red: 67
#100*150 pikselde her renkten ne kadar oranda kullanılmış

#itemset -> herhangi bir noktada değeri değiştirmeye yarayan yapı
#img.itemset((y,x,color),value) :koordinattaki hangi rengi değiştirip ne değer vericem
for y in range(50):
    for x in range (50):
     img[y, x, 0] = 255  #img.itemset((10,10,0),0)
     img[y, x, 1] = 255 
    img[y, x, 2] = 255 

#shape -> resim boyutunu görmeye yarar.
print(img.shape) #(218, 231, 3) #BGR 'dan 3 geliyor
print(img_gray.shape) #(218, 231) #renk tonu yok

#size -> piksel sayısını gösteren yapı. x*y+c
print(img.size) #151074
print(img_gray.size) #50358, color yok üçte biri

#datatype -> veri data tipini döner
print(img.dtype) #uint8

#ROI -> resimden bir parça alma mantığı
#roi = img[y1:y2,x1:x2] , 68:105, 60:115
roi = img [68:108,60:110]
cv2.imshow('fish_eye',roi)#sadece göz getirildi


img[0:40,0:50] = roi
cv2.imshow('fish',img) #şu koordinatlara balığın gözünü yapıştur


#renk filtresi -> istenilen renk yok edilebilir ya da baskın hale getirilebilir

img[:,:,0] =0 #maviyi yok et (kırmız, yeşil kalır)
img[:,:,1] =0 #yeşili de yok et(resim kırmızı)
img[:,:,2] =0 #kırızı da yok olsun(resim siyah)


cv2.imshow('fish',img)
cv2.waitKey(0)
cv2.destroyAllWindows()





