"""
Node Class of this linked list class is Restaurant.
"""
from Restaurant import Restaurant

class LinkedList:
    #Constructor
    def __init__(self):
        #Initialized as empty linked list.
        self.head = None

    #Getter of the head node value:
    def get_head_node(self):
        return self.head
    
    #Adder function of the LinkedList.
    #Linked list should keep the value as lexicographically by considering their names:
    def insert(self,name, price, rating, address):
        new_node = Restaurant(name, price, rating , address)
        current_node = self.get_head_node()
        
        #If the linked list is empth, there will be no head, Then the new node will be head.
        if current_node is None:
            self.head = new_node
            return self.head.get_name()

        #If new_node's has more priority than current head, it will be the new head.
        if new_node.get_name() < current_node.get_name() :
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
        current_node = self.get_head_node()
        while current_node:
            if current_node.get_name() is not None:
                print ("-------------------")
                print("")
                print(f"Name: {current_node.get_name()}")
                print(f"Price: {current_node.get_price()}")
                print(f"Rating: {current_node.get_rating()}")
                print(f"Address: {current_node.get_address()}")
                print("")
            current_node = current_node.get_next_node()
        print ("-------------------")