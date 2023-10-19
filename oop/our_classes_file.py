class Fruit:
    def __init__(self, name, color, weight, price):
        self.name = name
        self.color = color
        self.weight = weight
        self.price = price


class Car:
    def __init__(self, model, color, reg_no, price):
        self.model = model
        self.color = color
        self.reg_no = reg_no
        self.price = price


class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def register(self):
        print("Yeah I can register")

    def login(self):
        print("Yeah I can login")


class Admin(User):
    def __init__(self, name, email, password):
        super().__init__(name, email, password)

    def suspendUsers(self):
        print("Yeah I can suspend users")


class Superadmin(Admin):
    def __init__(self, name, email, password):
        super().__init__(name, email, password)

    def suspendAdmin(self):
        print("Yeah I can suspend admins")
