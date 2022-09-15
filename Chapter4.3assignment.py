#first part of the assignment
clothes = ["socks", "shirt", "skirt", "scarf"]
def insert_element(new_cloth, index):
    clothes.remove("socks")
    new_cloth = ["pants", "shoes"]
    clothes.insert(-2, new_cloth)
    clothes.insert(0, new_cloth)

#secend part of the assignment
employee_shift = ["Mike", "Andrew", "Emma", "Kelly", "John", "Brad"]
def replace_employee():
    old_employee = ["Mike", "Andrew", "Emma", "Kelly", "John", "Brad"]
    new_employee = [""]
    new_employee.extend(old_employee)
    print(new_employee)
