#Video Açma
import cv2

cap = cv2.VideoCapture('turtle.mp4')

if cap.isOpened() == False:
    print('Video Bulunamadı')


while cap.isOpened(): #video açılırsa true dön
    ret, frame = cap.read()

    if ret == True:
        cv2.imshow('frame',frame)

        kInp = cv2.waitKey(24) #video normal hızla döner
        if kInp == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()