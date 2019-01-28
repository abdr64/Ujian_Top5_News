import requests

apiKey = 'c0d4d56e89f84305b8ad0bf41093534c'

uTech = 'https://newsapi.org/v2/top-headlines?country=id&category=technology&apiKey='+apiKey
uBusiness = 'https://newsapi.org/v2/top-headlines?country=id&category=business&apiKey='+apiKey
uSports = 'https://newsapi.org/v2/top-headlines?country=id&category=sports&apiKey='+apiKey
uHealth = 'https://newsapi.org/v2/top-headlines?country=id&category=health&apiKey='+apiKey
uScience = 'https://newsapi.org/v2/top-headlines?country=id&category=science&apiKey='+apiKey

teknologi = requests.get(uTech)
bisnis = requests.get(uBusiness)
olahraga = requests.get(uSports)
kesehatan = requests.get(uHealth)
sains = requests.get(uScience)

p1 = teknologi.json()
p2 = bisnis.json()
p3 = olahraga.json()
p4 = kesehatan.json()
p5 = sains.json()

print('Selamat datang, mau tahu berita apa hari ini?')
print('[1]  Berita seputar teknologi')
print('[2]  Berita seputar bisnis')
print('[3]  Berita seputar olahraga')
print('[4]  Berita seputar kesehatan')
print('[5]  Berita seputar science')

pilihan = int(input('Ketik pilihan Anda [1/2/3/4/5] : '))

if pilihan == 1:
    print('Berikut adalah top 5 berita Indonesia bidang teknologi :')
    for urut in range(5):
        print(urut+1,' - ',p1['articles'][urut]['title'])
elif pilihan == 2:
    print('Berikut adalah top 5 berita Indonesia bidang bisnis :')
    for urut in range(5):
        print(urut+1,' - ',p2['articles'][urut]['title'])
elif pilihan == 3:
    print('Berikut adalah top 5 berita Indonesia bidang olahraga :')
    for urut in range(5):
        print(urut+1,' - ',p3['articles'][urut]['title'])
elif pilihan == 4:
    print('Berikut adalah top 5 berita Indonesia bidang kesehatan :')
    for urut in range(5):
        print(urut+1,' - ',p4['articles'][urut]['title'])
elif pilihan == 5:
    print('Berikut adalah top 5 berita Indonesia bidang science :')
    for urut in range(5):
        print(urut+1,' - ',p5['articles'][urut]['title'])