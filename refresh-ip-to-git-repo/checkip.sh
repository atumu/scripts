#!/bin/sh

# your ip file name and ip field name
IP_FILE="ip"
OLD_IP=0

# set -xv

# get new ip
NEW_IP=`/usr/bin/python newip.py 2>&1`

if [ ! -f "$IP_FILE" ]
then
 touch "$IP_FILE";
else
 OLD_IP=$(cat $IP_FILE)
fi

if [ "$NEW_IP" != "$OLD_IP" ]
then
echo $NEW_IP >$IP_FILE
/usr/bin/git add -A
/usr/bin/git commit -m "`date +%Y-%m-%d%t%H:%M:%S`"
/usr/bin/git push origin master
fi
