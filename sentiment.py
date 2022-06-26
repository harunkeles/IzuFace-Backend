import pandas as pd
import re
from textblob import TextBlob, Word
import nltk
from nltk.corpus import stopwords
import json as js
import numpy as np

import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download('omw-1.4')


def sentiment(data):
    try:
        # noktalama işaretleri
        data = data.replace('[^\w\s]', '')
        # sayılar
        data = data.replace('\d', '')
        # stopwords
        sw = stopwords.words('english')
        data = re.sub("[^\w]", " ",  data).split()

        abc = []
        # buyuk-kucuk donusumu
        for i in data:
            abc.append(i.lower())

        olumlu_yazilar = []
        olumlu_sonuc = []
        olumsuz_yazilar = []
        olumsuz_sonuc = []
        yorumsuz = []

        for yazı in abc:
            if yazı:
                blob1 = TextBlob(yazı)
                blob_eng = blob1.translate(from_lang='tr', to='en')

                if(blob_eng.polarity > 0):
                    olumlu_yazilar.append(yazı)
                    olumlu_sonuc.append(blob_eng.sentiment)

                elif(blob_eng.polarity < 0):
                    olumsuz_yazilar.append(yazı)
                    olumsuz_sonuc.append(blob_eng.sentiment)

                else:
                    yorumsuz.append(yazı)

        def myFunc(res):
            print("resresresresresresresresresresresres : ", res)
            if res >= -1 and res < -0.4:
                return 5
            elif res >= -0.4 and res < -0:
                return 4
            elif res >= -0 and res < 0.5:
                return 3
            elif res >= 0.5 and res < 0.7:
                return 2
            elif res >= 0.7 and res <= 1:
                return 1

        print("olumlu_sonuc : ", olumlu_sonuc)
        print("olumsuz_sonuc : ", olumsuz_sonuc)

        if len(olumlu_sonuc) > 0 and len(olumsuz_sonuc) <= 0:
            return myFunc(olumlu_sonuc[0].polarity)
        elif len(olumsuz_sonuc) > 0 and len(olumlu_sonuc) <= 0:
            return myFunc(olumsuz_sonuc[0].polarity)
        elif len(olumsuz_sonuc) <= 0 and len(olumlu_sonuc) <= 0:
            return 3
        else:
            res = float(olumlu_sonuc[0].polarity) + \
                float(olumsuz_sonuc[0].polarity)
            return myFunc(res)

    except:
        print("hata")
        return 3
