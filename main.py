# Завдання 1. Клас Людина
class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def short_info(self):
        return f"{self.name}, {self.age} років, проживає у місті {self.city}."


# Завдання 2. Клас Автомобіль
class Car:
    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color

    def full_info(self):
        return f"Автомобіль: {self.brand} {self.model}, {self.year} року, колір: {self.color}."

    def change_color(self, new_color):
        self.color = new_color
        return f"Колір автомобіля змінено на {self.color}."


# Завдання 3. Клас Банк
class BankAccount:
    def __init__(self, owner_name, account_number, balance=0):
        self.owner_name = owner_name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"Поповнено рахунок на {amount} грн. Новий баланс: {self.balance} грн."

    def withdraw(self, amount):
        if amount > self.balance:
            return "Помилка: недостатньо коштів на рахунку!"
        else:
            self.balance -= amount
            return f"Знято {amount} грн. Новий баланс: {self.balance} грн."

    def check_balance(self):
        return f"Поточний баланс: {self.balance} грн."


# Перевірка функціональності
print("=== Перевірка Person ===")
person1 = Person("Іван", 30, "Київ")
print(person1.short_info())

print("\n=== Перевірка Car ===")
car1 = Car("Toyota", "Camry", 2020, "чорний")
print(car1.full_info())
print(car1.change_color("білий"))
print(car1.full_info())

print("\n=== Перевірка BankAccount ===")
account1 = BankAccount("Олена", "UA123456789", 1000)
print(account1.check_balance())
print(account1.deposit(500))
print(account1.withdraw(200))
print(account1.withdraw(2000))
print(account1.check_balance())
