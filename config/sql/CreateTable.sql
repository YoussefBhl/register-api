CREATE TABLE users (
id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
email  varchar(50) UNIQUE NOT NULL,
password  BINARY(60) NOT NULL,
status varchar(20) DEFAULT 'pending',
code INT(4),
code_expiration INT(11)
);
