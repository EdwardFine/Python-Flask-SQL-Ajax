from store import Store
from product import Product

walmart = Store("Walmart")
walmart.add_product(Product("Nintendo Switch",299,"Electronics"))
walmart.add_product(Product("Play Station 5",499,"Electronics"))
walmart.add_product(Product("Milk",3.17,"Dairy"))

for product in walmart.product_list:
    product.print_info()

walmart.product_list[2].update_price(.05,True)
walmart.sell_product(1)

print("")
for product in walmart.product_list:
    product.print_info()

# walmart.add_product(Product("Whipped Cream",2.48,"Dairy"))
# walmart.inflation(.02)

# for product in walmart.product_list:
#     product.print_info()

# walmart.set_clearance("Dairy",.25)

# for product in walmart.product_list:
#     product.print_info()