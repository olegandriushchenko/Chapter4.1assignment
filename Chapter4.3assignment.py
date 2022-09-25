#first part of the assignment
clothes = ["socks", "shirt", "skirt", "scarf"]
def insert_element(new_cloth = "hats", index):
    clothes.insert(index, new_cloth)
    print(clothes)
insert_element("shoes", 1)
insert_element("coat", -2)
insert_element("suit")

insert_element()


#secend part of the assignment
employee_shift = ["Mike", "Andrew", "Emma", "Kelly", "John", "Brad"]
def replace_employee(employee_shift, old_employee, new_employee):
    old_employee_index = employee_shift.index(old_employee)
    employee_shift.remove(old_employee)
    employee_shift.insert(old_employee_index, new_employee)
    print(employee_shift)

replace_employee(employee_shift, "Kelly", "Maria")
