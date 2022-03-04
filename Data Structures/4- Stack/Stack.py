from Node import Node

class Stack:
  def __init__(self, limit=1000):
    #limite değer verilmez ise 1000 olarak başlayacak
    self.top_item = None
    self.size = 0
    self.limit = limit
  
  def push(self, value):
    #stacke eleman eklemek için
    #eğer yer yoksa gerekli bildirimi ekrana basacak
    #yer varsa stackin üstüne elemanı ekleyip eleman sayısını 1 artıracak
    if self.has_space():
      item = Node(value)
      item.set_next_node(self.top_item)
      self.top_item = item
      self.size += 1
      print("Adding {} to the pizza stack!".format(value))
    else:
      print("No room for {}!".format(value))

  def pop(self):
    #stackten eleman çıkarmak için
    #eğer çıkarılacak eleman yoksa yani size 0 a eşitse gerekli bildirimi ekrana basacak
    #eğer çıkarabilirse stackin eleman sayısını da 1 eksiltecek
    if not self.is_empty():
      item_to_remove = self.top_item
      self.top_item = item_to_remove.get_next_node()
      self.size -= 1
      print("Delivering " + item_to_remove.get_value())
      return item_to_remove.get_value()
    print("All out of pizza.")

  def peek(self):
    #stackte eğer eleman varsa en üstteki elemanın değerini ekrana bascak
    if not self.is_empty():
      return self.top_item.get_value()
    print("Nothing to see here!")

  def has_space(self):
    #helper method
    #stackte yer varsa doğru dönecek yer yoksa yanlış dönecek
    return self.limit > self.size

  def is_empty(self):
    #stack tamamen boş ise doğru dönecek, 1 eleman bile olsa yanlış dönecek
    return self.size == 0