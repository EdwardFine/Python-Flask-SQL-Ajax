class Product:
    ids = {}
    def __init__(self,name,price,catagory):
        self.name = name
        self.price = price
        self.catagory = catagory
        self.id = self.generate_id()
    
    def update_price(self,percent_change,is_increased):
        if is_increased:
            self.price = round(self.price*(1+percent_change),2)
        else:
            self.price = round(self.price*(1-percent_change),2)
        return self
    
    def print_info(self):
        print(f"Product: {self.name}")
        print(f"Catagory: {self.catagory}")
        print(f"Price: {self.price}")
        print(f"Id: {self.id}")
        return self
    
    def generate_id(self):
        if self.name in Product.ids.keys():
            return Product.ids[self.name]
        else:
            Product.ids[self.name] = len(Product.ids)+1
            return Product.ids[self.name]

