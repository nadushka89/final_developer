from click import command
from model.Camel import Camel
from model.Cat import Cat
from model.Dog import Dog
from model.Donkey import Donkey
from model.Hamster import Hamster
from model.Horse import Horse


class AnimalPresenter:
    def __init__(self,view,model):
        self.view = view
        self.model=model
        self.running=True

    def run(self):
        while self.running:
            self.view.menu()
            choice=input("Выберите пункт меню: ")

            if choice == '1':
                type = self.view.animal_type()
                name=self.view.animal_name()
                birthday=self.view.animal_birthday()
                commands = self.view.animal_commands()
                
                animal_data = {
                    "name": name,
                    "birthday": birthday,
                    "commands": commands
                }

                if type == 'cat':
                    self.model.add_animal(Cat(animal_data), commands)
                elif type == 'dog':
                    self.model.add_animal(Dog(animal_data), commands)
                elif type == 'hamster':
                    self.model.add_animal(Hamster(animal_data), commands)
                elif type == 'horse':
                    self.model.add_animal(Horse(animal_data), commands)
                elif type == 'camel':
                    self.model.add_animal(Camel(animal_data), commands)
                elif type == 'donkey':
                    self.model.add_animal(Donkey(animal_data), commands)
                else:
                    print("Неверный тип //Invalid type")

            elif choice == '2':
                name= self.view.animal_name()
                command = self.view.animal_command()
                animal=self.model.get_animal(name)
                if animal is not None:
                    animal.add_command(command)
                else:
                    print("Животное не найдено // Animal not found")

            elif choice == '3':
                name= self.view.animal_name()
                animal=self.model.get_animal(name)
                if animal is not None:
                    self.view.print_commands(animal.commands)
                else:
                    print("Животное не найдено // Animal not found")

            elif choice == '4':
                animals=self.model.get_all_animals()
                for animal in animals:
                    if animal is not None:
                        print(animal.get_info())
                    else:
                        print("Животное не найдено // Animal not found")

            elif choice == '5':
                name = self.view.animal_name()
                deleted_rows =self.model.delete_animal(name)
                if deleted_rows > 0:
                    print(f"Животное {name} успешно удалено.")
                else:
                    print("Извините, не удалось удалить животное. Попробуйте другое имя.")


            elif choice == '6':
                animal_type = self.view.get_animal_type()
                animals = self.model.get_animals(animal_type)
                for animal in animals:
                    if animal is not None:  
                        print(animal.get_info())

            elif choice == '7':
                self.running = False


            