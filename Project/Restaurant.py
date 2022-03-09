"""
Restaurants have 4 properties: Name, Price, Rating, Address:
"""

class Restaurant:
    #Constructor:
    def __init__(self, name, price, address):
        #Information of the restaurant is kept in a list.
        #self.data[-1]-> type of the node!
        self.data = [name, price, address, type]
        #Initially, any node didn't have any connection.
        self.next_node = None
    
    #Setter of the next node of the Restaurant node.
    def set_next_node(self,other_node):
        self.next_node = other_node
    
    #Getter of the next node of the Restaurant node.
    def get_next_node(self):
        return self.next_node


