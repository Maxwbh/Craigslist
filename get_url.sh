#!/bin/bash
echo
echo "Insntanciando sistema de coleta de URL."
echo "---------------------------------------"
for i in {1..50}
do
    nohup python ./import_url_pag.py $i &
    echo "Instancia $i."
done
echo "---------------------------------------"
echo
exit 0

