# refresh your IP to git repo with crontab:

## need： linux python git crontab

step 1:

    bash
        git clone this repo
        cd hosts
        vi checkip.sh 
            add your hosts path under the line "# hosts path"
    
    
step 2:

    python:
        pip install ipgetter
        
step 3:

    bash:    
        chmod 755 checkip.sh  OR chmod +x checkip.sh        
        crontab -e:    
            # crontab -l #list the cron jobs
            # crontab -e #to edit the cron
            # add these text to the crontab,then save and quit
            # it will run cron.sh every 15 minutes
            # :wq
            # it will be better to restart cron service
            # ubuntu:  sudo /etc/init.d/cron restart
            # centos:  sudo /sbin/service crond restart
            
            SHELL=/bin/bash
            PATH=/sbin:/bin:/usr/sbin:/usr/bin
            MAILTO=root
            
            # For details see man 4 crontabs
            
            # Example of job definition:
            # .---------------- minute (0 - 59)
            # |  .------------- hour (0 - 23)
            # |  |  .---------- day of month (1 - 31)
            # |  |  |  .------- month (1 - 12) OR jan,feb,mar,apr ...
            # |  |  |  |  .---- day of week (0 - 6) (Sunday=0 or 7) OR sun,mon,tue,wed,thu,fri,sat
            # |  |  |  |  |
            # *  *  *  *  * user-name  command to be executed
            
            * * * * * /bin/bash your/path/checkip.sh
step 4:

    bash:
        chkconfig --level 35 crond on
        # ubuntu: sudo /etc/init.d/cron restart
        # centos: sudo /sbin/service crond restart   
        

