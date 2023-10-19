class person:
    countary = "india"

    def takebreath(self):
        print("i am breathing")

class employee(person):
    company = "YT"

    def __init__(self):
        super().__init__()  # constructor
        print("Initializig employee...\n")

    def takebreath(self):
        print("i am luckily breathing...")

class programmer(employee):
    company = "honda"

    def takebreath(self):
        super().takebreath()  #SUPER
        print("i am breathing++++++")
p = person()
p.takebreath()
print(p.countary)

e = employee()
e.takebreath()
print(e.company)

pr = programmer()
pr.takebreath()
print(pr.company)