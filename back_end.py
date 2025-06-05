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

# Create class for pets (details, prices).

# Create class for whole inventory.
