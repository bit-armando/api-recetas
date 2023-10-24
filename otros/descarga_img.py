import requests
import pandas as pd

df = pd.read_csv('../data/Blogs.csv') # Cargamos el csv
urls = df['img'].tolist()
title = df['title'].tolist()

carpeta_destino = '../data/imgs/' # crear carpeta imgs

i = 0
for url in urls:
    try:
        r = requests.get(url)
        nombre = title[i].replace(' ', '_') + str(i) +'.jpg'
        with open(carpeta_destino + nombre, 'wb') as f:
            f.write(r.content)
    except:
        print('Error en la url: ', url)
    i += 1
