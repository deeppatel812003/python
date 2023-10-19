class employee:
    company = "visa"
    code = 12

class freelancer:
    company = "fiverr"
    level = 2

class programmer(employee, freelancer):
    name = "raj"

    def upgradelevel(self):
        self.level = self.level + 1

p = programmer()
print(p.company)
print(p.code)
p.upgradelevel()
print(p.level)
print(p.name)