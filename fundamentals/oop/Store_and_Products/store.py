class Store:
    def __init__(self,name):
        self.name = name
        self.product_list = []
    
    def add_product(self,new_product):
        self.product_list.append(new_product)
        return self
    
    def sell_product(self,id):
        for product in self.product_list:
            if product.id == id:
                self.product_list.remove(product)
                product.print_info()
                sold = True
                break
        if not sold:
            print("Item does not exits")
        return self
    
    def inflation(self,percent_increase):
        for product in self.product_list:
            product.update_price(percent_increase,True)
        return self
    
    def set_clearance(self,catagory,percent_discount):
        for product in self.product_list:
            if product.catagory == catagory:
                product.update_price(percent_discount,False)
        return self
