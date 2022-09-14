def show_employee(salary="50000"):
    output = "Oleg Andriushchenko" + "Earn" + str(salary) + "dollars a year"
    print(output)


def show_employees(salary = 50000):
	print("Jim earn ", salary, "a year")

salary = 85000
show_employees()
print("Jim earn ", salary, "a year")

def show_employees(name = "Kate", salary = 50000):
	output = name + " make " + salary + " dollars a year "
	print(output)
