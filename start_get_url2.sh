#!/bin/sh
##################################
# Script para monitorar processo #
##################################
# nome do processo a ser filtrado
PROCESSO='import_url_pag.py'
# intervalo que sera feita a checagem (em segundos)
INTERVALO=60
while true; do
      # numero de cópias do processo rodando
      OCORRENCIAS=$(ps -ef | grep "$PROCESSO" | grep -v "grep" | wc -l)

      if [ $OCORRENCIAS -le 20 ]; then
          echo "Fudeu !!"
          ./kill_proc.sh
      fi

      if [ $OCORRENCIAS -eq 0 ]; then
             ./get_url.sh
       fi
       # Aguarda o intervalo especificado na variável e executa novamente o script
        sleep $INTERVALO
done
# Fim do Script