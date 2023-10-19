class employee:
    company = "google"
    salary = 200

deep = employee()
mithil = employee()
print(deep.company)
print(mithil.company)
deep.salary = 200
mithil.salary = 300
employee.company = "youtube"
print(deep.company)
print(mithil.company)
print(deep.salary)
print(mithil.salary)