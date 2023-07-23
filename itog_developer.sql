DROP DATABASE IF EXISTS human_friends;
CREATE DATABASE human_friends;
USE human_friends;

DROP TABLE IF EXISTS pets;
CREATE TABLE pets (
	id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
	name varchar(255) NOT NULL,
	command varchar(255),
	birthday date,
	type varchar(255)
);
DROP TABLE IF EXISTS dogs; 
CREATE TABLE dogs LIKE pets;
DROP TABLE IF EXISTS cats;
CREATE TABLE cats LIKE pets;
DROP TABLE IF EXISTS hamsters;
CREATE TABLE hamsters LIKE pets;


DROP TABLE IF EXISTS pack_animals;
CREATE TABLE pack_animals (
	id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY, 
	name varchar(255) NOT NULL,
	command varchar(255),
	birthday date,
	type varchar(255)
);

DROP TABLE IF EXISTS  horses;
CREATE TABLE horses LIKE pack_animals;
DROP TABLE IF EXISTS  camels;
CREATE TABLE camels LIKE pack_animals;
DROP TABLE IF EXISTS  donkeys;
CREATE TABLE donkeys LIKE pack_animals;


INSERT INTO dogs (name, command, birthday, type)
VALUES 
("Vaska", "Sit","2018-05-15" , "dog"),
("Jon", "to lie","2017-09-10" , "dog"),
("Adam", "Voice","2015-12-13" , "dog"),
("Koul", "To me","2017-09-18" , "dog"),
("Mike", "To wait","2012-12-19" , "dog");

INSERT INTO cats (name, command, birthday, type)
VALUES 
("Milo", "Must not","2022-05-15" , "cat"),
("Jack ", "Kitty-kitty","2023-01-10" , "cat"),
("Loki", "Meow","2022-12-25" , "cat"),
("Buddy", "Ugh","2020-10-18" , "cat"),
("George", "To wait","2021-11-21" , "cat");


INSERT INTO hamsters (name, command, birthday, type)
VALUES 
("Tuz", "knowledge of the nickname","2021-07-11" , "hamster"),
("Apple ", "running","2022-01-02" , "hamster"),
("Bob", "stand","2022-10-02" , "hamster"),
("Berni", "jump","2023-02-18" , "hamster"),
("Chibi", "upheaval","2023-01-21" , "hamster");

INSERT INTO horses (name, command, birthday, type)
VALUES 
("Amori", "Forward","2023-07-11" , "horse"),
("Amos ", "Stand","2022-10-02" , "horse"),
("Wern", "Step","2021-10-22" , "horse"),
("Greg", "Stand","2018-02-21" , "horse"),
("Dikki", "upheaval","2021-08-21" , "horse");

INSERT INTO camels (name, command, birthday, type)
VALUES 
("Agata", "Right!","2018-05-13" , "camel"),
("Ida ", "Back!","2019-06-14" , "camel"),
("Vasja", "Left!","2020-07-15" , "camel"),
("Gjared", "Stop!","2018-08-16" , "camel"),
("Twist", "Go away!","2021-09-17" , "camel");

INSERT INTO donkeys (name, command, birthday, type)
VALUES 
("Biggs", "Forward","2023-06-15" , "donkey"),
("Wuddi ", "Stand","2021-07-16" , "donkey"),
("Bond", "Step","2022-08-17" , "donkey"),
("Samara", "Stand","2018-09-18" , "donkey"),
("Lusi", "upheaval","2021-10-19" , "donkey");

DROP TABLE camels;

DROP TABLE IF EXISTS horses_and_donkeys;
CREATE TABLE horses_and_donkeys AS
SELECT * FROM horses
UNION ALL
SELECT * FROM donkeys;

INSERT INTO pets  (name, command, birthday, type) 
SELECT name, command, birthday, type FROM cats
UNION ALL
SELECT name, command, birthday, type FROM dogs
UNION ALL
SELECT name, command, birthday, type FROM hamsters;

DROP TABLE IF EXISTS young_animals;
CREATE TABLE young_animals AS 
SELECT *, TIMESTAMPDIFF(month, birthday, CURDATE()) as age_in_months
FROM pets 
WHERE birthday BETWEEN DATE_SUB(CURDATE(), INTERVAL 3 YEAR) AND  DATE_SUB(CURDATE(), INTERVAL 1 YEAR)

INSERT INTO young_animals 
SELECT *, TIMESTAMPDIFF(month, birthday, CURDATE()) as age_in_months
FROM horses_and_donkeys 
WHERE birthday BETWEEN DATE_SUB(CURDATE(), INTERVAL 3 YEAR) AND  DATE_SUB(CURDATE(), INTERVAL 1 YEAR)


DROP TABLE IF EXISTS all_animals;
CREATE TABLE `all_animals` (
    id int NOT NULL AUTO_INCREMENT,
    name varchar(255),
    command varchar(255),
    birthday date,
    type varchar(255),
    previous_table varchar(255),
    PRIMARY KEY (`id`)
);


INSERT INTO all_animals (name, command, birthday, type, previous_table)
SELECT name, command, birthday, type, 'pets' as previous_table FROM pets 
UNION ALL
SELECT name, command, birthday, type, 'horses_and_donkeys' FROM horses_and_donkeys
UNION ALL
SELECT name, command, birthday, type, 'young_animals' FROM horses_and_donkeys;



