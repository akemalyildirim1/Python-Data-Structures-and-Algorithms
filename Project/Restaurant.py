"""
Restaurants have 4 properties: Name, Price, Rating, Address:
"""

class Restaurant:
    #Constructor:
    def __init__(self, name, price, rating, address):
        #Information of the restaurant is kept in a list.
        #self.data[0]-> name
        self.data = [name, price, rating, address]
        #Initially, any node didn't have any connection.
        self.next_node = None
    
    #Getter of the name of the node:
    def get_name(self):
        return self.data[0]
    
    def get_price(self):
        return self.data[1]

    def get_rating(self):
        return self.data[2]
    
    def get_address(self):
        return self.data[3]

    #Setter of the next node of the Restaurant node.
    def set_next_node(self,other_node):
        self.next_node = other_node
    
    #Getter of the next node of the Restaurant node.
    def get_next_node(self):
        return self.next_node


