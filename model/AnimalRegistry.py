import datetime
import mysql.connector
from model.Camel import Camel
from model.Cat import Cat
from model.Dog import Dog
from model.Donkey import Donkey
from model.Hamster import Hamster
from model.Horse import Horse


class AnimalRegistry:
    def __init__(self):
        self.cnx=mysql.connector.connect(user='root', password='5422531z', host = '127.0.0.1', database='human_friends')
        self.cursor = self.cnx.cursor()


    def add_animal(self,animal,commands):
        query = ("INSERT INTO all_animals "
                 "(name, command, birthday, type)"
                 "VALUES (%s, %s, %s, %s)")
        animal_data = (animal.name, ",".join(commands), animal.birthday, type(animal).__name__)
        self.cursor.execute(query,animal_data)
        self.cnx.commit()
        


    def get_animals(self, animal_type):
        query = ("SELECT name, command, birthday, type FROM all_animals WHERE type=%s")
        self.cursor.execute(query, (animal_type,))
        animals=[]
        for row in self.cursor.fetchall():
            row_dict = dict(zip(self.cursor.column_names, row))  
            animals.append(self._create_animal(row_dict))
        return animals

    
    def get_animal(self, name):
        query = ("SELECT name, command, birthday, type FROM all_animals WHERE name=%s")
        self.cursor.execute(query, (name,))
        row = self.cursor.fetchone()
        self.cursor.fetchall()
        if row:
            row_dict = dict(zip(self.cursor.column_names, row)) 
            return self._create_animal(row_dict)
        return None


    
    def get_all_animals(self):
        query = ("SELECT name, command, birthday, type FROM all_animals")
        self.cursor.execute(query)
        animals = []
        for row in self.cursor.fetchall():
            row_dict = dict(zip(self.cursor.column_names, row)) 
            animal = self._create_animal(row_dict)
            if animal is not None:
                animals.append(animal)
        return animals
    
    def _create_animal(self, row_dict):
        animal_type = row_dict['type'].lower()
        if animal_type == 'dog':
            return Dog(row_dict)
        elif animal_type == 'cat':
            return Cat(row_dict)
        elif animal_type == 'hamster':
            return Hamster(row_dict)
        elif animal_type == 'horse':
            return Horse(row_dict)
        elif animal_type == 'donkey':
            return Donkey(row_dict)
        elif animal_type == 'camel':
            return Camel(row_dict)
        else:
            return None


    def delete_animal(self, name):
        query = "DELETE FROM all_animals WHERE name = %s"
        self.cursor.execute(query, (name,))
        self.cnx.commit()
        return self.cursor.rowcount  # возвращает количество удаленных строк
    