DB=baseball_db

db-stop:
	- docker stop ${DB}

db-init: db-stop
	docker run --rm --name ${DB}\
	 -e MYSQL_ROOT_PASSWORD=baseball_pass\
	 -e MYSQL_USER=baseball_user\
	 -e MYSQL_PASSWORD=baseball_pass\
	 -e MYSQL_DATABASE=${DB}\
	 -d -v `pwd`/db_init:/docker-entrypoint-initdb.d -v `pwd`/cnf:/etc/mysql/conf.d\
	 -p 3306:3306 mysql:5.7

db-connect: db-init
	mysql -u baseball_user -h 127.0.0.1 -p baseball_db
