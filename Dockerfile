FROM mariadb

MAINTAINER ExcelE

ENV MYSQL_DATABASE=DB1 \
    MYSQL_ROOT_PASSWORD=changepassword

EXPOSE 3306