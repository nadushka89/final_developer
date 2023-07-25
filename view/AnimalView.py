import datetime


class AnimalView:
    def menu(self):
    
        print("1. Добавить животное // Add an animal")
        print("2. Добавить животному новую команду // Teach an animal a new command")
        print("3. Посмотреть команды животного // View an animals commands")
        print("4. Посмотреть всех животных // View all animals")
        print("5. Удалить животное // Delete an animal")
        print("6. Посмотреть всех животных определенного типа")
        print("7. Выход // Exit")

    def animal_type(self):
        return input("Введите тип животного (cat/dog/hamster/horse/camel/donkey): ")
    
    def animal_name(self):
        return input("Введите имя животного: ")
    
    def animal_birthday(self):
        birthday = input("Enter the animal's birthday (yyyy-mm-dd): ")
        year, month, day = map(int, birthday.split('-'))
        return datetime.date(year, month, day)
    
    def animal_command(self):
        return input("Введите новую команду: ")
    
    def print_commands(self,commands):
        print(commands)

    def animal_commands(self):
        commands = input("Введите команды(через запятую): ")
        return [command.strip() for command in commands.split(",")]
    
    def get_animal_type(self):
        return input ("Введите тип животного cat/dog/hamster/horse/camel/donkey): ")
    
