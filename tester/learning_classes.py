

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def print_full_name(self):
        print(self.first + ' ' + self.last)


emp1 = Employee('duy', 'le', 100000)

emp1.print_full_name()


