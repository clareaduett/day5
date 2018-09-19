class BankAccount:
    
    def __init__(self):
        self.bal =  0
        self.status = True
    
    def open(self):
        self.status = True

    def get_balance(self):
        if self.status == False:
            raise ValueError ('Account closed')
        return self.bal


    def deposit(self, amount):
        if self.status == False:
            raise ValueError ('Account closed')
        if amount < 0:
            raise ValueError ('value can not be negative')
        self.bal += amount

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError ('can not withdraw negative')
        if amount > self.bal:
            raise ValueError ('can not withdraw more than available')
        self.bal -= amount
    
    def close(self):
        self.status = False 
