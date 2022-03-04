from linked_list import Node,LinkedList
from blossom_lib import flower_definitions 

#Seperate Chaining kullanılıyor.
class HashMap:

  #constructor:
  def __init__(self,array_size):
    self.array_size=array_size
    self.array=[LinkedList() for i in range(array_size)]
  
  #hash code oluşturucu
  def hash(self,key):
    return sum(key.encode())
  
  #index oluşturucu hashten gelen değeri kullanıyor
  def compress(self,hash_code):
    return hash_code % self.array_size
  
  #yeni eleman eklemek için
  def assign(self,key,value):
    #önce indexi buluyoruz
    array_index=self.compress(self.hash(key))
    #seperate chain kullandığımız için yeni değeri bir nodea aktarıyoruz
    payload=Node([key,value])
    #o indexteki linkedliste erişiyoruz
    list_at_array=self.array[array_index]
    for item in list_at_array:
      #linkedlistin içine bakıyoruz aradığımız key ile eşleşen var ise bunu güncelliyoruz
      if item[0] == key:
        item[1]=value
        return 
    #eğer daha önceden bu key eklenmediyse linkedliste yeni elemanı ekliyoruz
    list_at_array.insert(payload)
  
  def retrieve(self,key):
    #aradığımız keyin değerini bulmak için önce inmdexi buluyoruz sonra da o indexteki linkedlisti elde edip for ile içinde dönüp kontrol ediyoruz.
    array_index=self.compress(self.hash(key))
    list_at_index=self.array[array_index]
    for item in list_at_index:
      if item[0]==key:
        return item[1]
    return [0]

blossom=HashMap(len(flower_definitions))
for flower in flower_definitions:
  blossom.assign(flower[0],flower[1])
print(blossom.retrieve("begonia"))

  