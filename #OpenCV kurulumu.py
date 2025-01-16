#OpenCV kurulumu

import cv2 #openCv 

#kamera açma kodu
vid = cv2.VideoCapture(0) #vi
while True: #kameradan sürekli görüntü almak için kullanılır.
    ret,frame = vid.read() #ret, kamera çalışıyor mu kontrol eder.
    #frame alınan görüntü karesi
    cv2.imshow('from', frame) #alınan görüntü from başlıklı pencerede gösterilir.
    if cv2.waitKey(1)& 0xFF == ord('q'): #q basıldığında döngüden çıkar.
        break
vid.release #kamera serbest bırakılır
cv2.destroyAllWindows()
