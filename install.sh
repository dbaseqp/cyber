#!/bin/bash

YUM_CMD=$(which yum)
APT_GET_CMD=$(which apt-get)

if [[ ! -z $YUM_CMD ]]; then
    yum install auditd git -y
    service auditd restart
    service auditd stop
elif [[ ! -z $APT_GET_CMD ]]; then
    apt-get update -y 
    apt-get install auditd git -y
    systemctl restart auditd
    systemctl stop auditd
else
    echo "installation failed"
    exit 1;
fi

systemctl stop systemd-journald-audit.socket
systemctl mask systemd-journald-audit.socket

git clone https://github.com/dbaseqp/cyber stage
cd stage
mv audit.rules /etc/audit/audit.rules
