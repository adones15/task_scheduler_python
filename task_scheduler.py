#Importando as funções a serem agendadas dos outros arquivos.py
from script1 import func_s1
from script2 import func_s2
from script3 import func_s3

import datetime


while True: #Loop infinito, ou seja fica executando sempre e fazendo as verificações necessárias a todo tempo.

    date_now = str(datetime.datetime.now()) #Verificando a data e hora atual
    hour_now = date_now[11:22] #Obtendo apenas o horário da variável date_now

    if hour_now == "10:35:00.00": #Verificando o horário agendado para executar a função do script1 (func_s1()), se o horário for igual a variável hour_now ele executa a função.
        func_s1() #Chamando a função caso atenda a condição verdadeira do if.
        print(f"Primeiro Script executado em {datetime.datetime.now()}")

    if hour_now == "10:35:30.00": #Verificando o horário agendado para executar a função do script2 (func_s2())
        func_s2()#Chamando a função caso atenda a condição verdadeira do if.
        print(f"Segundo Script executado em {datetime.datetime.now()}")

    if hour_now == "10:35:55.00": #Verificando o horário agendado para executar a função do script3 (func_s3())
        func_s3()#Chamando a função caso atenda a condição verdadeira do if.
        print(f"Terceiro Script executado em {datetime.datetime.now()}")        

    ###Neste exemplo agendei apenas 3 scripts para executar em determinado horário, porém conforme for a demanda, basta incluir o bloco if e colocar o horário desejado para executar o script###