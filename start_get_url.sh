#!/bin/sh
##################################
# Script para monitorar processo #
##################################
# nome do processo a ser filtrado
PROCESSO='import_url_pag.py'
# intervalo que sera feita a checagem (em segundos)
INTERVALO=10
while true; do
    # numero de cópias do processo rodando
    for i in {1..10}; do
        OCORRENCIAS=$(ps -ef | grep "$PROCESSO" $i | grep -v "grep" | wc -l)
        if [ $OCORRENCIAS -eq 0 ]; then
            nohup ./$PROCESSO $i
        fi
    done
    # Aguarda o intervalo especificado na variável e executa novamente o script
    sleep $INTERVALO
done
# Fim do Script