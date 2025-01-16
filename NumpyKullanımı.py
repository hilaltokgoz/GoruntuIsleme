#Numpy Kullanımı
#çok boyutlu dizi, matris ile çalışmayı sağlayan,matematiksel işlem yapabileceğimiz Python kütüphanesi.
import numpy as np

arr = np.array([1,2,3,4,5])
print(arr)
print(type(arr))

#elemanlarını otomatik 0 oluşturabilecedk kod
arr = np.zeros((3,4))
print(arr) 
#[[0. 0. 0. 0.]
#[0. 0. 0. 0.]
#[0. 0. 0. 0.]]

#arange 
arr = np.arange(10,100,10)
print(arr) #[10 20 30 40 50 60 70 80 90]

