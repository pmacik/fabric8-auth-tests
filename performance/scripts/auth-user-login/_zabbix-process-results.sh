#!/bin/bash

source _setenv.sh

export ZABBIX_LOG=$1
export ZABBIX_TIMESTAMP=`date +%s`

./__zabbix-process-load.sh '"loginUserAuth","open-login-page-time"' "login-user.auth.open-login-page" >> $ZABBIX_LOG
./__zabbix-process-load.sh '"loginUserAuth","login-time"' "login-user.auth.login" >> $ZABBIX_LOG
