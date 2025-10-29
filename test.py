class User:
    def __init__(self, name, last_name, age):
        self.name = name
        self.last_name = last_name
        self.age = age

    def login(self, name, last_name, age):
        if self.name == name and self.last_name == last_name and self.age == age:
            print('Acceso concedido')

        else: 
            print('Acceso denegado')

user1 = User("Vicente", "Lagos", 25)
user1.login("Vicente", "Lagos", 25) 
user1.login("Ana", "Pérez", 30)
user1.login("Ariel", "Roco", 12)














