#Mathplotlib Kullanımı
#Veri görselleştirmesi için kullanılan kütüphane.
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('insurance.csv')
print(df.head(3))

#grafikleştirme
plt.figure(figsize=(12,6)) #grafik boyutu
plt.plot(df.age,df.bmi) #x,y belirleme
plt.show()
