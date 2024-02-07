class Employee:
    def __init__(self,name=''):
        #self.name=name
        print('nalla constructor')
    def __init__(self,name):
        self.name=name

emp=Employee()
emp.name="Rohit"
print(emp.name)

emp2=Employee("Ashu")
print(emp2.name)

