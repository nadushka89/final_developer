# Итоговая контрольная работа по специализации "Программист"

## Информация о проекте
- Необходимо организовать систему учета для питомника в котором живут домашние и вьючные животные.

## Как сдавать проект
- Для сдачи проекта необходимо создать отдельный общедоступный репозиторий.
- Разработку вести в этом репозитории, использовать пул реквесты на изменения.
- Программа должна запускаться и работать, ошибок при выполнении программы быть не должно.
- Программа, может использоваться в различных системах, поэтому необходимо разработать класс в виде конструктора.

## Задание
### Блок по работе с терминалом в OS Linux
- Операции с файлами:
    1. Используя команду cat создать файл "Домашние животные", с данными: собаки, кошки, хомяки.
    2. Создать файл "Вьючные животные", с данными: лошади, верблюды, ослы.
    3. Объединить созданные файлы.
    4. Вывести содержимое созданного файла.
    5. Переименовать файл в "Друзья человека".
    6. Создать директорию, переместить в нее файл.
- Репозотории и работа с пакетами
    1. Подключить дополнительный репозиторий MySQL.
    2. Установить любой пакет из подключенного репозитория.
    3. Установить и удалить deb-пакет с помощью dpkg.
- Выложить историю команд из терминала OS Linux.

# Блок по работе с Диаграммами
- Нарисовать диаграмму:
    1. Родительский класс.
    2. Подклассы домашние животные и вьючные животные.
    3. Подклассы для домашних животных: собаки, кошки, хомяки.
    4. Подклассы для вьючных животных: лошади, верблюды, ослы.

# Блок по работе с SQL в СУБД MySQL
- Создать базу данных "Друзья человека" // "human_friends"
    1. Создать таблицы "pets", "dogs", "cats", "hamsters", "pack_animals", "horses", "camels", "donkeys" с иерархией из диаграммы.
    2. Низкоуровневые таблицы должны иметь следующие поля:
        - имена животных.
        - команды которые животные выполняют.
        - даты рождения животных.
    3. Наполните низкоуровневые таблицы данными.
    4. Удалите таблицу верблюды.
    5. Объедините таблицы "лошади" и "ослы".
    6. Создайте таблицу "молодые животные". // "young_animals"
        - В отдельном столбце с точностью до месяца должен храниться возраст животных.
    7. Поместите в нее всех животных старше 1 года и младше 3 лет.
    8. Объединить все таблицы в одну, при этом сохраняя поля, указывающие на прошлую принадлежность к старым таблицам.

# Блок "Программирование"
- Создайте класс с Инкапсуляцией методов и наследованием по диаграмме.
- Напишите программу, имитирующую работу реестра домашних животных, со следующим функционалом:
    1. Завести новое животное.
    2. Определять животное в правильный класс.
    3. Увидеть список команд, которое выполняет животное.
    4. Обучить животное новым командам.
    5. Реализовать навигацию по меню.
- Создайте класс-счетчик, со следующим функционалом:
    1. Метод add(), увеличивающий значение внутренней int переменной на 1 при нажатии "Завести новое животное".
    2. Объект типа счетчик должен уметь работать в блоке try-with-resources.
    3. Должно срабатывать исключение, если работа с объектом типа счетчик была не в ресурсном try и/или ресурс остался открыт.
    4. Значение считать в ресурсе try, если при заведения животного заполнены все поля.


## Задание 1: Блок по работе с терминалом в OS Linux

1. Создаем 2 файла и наполняем их:

```
cat > "Домашние животные"
собаки
кошки
хомяки
cat > "Вьючные животные"
лошади
верблюды
ослы
```
2. Объединяем файлы:
```
"Домашние животные" "Вьючные животные" > "Друзья человека"
```
3. Посмотрим объедененный файл:
```
cat "Друзья человека"
```
4. Создаем новую директорию и перемещаем файл туда:
```
mkdir Animals
mv "Друзья человека" Animals/
```
5. Скачиваем и устанавливаем пакет:
```
sudo wget https://dev.mysql.com/get/mysql-apt-config_0.8.25-1_all.deb

sudo apt install ./mysql-apt-config_*_all.deb
```
6. Обновляем информацию о пакетах:
```
sudo apt update
```
7. Устанавливаем и удаляем пакет:
```
sudo apt install mysql-server
sudo apt remove mysql-client
```
8. Установливаем и удаляем deb-пакет с помощью dpkg:
```
sudo dpkg -i mysql-apt-config_0.8.25-1_all.deb && sudo apt update && sudo apt install mysql-client
sudo dpkg -r mysql-client

```

9. История команд:
```
 263  cat > "Домашние животные"
  264  cat > "Вьючные животные"
  265  cat "Домашние животные" "Вьючные животные" > "Друзья человека"
  266  cat "Друзья человека"
  267  mkdir Animals
  268  mv "Друзья человека" Animals/
  269  sudo wget https://dev.mysql.com/get/mysql-apt-config_0.8.25-1_all.deb
  270  sudo apt install ./mysql-apt-config_*_all.deb
  271  sudo apt update
  272  sudo apt install mysql-server
  273  sudo apt remove mysql-client
  274  sudo dpkg -i mysql-apt-config_0.8.25-1_all.deb && sudo apt update && sudo apt install mysql-client
  275  sudo dpkg -r mysql-client
  276  history
```
10. Диаграмма:
    1. Родительский класс.
    2. Подклассы домашние животные и вьючные животные.
    3. Подклассы для домашних животных: собаки, кошки, хомяки.
    4. Подклассы для вьючных животных: лошади, верблюды, ослы.

![Диаграмма](https://github.com/nadushka89/final_developer/blob/main/source/Diagramma.png) 


# Блок по работе с SQL в СУБД MySQL

1. Создаем базу данных human_friends:
```
DROP DATABASE IF EXISTS human_friends;
CREATE DATABASE human_friends;

```
2. Создаем таблицу pets и на ее основе dogs, cats, hamsters, а также pack_animals и на ее основе horses,camels,donkeys:
```
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
```
3. Наполняем таблицы данными:
```
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
```

4. Удаляем таблицу "camels" :
```
DROP TABLE camels;
```
5. Объединяем таблицы "camels" и "donkeys" в "horses_and_donkeys":
```
DROP TABLE IF EXISTS horses_and_donkeys;
CREATE TABLE horses_and_donkeys AS
SELECT * FROM horses
UNION ALL
SELECT * FROM donkeys;
```
6. Объединим домашних животных в таблицу pets:
```
INSERT INTO pets  (name, command, birthday, type) 
SELECT name, command, birthday, type FROM cats
UNION ALL
SELECT name, command, birthday, type FROM dogs
UNION ALL
SELECT name, command, birthday, type FROM hamsters;
```

7. Создаем таблицу "молодые животные" и добавление в неё животных от 1 до 3 лет(из pets и horses_and_donkeys):
```
DROP TABLE IF EXISTS young_animals;
CREATE TABLE young_animals AS 
SELECT *, TIMESTAMPDIFF(month, birthday, CURDATE()) as age_in_months
FROM pets 
WHERE birthday BETWEEN DATE_SUB(CURDATE(), INTERVAL 3 YEAR) AND  DATE_SUB(CURDATE(), INTERVAL 1 YEAR)

INSERT INTO young_animals 
SELECT *, TIMESTAMPDIFF(month, birthday, CURDATE()) as age_in_months
FROM horses_and_donkeys 
WHERE birthday BETWEEN DATE_SUB(CURDATE(), INTERVAL 3 YEAR) AND  DATE_SUB(CURDATE(), INTERVAL 1 YEAR)
```

8. Объединим всех животных в одну таблицу all_animals:
```
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
```