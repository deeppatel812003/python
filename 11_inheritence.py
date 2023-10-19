class employee:
    company = "google"

    def showdetails(self):
        print("This is an employee")

class programmer(employee):
    language = "python"
    company = "YT"

    def  getlanguge(self):
        print(f"The language is {self.language}")

    def showdetails(self):
        print("This is an programmer")

a = employee()
a.showdetails()
p = programmer()
p.showdetails()
print(p.company)
print(p.language)
print(p.company)