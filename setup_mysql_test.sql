-- script to create database hbnb_test_db
--- A new user hbnb_test (in localhost)
CREATE DATABASE IF NOT EXIST hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED AS 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbn_tets'@'localhost'
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
