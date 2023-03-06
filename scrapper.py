import pandas as pd
from bs4 import BeautifulSoup
import requests
import random


dict1 = {'url2': 'https://ankara.bel.tr/hal-fiyatlari', 'il2': 'Ankara'}
dict2 = {'url2': 'https://biizmir.com/hal-fiyatlari', 'il2': 'İzmir'}
dict3 = {'url2': 'https://www.bimalatya.com/hal-fiyatlari', 'il2': 'Malatya'}
dict4 = {'url2': 'https://denizli.bel.tr/Default.aspx?k=halfiyatlari','il2': 'Denizli'}
dict5 = {'url2': 'https://www.biadana.com/hal-fiyatlari', 'il2': 'Adana'}
dict6 = {'url2': 'https://www.bikonya.com/hal-fiyatlari', 'il2': 'Konya'}
dict7 = {'url2': 'https://www.biantep.com/hal-fiyatlari', 'il2': 'Gaziantep'}
dict8 = {'url2': 'https://www.bihatay.com/hal-fiyatlari', 'il2': 'Hatay'}
dict9 = {'url2': 'https://www.kayseri.bel.tr/hal-fiyatlari', 'il2': 'Kayseri'}
dict10 = {'url2': 'https://www.bitrabzon.com/hal-fiyatlari', 'il2': 'Trabzon'}
dict11 = {'url2': 'https://www.kutahya.bel.tr/hal.asp', 'il2': 'Kütahya'}


def _scrape_data(url2, il2):
    url = url2
    il = il2
    file1 = open('user-agents.txt', 'r')
    Lines = file1.readlines()
    random_user_agent = random.choice(Lines)
    header = {
        'User-Agent': random_user_agent.strip()
    }
    response = requests.get(url, headers=header)

    hal_ismi = []
    urun_ismi = []
    en_dusuk_fiyat = []
    en_yuksek_fiyat = []
    birim = []

    html_content = response.content
    html_content_string = response.text

    soup = BeautifulSoup(html_content, 'html.parser')
    tables = soup.select('table')
    for oneeach in tables:
        for row in oneeach.findAll('tr'):
            columns = row.findAll('td')
            if (il == 'Çorum'):
                pass
            if (columns != []):
                hal_ismi.append(il)
                if (len(columns) < 4):
                    birim.append('Kg/Adet')
                    urun_ismi.append(columns[0].text)
                    en_dusuk_fiyat.append(columns[1].text.strip())
                    en_yuksek_fiyat.append(columns[2].text.strip())
                else:
                    urun_ismi.append(columns[0].text)
                    en_dusuk_fiyat.append(columns[2].text.strip())
                    en_yuksek_fiyat.append(columns[3].text.strip())
                    birim.append(columns[1].text.strip())

    df = pd.DataFrame({'halismi': hal_ismi,
                       'urunismi': urun_ismi,
                       'birim': birim,
                       'endusukfiyat': en_dusuk_fiyat,
                       'enyuksekfiyat': en_yuksek_fiyat
                       })
    return df





def _kaydet():
    dataframe = pd.DataFrame()
    dizi = []
    sehirler = [dict1, dict2,dict3,dict4,dict5,dict6,dict7,dict8,dict9,dict10,dict11]
    for i in sehirler:
        for z in range(0,1):
            df = _scrape_data(**i)
            dizi.append(df)
    for i in dizi:
        dataframe = pd.concat([dataframe,i])

    result = dataframe.to_json(orient="records")
    with open(f"halfiyatlari.json", "w") as file:
        file.write(result)
        file.close()

if __name__ == "__main__":
    _kaydet()
