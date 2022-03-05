"""
A max-heap tracks the maximum element as the element at index 1 within an internal Python list.

Max-heaps must maintain the heap property that the parent values must be greater than their children.

When adding elements, we use .heapify_up() to compare the new element with its parent; if it violates the heap property, then we must swap the two values.

"""

class MaxHeap:
  #constructor:
  #bir liste veriliyor ve bu listenin başta içinde None var bunun nedeni indexi düzenlemek.
  #Heap'i binary tree gibi implement ettiğimiz için index çok önemli bu nedenle None koyarak index'i 1 den başlatabiliyoruz.
  def __init__(self):
    self.heap_list = [None]
    self.count = 0

  # HEAP HELPER METHODS
  # DO NOT CHANGE!
  #her node'un parent node'u onun indexinin 2'ye tam bölümüyle bulunuyor.
  def parent_idx(self, idx):
    return idx // 2

  #her node'un sol çocuğu onun indexinin 2 katı indexinde 
  def left_child_idx(self, idx):
    return idx * 2

  #her node'un sağ çocuğu onun indexinin 2katının1  fazlası indexinde .
  def right_child_idx(self, idx):
    return idx * 2 + 1

  # END OF HEAP HELPER METHODS
  
  #heap'e eleman eklemek için!
  def add(self, element):
    #counter'ı yani indeximizi bir artırıyoruz.
    self.count += 1
    print("Adding: {0} to {1}".format(element, self.heap_list))
    #elemanları tuttuğumuz listeye append ediyoruz.
    self.heap_list.append(element)
    #max_heap'in düzenli kalması için kullanıdğımız heapify_up fonksiyonunu çağırarak sıranın karışmamasını engelliyoruz.
    self.heapify_up()
    
  def heapify_up(self):
    #düzenli bir şekilde heap oluşturmayı sağlayan asıl fonskiyon bu
    print("Heapifying up")
    #önce yeni eklenen değerin indexini buluyoruz bunu count değişkeninde tuttuğumuz için direk alabiliyoruz.
    idx = self.count
    #bir döngü içinde parent nodelarını inceleyeceğiz
    while self.parent_idx(idx) > 0:
      #önce eklediğimiz node'a bakıyoruz sonra da onun parent node'una yani idx//2 indexine sahip olan node'a bakıyoruz
      child = self.heap_list[idx]
      parent = self.heap_list[self.parent_idx(idx)]
      #eğer eklenen node, parent node'undan büyük ise yer değiştiriyoruz.
      if parent < child:
        print("swapping {0} with {1}".format(parent, child))
        self.heap_list[idx] = parent
        self.heap_list[self.parent_idx(idx)] = child
      #sonraki parentlarından da büyük olup olmadığını kontrol etmek için parent_idx'inden döngüyü devam ettiriyoruz.
      idx = self.parent_idx(idx)
    print("Heap Restored {0}".format(self.heap_list))

""" 
Denemek için bu kodu kullanabiliriz:

# import random number generator
from random import randrange
# import heap class
from max_heap import MaxHeap 

# make an instance of MaxHeap
max_heap = MaxHeap()

# populate max_heap with random numbers
random_nums = [randrange(1, 101) for n in range(6)]
for el in random_nums:
  max_heap.add(el)


# test it out, is the maximum number at index 1?
print(max_heap.heap_list)





"""