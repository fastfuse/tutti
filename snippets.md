# Snippets

### MYSQL

Create container

```sh
$> docker run --name mysql_db  -p 127.0.0.1:3307:3306 -e MYSQL_ROOT_PASSWORD=root -v vol_mysql:/var/lib/mysql -d mysql:5.6 --default-authentication-plugin=mysql_native_password
```

Create DB

```sh
$> mysql -u root -proot --host=127.0.0.1 --port=3307

mysql> create database <your-db-name>;
mysql> q\;
```

Load DB dump

```sh
$> mysql -u root -proot --host=127.0.0.1 --port=3307 <your-db-name> < dump.sql
```


Stop container

```sh
$> docker stop mysql_db
```

Start container

```sh
$> docker start mysql_db
```

Update password

```sh
$> update user set password=PASSWORD('NEW PASSWORD') where user='root';
```
---

### Redis

Run Redis container

```sh
$> docker run -p 6379:6379 redis
```

### Misc

Start HTTP server inside the directory

Bash:

```sh
$> echo Your IP: $( ifconfig en0 | awk '$1 == "inet" {print $2}') && python3 -m http.server
```

Fish shell:

```sh
$> echo Your IP: ( ifconfig en0 | awk '$1 == "inet" {print $2}') & python3 -m http.server
```


### Jenkins

Create Jenkins container w/ volume

```sh
$> docker run --name jenkins_server -p 8080:8080 -p 50000:50000 -v jenkins_home:/var/jenkins_home jenkins/jenkins:lts
```

Stop container

```sh
$> docker stop jenkins_server
```

Start container

```sh
$> docker start jenkins_server
```
