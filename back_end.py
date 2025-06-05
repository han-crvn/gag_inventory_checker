# Import libraries
from abc import ABC, abstractmethod

# Create class for basic details (name, status, sold or not).
class Items(ABC):
    def __init__(self, name):
        self.name = name
        self.status = "available"

    @abstractmethod
    def get_details(self):
        pass

    def mark_sold(self):
        self.status = "sold"

    def get_status(self):
        return self.status

    def get_name(self):
        return self.name

# Create class for goods (details, prices, mutations).
class Goods(Items):
    def __init__(self, name, mutation, price):
        super().__init__(name)
        self.mutation = mutation
        self.price = float(price)

    def get_details(self):
        return f"{self.name} - ${self.price:.2f} (Mutation: {self.mutation}) [{self.status}]"

    def get_price(self):
        return self.price

    def get_mutation(self):
        return self.mutation
    
# Create class for pets (details, prices).
class Pet(Items):
    def __init__(self, name, weight):
        super().__init__(name)
        self.weight = float(weight)

    def get_details(self):
        return f"{self.name} - {self.weight}kg [{self.status}]"

    def get_weight(self):
        return self.weight
    
# Create class for whole inventory.
