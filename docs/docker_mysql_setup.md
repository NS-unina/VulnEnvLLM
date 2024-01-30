## MySQL Setup
```bash
apt install -y wget default-mysql-client
wget https://dev.mysql.com/get/mysql-apt-config_0.8.29-1_all.deb -O mysql.deb
apt install -y ./mysql.deb
# If mariadb is installed run:
apt remove -y mariadb-client-10.5 mariadb-client-core-10.5
apt install -y mysql-server
chown -R mysql:mysql /var/lib/mysql /var/log/mysql /var/run/mysqld
mysqld --user=mysql
```