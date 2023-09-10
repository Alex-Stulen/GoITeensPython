
cars = ["\n", "BMW\n", "Audi", "\t", "Mercedes"]

copy_cars = [el.strip() for el in cars if "a" in el.lower()]
print(copy_cars)

# for el in cars:
#     new_el = el.strip()
#     if "a" in new_el.lower():
#         copy_cars.append(new_el)
#
# print(cars)
# print(copy_cars)
# cars[0] = "HAHAHA"
# print(cars)
# print(copy_cars)
