import pandas as pd
import numpy as np

df = pd.read_csv('nba.csv')


#1- ilk 10 kaydı getiriniz.
result = df.head(10)

#2- Toplam kaç kayıt vardır.

result = len(df.index)

#3- Tüm oyuncuların toplam maaş ortalaması nedir ?

result = df['Points'].mean()

#4- En yüksek maaş ne kadardır.

result = df['Points'].max()

#5- En yüksek maaşı alan oyuncu kimdir ?

#result = df.groupby('Player')['Points'].max().head(1)
result = df[df['Points']==df['Points'].max()]['Player'].iloc[0] #sadece isim bilgisi

#6- Yaşı 20-25 arasında olan oyuncuların isim ve oynadıkları takımlar

result = df[(df['Age'] >= 20) & (df['Age'] <= 25)][['Player','Team','Age']]

#7- "Stephen Curry" isimli oyuncunun oynadıgı takım hangisidir ?

result = df[df.Player.str.contains('Stephen Curry')]['Team']

#8- Takımlara göre oyuncuların ortalama maaş bilgisi nedir?

result = df.groupby('Team')['Points'].mean()

#9 - kaç farklı takım mevcut

result = len(df.groupby('Team'))
result = df['Team'].nunique()  #yukarıdaki ile aynı

#10 - her takımda kaç oyuncu bulunmaktadır.

result = df.groupby('Team')['Player'].count()
result = df['Team'].value_counts() #yukarıdaki ile aynı

#11- İsmi içinde 'and' geçen kayıtları bulunuz.
df.dropna(inplace=True)    #orjinal liste değişsin diye
result = df[df.Player.str.contains('and')]

#def str_find(name):
#    if 'and' in name.lower():
#        return True
#    return False

#result = df[df['Player'].apply(str_find)]

print(result)
