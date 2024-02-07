class Employee:
    company="google"

# rohit=Employee()
# rohit.company="whatsapp"
# print(type(rohit))

rohit=Employee
rohit.company="whatsapp"
print(type(rohit))

print(rohit.company)
print(Employee.company)

