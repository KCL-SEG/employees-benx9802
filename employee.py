"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self):
        self.name = ""
        self.pay = 0
        self.description = ""
        self.commission = 0
        self.commissionType = None
        self.num_commissions = 0 
    
    def calculate_commission(self):
        match self.commissionType:
            case None:
                pass
            case 'Bonus':
                self.pay += self.commission
                self.description += f' and receives a bonus commission of {self.commission}'
            case 'Contract':
                self.pay += (self.commission * self.num_commissions)
                self.description += f' and receives a commission for {self.num_commissions} contract(s) at {self.commission}/contract'
            case _:
                pass
    
    def get_pay(self):
        return self.pay

    def __str__(self):
        self.description += f'. Their total pay is {self.pay}.'
        print(self.description)
        return self.description

class HourlyEmployee(Employee):

    def __init__(self, name, hours, rate, commissionType = None, commission = 0, num_commissions = 0):
        self.name = name
        self.pay = hours * rate
        self.hours = hours
        self.rate = rate
        self.description = f'{self.name} works on a contract of {self.hours} hours at {self.rate}/hour'
        self.commission = commission
        self.commissionType = commissionType
        self.num_commissions = num_commissions
        super().calculate_commission()
    

class MonthlyEmployee(Employee):

    def __init__(self, name, pay, commissionType = None, commission = 0, num_commissions = 0):
        self.name = name
        self.pay = pay
        self.description = f'{self.name} works on a monthly salary of {self.pay}'
        self.commission = commission
        self.commissionType = commissionType
        self.num_commissions = num_commissions
        super().calculate_commission()
    


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
#billie = Employee('Billie')
billie = MonthlyEmployee('Billie', 4000)
# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
#charlie = Employee('Charlie')
charlie = HourlyEmployee('Charlie', 100, 25)
# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
#renee = Employee('Renee')
renee = MonthlyEmployee('Renee', 3000, 'Contract', 200, 4)
# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
#jan = Employee('Jan')
jan = HourlyEmployee('Jan',150,25, 'Contract',220,3)
# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
#robbie = Employee('Robbie')
robbie = MonthlyEmployee('Robbie', 2000, 'Bonus', 1500)
# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
#ariel = Employee('Ariel')
ariel = HourlyEmployee('Ariel', 120, 30, 'Bonus', 600)
