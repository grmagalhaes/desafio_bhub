drop database if exists desafio_bhub;
drop user if exists 'bhub'@'localhost';

create database desafio_bhub character set utf8;
create database test_desafio_bhub character set utf8;

create user 'bhub'@'localhost' identified by 'SENHA';

grant all privileges on desafio_bhub.* to 'bhub'@'localhost';
grant all privileges on test_desafio_bhub.* to 'bhub'@'localhost';