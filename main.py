meme_dict = 
{
    'gabut' : 'tidak ada kegiatan'
    'YGY' : 'ya guys ya'
    'mager' : 'malas gerak'
    'kepo' : 'pengen tahu aja'
    'mantul' : 'mantap betul'
    'santuy' : 'santai'
    'BTW' : 'ngomong-ngomong'
    'gercep' : 'gerak cepat'
    'gaje' : 'gak jelas'
    'japri' : 'jawab pribadi'
    'baper' : 'bawa perasaan'
    'halu' : 'halusinasi'
    
}

for i in range(5):
    word = input("Ketik kata yang kamu tidak mengerti:")
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print('kata tersebut tidak ada di kamus')








