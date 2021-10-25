import requests
import json
import pandas as pd

i= 100
a= 463
b = "462"   
while i <= a:
    url = "https://resultados.tse.jus.br/oficial/ele2020/divulgacao/oficial/boletim-urna/304/dados/sp/p000304-sp-m65790-z0059-s0" + str(i) +".json"
    res = requests.get(url)
    if res.status_code == 200:
            print(f'{url}')
            data = res.json()
            dump = json.dumps(data)
            info = json.loads(dump)
            zone = info['z']
            section = info['s']
            nome= info['ele'][0]['carg'][0]['nm']
            req = info['ele'][0]['carg'][0]['par']
            
            zText = {
                
                'Zona':zone,
                'Secao':section,
                'Cargo':nome
            }
            
            print(req,zText)
            
            if zText['Cargo'] == 'Prefeito':
                zdf =pd.json_normalize(zText)
                df = pd.json_normalize(req)
                zdf.to_csv('DataPrefeito.csv',mode='a')
                df.to_csv("DataPrefeito.csv",mode='a')
            else:
                print(zText['Cargo']+' Retido ')
            
            i+=1
            
    else:
        print('') 
        i+=1
