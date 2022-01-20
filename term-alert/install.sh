#!/bin/bash
YUM_CMD=$(which yum)
APT_GET_CMD=$(which apt-get)
SYSTEMCTL_EXIST=$(which systemctl)
if [[ ! -z $YUM_CMD ]]; then
    yum install epel-release python-urwid python3 python3-pip git auditd  -y
elif [[ ! -z $APT_GET_CMD ]]; then
    apt-get update -y 
    apt-get install python3 python3-pip git python-urwid auditd  -y
else
    echo "installation failed"
    exit 1;
fi
pip3 install urwid
git clone https://github.com/dbaseqp/cyber
cd cyber/term-alert
if [[ ! -z $SYSTEMCTL_EXIST ]]; then
    systemctl mask systemd-journald-audit.socket
    systemctl start auditd
    systemctl stop auditd
else
    service auditd start
fi
service auditd stop
chmod +x go-audit
./go-audit -config go-audit.yaml &
