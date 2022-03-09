"""
Node Class of this linked list class is Restaurant.
"""
from hashlib import new
from Restaurant import Restaurant

class LinkedList:
    #Constructor
    def __init__(self, name, price, rating, address):
        #Function parameter is the head node of the linked list.
        self.head=Restaurant(name, price, rating, address)
    
    #Getter of the head node value:
    def get_head_node(self):
        return self.head
    
    #Adder function of the LinkedList.
    #Linked list should keep the value as lexicographically by considering their names:
    def insert(self,name, price, rating, address):
        new_node = Restaurant(name, price, rating , address)
        current_node = self.get_head_node()
        #If new_node's has more priority than current head, it will be the new head.
        if new_node.get_name() < current_node.get_name():
            new_node.set_next_node(current_node)
            self.head = new_node
            return self.head.get_name()

        #To traverse other node, while Truee loop is used.
        while True:
            #If next node exists and lexigrophically propriate, new_node is added in there.
            if current_node.get_next_node() is not None:
                if current_node.get_next_node().get_name() > new_node.get_name():
                    new_node.set_next_node(current_node.get_next_node())
                    current_node.set_next_node(new_node)
                    return new_node.get_name()

                current_node = current_node.get_next_node()

            #If the next node doesn't exist, then the new node will be added as tail node.
            else:
                current_node.set_next_node(new_node)
                return new_node.get_name()
    
    #For visualization of the linked list:
    def stringify_list(self):
        string_list = ""
        current_node = self.get_head_node()
        while current_node:
            if current_node.get_name() is not None:
                string_list += str(current_node.get_name()) +"\n"
            current_node = current_node.get_next_node()
        return string_list
                
                
            
