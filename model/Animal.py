import datetime

class Animal:
    def __init__(self,db_row):
        self.db_row = db_row
        self.is_update = True

    @property
    def name(self):
        return self.db_row['name']
    
    @property
    def birthday(self):
        date = self.db_row['birthday']
        return datetime.datetime(date.year, date.month, date.day)
    

    @property
    def commands(self):
        return self.db_row['command'].split(',')

    def add_command(self, command):
        self.commands.append(command)
        self.is_update = True
    
    def get_info(self):
        return f"Name: {self.name}, Birthday: {self.birthday}, Type: {self.__class__.__name__}, Commands: {', '.join(self.commands)}"
    
    def __str__(self):
        return self.name 