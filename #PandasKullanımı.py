#Pandas Kullanımı
#Veri işleme ve analizi için kullanılır

import pandas as pd

personel_list = { 'ad':['hilal','ibrahim','ali','veli'],
                 'yas':[26,30,14,31],
                 'maas':[5000,1000,3000,2000]}
print(type(personel_list)) #<class 'dict'>, dictionary öz. liste elemanı

df = pd.DataFrame(personel_list)
print(df)