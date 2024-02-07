class Calculator:
    def square(self,num):
        return num*num
    def cube(self,num):
        return num**3
    def sqrt(self,num):
        return num**0.5
    
    @staticmethod
    def greet(name):
        print("hello"+name)
    
   
cal=Calculator()
Calculator.greet("rohit")
print(cal.square(12))
print(cal.cube(3))
print(cal.sqrt(169))

