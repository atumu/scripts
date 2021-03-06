#!/bin/sh

# your hosts path
cd /opt/cron/hosts/
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
/root/bin/git add -A
/root/bin/git commit -m "`date +%Y-%m-%d%t%H:%M:%S`"
/root/bin/git push origin master
fi
