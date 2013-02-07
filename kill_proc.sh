#!/bin/sh
PROCESSO='start_get'
/usr/ucb/ps -wwaux | grep $PROCESSO | grep -v grep |awk '{print $2}' | while read i
do
     echo "$i"
     kill -9 "$i"
done
PROCESSO='import_url_pag.py'
/usr/ucb/ps -wwaux | grep $PROCESSO | grep -v grep |awk '{print $2}' | while read i
do
     echo "$i"
     kill -9 "$i"
done