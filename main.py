import fastapi as _fastapi
import json
from typing import Optional
from fastapi import Query


app = _fastapi.FastAPI()


with open('halfiyatlari.json','r') as f:
    fiyatlar = json.load(f)

@app.get("/")
def root():
    return fiyatlar


#tüm ürünler ve arama için
@app.get('/tumhallersearch',status_code=200)
def search_urun(name: Optional[str] = Query(None, title="Name",description="Aranacak Ürün Giriniz.")):
    if name is None:
        return {"Aradığınız Ürün Bulunamadı"}
    else:
        people2 = [p for p in fiyatlar if name.lower() in p ['urunismi'].lower()]
        return people2

@app.get('/all',status_code=200)
def butun_urunler():
    return fiyatlar


@app.get('/ankara',status_code=200)
def ankara_urunler(name: Optional[str] = Query(None, title="Name",description="Aranacak Ürün Giriniz.")):
    if name is None:
        tumankara = [p for p in fiyatlar if 'Ankara'.lower() in p ['halismi'].lower()]
        return tumankara
    else:
        tumankara = [p for p in fiyatlar if 'Ankara'.lower() in p ['halismi'].lower()]
        urun = [p for p in tumankara if name.lower() in p ['urunismi'].lower()]
        return urun

@app.get('/malatya',status_code=200)
def ankara_urunler(name: Optional[str] = Query(None, title="Name",description="Aranacak Ürün Giriniz.")):
    if name is None:
        tumankara = [p for p in fiyatlar if 'Malatya'.lower() in p ['halismi'].lower()]
        return tumankara
    else:
        tumankara = [p for p in fiyatlar if 'Malatya'.lower() in p ['halismi'].lower()]
        urun = [p for p in tumankara if name.lower() in p ['urunismi'].lower()]
        return urun

@app.get('/izmir',status_code=200)
def ankara_urunler(name: Optional[str] = Query(None, title="Name",description="Aranacak Ürün Giriniz.")):
    if name is None:
        tumankara = [p for p in fiyatlar if 'İzmir'.lower() in p ['halismi'].lower()]
        return tumankara
    else:
        tumankara = [p for p in fiyatlar if 'İzmir'.lower() in p ['halismi'].lower()]
        urun = [p for p in tumankara if name.lower() in p ['urunismi'].lower()]
        return urun


@app.get('/denizli',status_code=200)
def ankara_urunler(name: Optional[str] = Query(None, title="Name",description="Aranacak Ürün Giriniz.")):
    if name is None:
        tumankara = [p for p in fiyatlar if 'Denizli'.lower() in p ['halismi'].lower()]
        return tumankara
    else:
        tumankara = [p for p in fiyatlar if 'Denizli'.lower() in p ['halismi'].lower()]
        urun = [p for p in tumankara if name.lower() in p ['urunismi'].lower()]
        return urun

@app.get('/adana',status_code=200)
def ankara_urunler(name: Optional[str] = Query(None, title="Name",description="Aranacak Ürün Giriniz.")):
    if name is None:
        tumankara = [p for p in fiyatlar if 'Adana'.lower() in p ['halismi'].lower()]
        return tumankara
    else:
        tumankara = [p for p in fiyatlar if 'Adana'.lower() in p ['halismi'].lower()]
        urun = [p for p in tumankara if name.lower() in p ['urunismi'].lower()]
        return urun

@app.get('/gaziantep',status_code=200)
def ankara_urunler(name: Optional[str] = Query(None, title="Name",description="Aranacak Ürün Giriniz.")):
    if name is None:
        tumankara = [p for p in fiyatlar if 'Gaziantep'.lower() in p ['halismi'].lower()]
        return tumankara
    else:
        tumankara = [p for p in fiyatlar if 'Gaziantep'.lower() in p ['halismi'].lower()]
        urun = [p for p in tumankara if name.lower() in p ['urunismi'].lower()]
        return urun


@app.get('/hatay',status_code=200)
def ankara_urunler(name: Optional[str] = Query(None, title="Name",description="Aranacak Ürün Giriniz.")):
    if name is None:
        tumankara = [p for p in fiyatlar if 'Hatay'.lower() in p ['halismi'].lower()]
        return tumankara
    else:
        tumankara = [p for p in fiyatlar if 'Hatay'.lower() in p ['halismi'].lower()]
        urun = [p for p in tumankara if name.lower() in p ['urunismi'].lower()]
        return urun


@app.get('/kayseri',status_code=200)
def ankara_urunler(name: Optional[str] = Query(None, title="Name",description="Aranacak Ürün Giriniz.")):
    if name is None:
        tumankara = [p for p in fiyatlar if 'Kayseri'.lower() in p ['halismi'].lower()]
        return tumankara
    else:
        tumankara = [p for p in fiyatlar if 'Kayseri'.lower() in p ['halismi'].lower()]
        urun = [p for p in tumankara if name.lower() in p ['urunismi'].lower()]
        return urun



@app.get('/trabzon',status_code=200)
def ankara_urunler(name: Optional[str] = Query(None, title="Name",description="Aranacak Ürün Giriniz.")):
    if name is None:
        tumankara = [p for p in fiyatlar if 'Trabzon'.lower() in p ['halismi'].lower()]
        return tumankara
    else:
        tumankara = [p for p in fiyatlar if 'Trabzon'.lower() in p ['halismi'].lower()]
        urun = [p for p in tumankara if name.lower() in p ['urunismi'].lower()]
        return urun


@app.get('/kütahya',status_code=200)
def ankara_urunler(name: Optional[str] = Query(None, title="Name",description="Aranacak Ürün Giriniz.")):
    if name is None:
        tumankara = [p for p in fiyatlar if 'Kütahya'.lower() in p ['halismi'].lower()]
        return tumankara
    else:
        tumankara = [p for p in fiyatlar if 'Kütahya'.lower() in p ['halismi'].lower()]
        urun = [p for p in tumankara if name.lower() in p ['urunismi'].lower()]
        return urun
