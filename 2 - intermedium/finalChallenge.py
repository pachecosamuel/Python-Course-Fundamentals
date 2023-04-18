product_list = {'freezer': 2500, 'microwave': 350, 'stove': 1300, 'mixer': 150}
discounted_products = {p: (value * 0.95) for p, value in product_list.items()}

print(product_list)
print(discounted_products)
