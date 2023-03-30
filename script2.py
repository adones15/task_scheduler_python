import requests, json, pandas as pd, datetime
from chave_api import chave_api

def func_s2(): #Função a ser agendada no arquivo principal (task_scheduler.py)
    try:
        #Código utilizado para exemplo, faz uma chamada na API, transforma em um DataFrame e exporta para Excel.
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=ITUB4.SAO&apikey={chave_api}'
        r = requests.get(url)
        data_a = json.loads(r.content)
        df = pd.DataFrame(data_a['Time Series (Daily)'])
        dtn = str(datetime.datetime.now())
        df.to_excel("Script2.xlsx")

        #log caso a função seja executada SEM erros.
        with open(fr"G:\Meu Drive\Adones\Projetos_Python\task_scheduler\logs\log_sucesso_func_s2_data_{dtn[0:4]}{dtn[5:7]}{dtn[9:11]}_hora_{dtn[11:13]}{dtn[14:16]}{dtn[17:19]}.txt", "w+") as arquivo:
            arquivo.write("Executado com sucesso!!!")
    
    except:
        #log caso a função seja executada COM erros.
        dtn = str(datetime.datetime.now())
        with open(fr"G:\Meu Drive\Adones\Projetos_Python\task_scheduler\logs\log_erro_func_s2_data_{dtn[0:4]}{dtn[5:7]}{dtn[9:11]}_hora_{dtn[11:13]}{dtn[14:16]}{dtn[17:19]}.txt", "w+") as arquivo:
            arquivo.write("Função executou com ERRO, favor analisar e corrigir!!!")
        
    #Para os logs, determinei o nome como *log_(sucesso ou erro)_(nome da função)_(data)_(hora).txt* pois fica fácil para encontrar do momento e a função que se refere.