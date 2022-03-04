from Node import Node
class LinkedList:
  def __init__(self, value=None):
    self.head_node = Node(value)
  
  def get_head_node(self):
    return self.head_node
  
  def insert_beginning(self, new_value):
    new_node = Node(new_value)
    new_node.set_next_node(self.head_node)
    self.head_node = new_node
    
  def stringify_list(self):
    string_list = ""
    current_node = self.get_head_node()
    while current_node:
      if current_node.get_value() != None:
        string_list += str(current_node.get_value()) + "\n"
      current_node = current_node.get_next_node()
    return string_list
  
  def remove_node(self, value_to_remove):
    current_node = self.get_head_node()
    if current_node.get_value() == value_to_remove:
      self.head_node = current_node.get_next_node()
    else:
      while current_node:
        next_node = current_node.get_next_node()
        if next_node.get_value() == value_to_remove:
          current_node.set_next_node(next_node.get_next_node())
          current_node = None
        else:
          current_node = next_node
    
    
  def swap_nodes(input_list, val1, val2):
    print(f'Swapping {val1} with {val2}')

    #We must first find node1 and node2:
    #bunun içini önce node1_prev ve node2_prev i None a eşitleyerek döngü içinde dönüyor.
    node1_prev = None
    node2_prev = None
    node1 = input_list.head_node
    node2 = input_list.head_node
       
    #Edge case 1:
    #değerler eşitse direk fonksiyonu bitirir
    if val1 == val2:
        print("Elements are the same - no swap needed")
        return
    
    #to find node1:
    while node1 is not None:
        if node1.get_value() == val1:
            break
        node1_prev = node1
        node1 = node1.get_next_node()

    #to find node2:
    while node2 is not None:
        if node2.get_value() == val2:
            break
        node2_prev = node2
        node2 = node2.get_next_node()

    #Edge case 2:
    #değerler linkedlistte yoksa fonksiyonu bitirir
    if (node1 is None or node2 is None):
        print("Swap not possible - one or more element is not in the list")
        return

    #node1_prev none ise node1 linkedlistin headi demek
    if node1_prev is None:
        input_list.head_node = node2
    else:
        node1_prev.set_next_node(node2)
    
    #node2_prev none is non2 linkedlistin headi demek
    if node2_prev is None:
        input_list.head_node = node1
    else:
        node2_prev.set_next_node(node1)

    #node1in next nodunu temp değişkenine atadık bunu daha sonra node2nin next noduna atıyoruz.
    temp = node1.get_next_node()
    node1.set_next_node(node2.get_next_node())
    node2.set_next_node(temp)
    
    def nth_last_node(linked_list, n):
        #linked listin sondan n. elemanını bulmak için kullanılacak kod
        #bunun için iki farklı takip edici pointer kullanıyoruz.
        #current arkadan gelen , tail_seeker önden giden pointer olacak
        #counter>=n+1 durumu sağlandığında current pointerı da headden başlayarak tek tek gelmeye başlayacak
        #böyle while döngüsü bittiğinde counter pointerı sondan n. eleman olmuş olacak
        
        """
        PSEUDO CODE:
            nth last pointer = None
            tail pointer = linked list head
            count = 1

            while tail pointer exists
              move tail pointer forward
              increment count

              if count >= n + 1
                if nth last pointer is None
                  set nth last pointer to head
                else
                  move nth last pointer forward

            return nth last pointer
        """
        
        current = None
        tail_seeker = linked_list.head_node
        count = 1
        while tail_seeker:
            tail_seeker = tail_seeker.get_next_node()
            count += 1
            if count >= n + 1:
            if current is None:
                current = linked_list.head_node
            else:
                current = current.get_next_node()
        return current
       
    
    def find_middle(linked_list):
    #Linked listin mid elemanını bulmak için kullanıyoruz.
    #bir ptr iki adım giderken öbürü tek adım gidiyor.
    
    """
    PSEUDO CODE:
        fast pointer = linked list head
        slow pointer = linked list head
        while fast pointer is not None
          move fast pointer forward
          if the end of the linked list has not been reached
            move fast pointer forward
            move slow pointer forward
        return slow pointer
    """
    
    fast = linked_list.head_node
    slow = linked_list.head_node
    while fast:
        fast = fast.get_next_node()
        if fast:
            fast = fast.get_next_node()
            slow = slow.get_next_node()
    return slow
    