FROM mariadb

MAINTAINER ExcelE

ENV MYSQL_DATABASE=DB1 \
    MYSQL_ROOT_PASSWORD=changepassword

ADD ./pre-start/init.sql /docker-entrypoint-initdb.d

EXPOSE 3306