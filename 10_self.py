class employee:
    company = "yt"
    def salary(self):
        print("salary is 10000")
    
    @staticmethod #static method
    def greet():
        print("Good Morning")

    def __init__(self,name,salary,subunit):
        self.name = name
        self.salary = salary
        self.subunit = subunit
        print("employee is created!")

    def getdetails(self):
        print(f"The name of the employee is {self.name}")
        print(f"The name of the employee is {self.salary}")
        print(f"The name of the employee is {self.subunit}")


# meet = employee()
# meet.salary()
# employee.salary(meet)
# meet.greet()
meet = employee("meet", 1000, "fb")
meet.getdetails()