v1 = [1200, 234, 2345, 1560]
v2 = [1245, 300, 2103, 1434]
prods = ['Oven', "Blender", "Fridge", "Tv"]

list_ = {sales[0]: max(sales[1], sales[2]) for sales in zip(prods, v1, v2)}
print(list_)