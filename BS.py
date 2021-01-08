class User():
    def __init__(self, name, age, gender, phn_no):
        self.name = name
        self.age = age
        self.gender = gender
        self.phone_number = phn_no
    def show_details(self):
        print("personal details")
        print(" ")
        print("name:" ,self.name)
        print("age:" ,self.age)
        print("gender:",self.gender)
        print("phone number:",self.phone_number)


class Bank(User):
    def __init__(self, name,age,gender,phn_no):
        super().__init__(name,age,gender,phn_no)
        self.balance = 0

    def deposit(self,amount):
        self.amount = amount
        self.balance = self.balance + amount
        print("account balance has been updated : Rs",self.balance)

    def withdrawn(self,amount):
        self.amount = amount
        if self.amount > self.balance:
            print("insufficient balance: Rs" ,self.balance)
        else:
            self.balance = self.balance - self.amount
        print("successfully withdrawn and updated: Rs",self.balance)

    def view_balance(self):
        self.show_details()
        print("updated balance is: Rs",self.balance)

amit = Bank("amit", 25, 'male', 8888888888)
amit.deposit(10000)
amit.withdrawn(5000)
amit.view_balance()


