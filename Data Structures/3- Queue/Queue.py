from Node import Node

class Queue:
  def __init__(self, max_size=None):
    #max size belirlemez isek her zaman yerimiz olacağı için sınırsız ekleyebiliriz.
    self.head = None
    self.tail = None
    self.max_size = max_size
    self.size = 0
    
  def enqueue(self, value):
    #sona eleman eklemek için kullanılıyor
    #eğer uygun yer yoksa gerekli bildirimi ekrana basıyor
    if self.has_space():
      item_to_add = Node(value)
      print("Adding " + str(item_to_add.get_value()) + " to the queue!")
      if self.is_empty():
        #eğer queue boşsa eklenen eleman hem head hem tail olacak
        self.head = item_to_add
        self.tail = item_to_add
      else:
        self.tail.set_next_node(item_to_add)
        self.tail = item_to_add
      self.size += 1
    else:
      print("Sorry, no more room!")
         
  def dequeue(self):
    #baştan eleman çıkarmak için kullanılıyor
    #eğer çıkarılacak eleman yoksa gerekli bildirimi ekrana basıyor
    if self.get_size() > 0:
      item_to_remove = self.head
      print(str(item_to_remove.get_value()) + " is served!")
      if self.get_size() == 1:
        #eğer queueda tek eleman varsa hem head hem taili siliyor
        self.head = None
        self.tail = None
      else:
        self.head = self.head.get_next_node()
      self.size -= 1
      return item_to_remove.get_value()
    else:
      print("The queue is totally empty!")
  
  def peek(self):
    #quenun önündeki elemanın datasını almak için
    if self.size > 0:
      return self.head.get_value()
    else:
      print("No orders waiting!")
  
  def get_size(self):
    #queudaki eleman sayısını almak için
    return self.size
  
  def has_space(self):
    #queueda yer olup olmadığına bakmak için
    if self.max_size == None:
      return True
    else:
      return self.max_size > self.get_size()
    
  def is_empty(self):
    #queuenun boş olduğunu kontrol etmek için
    return self.size == 0