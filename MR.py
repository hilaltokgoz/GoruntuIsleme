#MR' daki beyaz alan yüzdesi hesaplama

import cv2
import numpy as np

img = cv2.imread('mr.jpg')
img_gray = cv2.imread('mr.jpg',0)

# Görüntünün boyutlarını kontrol etme
height, width = img_gray.shape  # Görüntü yüksekliği ve genişliği
total_pixels = height * width  # Toplam piksel sayısı
print(f"Görüntüdeki toplam piksel sayısı: {total_pixels}") #Görüntüdeki toplam piksel sayısı: 314405

white_pixels = np.sum(img_gray == 255)# Beyaz piksellerin sayısını hesaplam
print(f"Beyaz piksel sayısı: {white_pixels}") #Beyaz piksel sayısı: 37622

# Beyaz alanın toplam alana oranı (yüzde hesaplama)
white_area_percentage = (white_pixels / total_pixels) * 100
print(f"Beyaz alanın yüzdesi: {white_area_percentage:.2f}%") #Beyaz alanın yüzdesi: 11.97%

cv2.imshow('mr.jpg', img_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()