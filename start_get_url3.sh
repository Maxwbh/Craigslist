#!/bin/sh
##################################
# Script para monitorar processo #
##################################
# nome do processo a ser filtrado
PROCESSO='import_url_pag.py'
# intervalo que sera feita a checagem (em segundos)
INTERVALO=3600
while true; do
    # numero de cópias do processo rodando
    for i in {1..10}; do
        OCORRENCIAS=$(ps -ef | grep "$PROCESSO $i" | grep -v "grep" | wc -l)
        if [ $OCORRENCIAS -eq 0 ]; then
	     echo $PROCESSO $i
             python ./$PROCESSO $i >> import$i.log &
        fi
    done
    # Aguarda o intervalo especificado na variável e executa novamente o script
    sleep $INTERVALO
    ./kill_proc.sh
    sleep 60
done
# Fim do Script
