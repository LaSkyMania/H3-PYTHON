#!/bin/bash

# Start/Stop Mysql Server Docker

OPTION=$1

if [[ "$OPTION" == "start" ]]; then
    docker run -d --rm --name mysql \
        -e MYSQL_ROOT_PASSWORD=Hitema2025 \
        -p 3306:3306 \
        -v volume_mysql:/var/lib/mysql \
        mysql:8.4.4
    echo "MySQL Docker démarré."
elif [[ "$OPTION" == "stop" ]]; then
    docker stop mysql
    echo "MySQL Docker arrêté."
else
    echo ""
    echo "Usage : ./dkmysql.sh [start|stop]"
    echo ""
fi