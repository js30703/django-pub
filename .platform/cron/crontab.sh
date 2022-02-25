#!/bin/bash
crontab -r
touch /var/log/crontab.log
chown ec2-user:ec2-user /var/log/crontab.log && chmod 777 /var/log/crontab.log
/var/app/venv/*/bin/python3 /var/app/current/manage.py crontab add
service crond restart