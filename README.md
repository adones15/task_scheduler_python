# Task Scheduler Python

Desenvolvi um agendador de tarefasem Python, ele tem por finalidade agendar scripts python para rodar no horário que for configurado, funciona semelhante ao Task Scheduler do Windows e o Cron do Linux.

A idéia é basicamente ter um arquivo principal do agendador (task_scheduler.py) onde ele faz a "orquestração", nesse arquivo é feita a imoprtação das funções dos outros arquivos.py (script1.py, script2.py, script3.py) e então é iniciado um loop infinito que fica verificando a todo momento o horário atual, então faço uma condição, se o horário atual for igual o horário que agendei o script, ele chama a função que foi agendada para aquele horário. Após finalizar a execução do código é gerado um arquivo.txt de log informando se o código executou com sucesso ou com erro, e armazenado no diretório de logs.

Para o código não "quebrar" e ficar rodando em loop infinito, nas funções eu uso o try - except, pois havendo erro o código continua funcionando, e você é informado que deu erro através do log.
