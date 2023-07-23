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
CREATE DATABASE human_friends
```

