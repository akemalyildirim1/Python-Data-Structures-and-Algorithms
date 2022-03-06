"""
A heapsort is a sorting algorithm that uses heaps to organize data.

To implement heapsort, do the following
    1- Place an unordered list into a max-heap.
    2- While the max-heap has at least 1 element, extract the root of the heap and swap it with the left-most child node. 
        The extracted value will be placed at the beginning of a list that contains the sorted values.
    3- After the left-most child is placed at the root of the heap, rebalance the heap by comparing the new root value to the next largest child; 
        if the child is greater than the parent, swap the two values. Continue this process until the heap is restored.
    4- Once the heap is empty, return the sorted list.

"""

"""
class MaxHeap:
  #constructor
  #count eleman sayısını sayıyor
  #heap_list'in içine başta None verdik böylece indexlememiz kolay olacak. Heap'te index çok önemli çünkü tree gibi düşünüp liste gibi implement ediyoruz.
  def __init__(self):
    self.heap_list = [None]
    self.count = 0

  # HEAP HELPER METHODS
  # DO NOT CHANGE!
  #o node'un indexinin 2ye tam bölümü parent node'un indexini veriyor.
  def parent_idx(self, idx):
    return idx // 2

  #node'un indexinin 2 katı sol çocuğunun indexini veriyor
  def left_child_idx(self, idx):
    return idx * 2

  #node'un indexinin 2 katının 1 fazlası sağ çocuğunun indexini veriyor
  def right_child_idx(self, idx):
    return idx * 2 + 1

  #çocuğunun olup olmadığını kontrol etmek için. Sol çocuk olmadığı takdirde sağ çocuk da olmayacağı için solu kontrol etmek yeterli oluyor.
  def child_present(self, idx):
    return self.left_child_idx(idx) <= self.count

  # END OF HEAP HELPER METHODS
  
  #heap'e eleman eklemek için:
  def add(self, element):
    #counter'ı bir artırıyoruz.
    self.count += 1
    print("Adding: {0} to {1}".format(element, self.heap_list))
    #heap_list'e o elemanı sonuna ekliyoruz.
    self.heap_list.append(element)
    #heap'i düzende tutmak için bu fonksiyonu kullanıyoruz.
    self.heapify_up()
    
  #heap_list'i düzenli bir şekilde tutmak için:
  def heapify_up(self):
    print("Heapifying up")
    #önce son elemanın indexini alıyoruz bunu counterdan direk alabiliyoruz.
    idx = self.count
    #döngü içinde root'a kadar bakıyoruz
    while self.parent_idx(idx) > 0:
      #önce çocuk node'un yani yeni eklenen node'un değerini sonra da onun parentini(2*index) değerini buluyoruz.
      child = self.heap_list[idx]
      parent = self.heap_list[self.parent_idx(idx)]
      #bu 2 değeri kıyaslıyoruz. Eğer çocuk node, parent node'dan daha büyükse bunları değiştirmemiz gerekiyor.
      if parent < child:
        print("swapping {0} with {1}".format(parent, child))
        self.heap_list[idx] = parent
        self.heap_list[self.parent_idx(idx)] = child
      #parent nodeları da kontrol etmek için idx'i parentin idxine eşitliyoruz.
      idx = self.parent_idx(idx)
    print("Heap Restored {0}".format(self.heap_list))

  #Heap Sortta kullanmak için en büyük değeri al methodu:
  def retrieve_max(self):
    #counter 0 ise eleman olmayacağı için None döndürüyoruz.
    if self.count == 0:
      print("No items in heap")
      return None
    #heap_list'te en büyük değeri 1. indexte tutuyoruz. heap'ten çıkarmamız gereken değer bu değer.
    max_value = self.heap_list[1]
    print("Removing: {0} from {1}".format(max_value, self.heap_list))
    #en büyük değeri altıkdan sonra heap'e en son eklenen yani listenin en sağdaki elemanını 1.elemanı olarak koyuyoruz(çocuğu olmadığı için işlem kolay oluyor)
    self.heap_list[1] = self.heap_list[self.count]
    #eski max elemanı çıkardığımız için counter'ı 1 eksiltiyoruz.
    self.count -= 1
    self.heap_list.pop()
    print("Last element moved to first: {0}".format(self.heap_list))
    #son elemanı heap'İn başına aldığımız için heap_listi tekrar düzenlememiz gerekiyor bunu bu fonksiyon ile yapıyoruz.
    self.heapify_down()
    #fonksiyon maximum değeri döndürüyor.
    return max_value
  
  #heap_list'in eleman çıkardıktan sonra istenilen heap formatında olması için listede gerekli işlemleri yapıyor!
  def heapify_down(self):
    #max elemanı atıp en sağ elemanı listenin 1.indexine aldığımızdan dolayı bu node ile çocuklarının değerini incelememiz gerekiyor.
    idx = 1
    while self.child_present(idx):
      #çocuk node olana kadar döngüyü döndürüyoruz.
      print("Heapifying down!")
      #node'un en büyük değerine sahip çocuğu almak için fonksiyonu kullanıyoruz.
      larger_child_idx = self.get_larger_child_idx(idx)
      #child değişkenini fonksiyondan gelen indexteki değere atıyoruz, parent değeri de 1.indexte olan değerimiz.
      child = self.heap_list[larger_child_idx]
      parent = self.heap_list[idx]
      #eğer child, parent'tan büyük değere sahipse ikisini yer değiştirmemiz gerekiyor.
      if parent < child:
        self.heap_list[idx] = child
        self.heap_list[larger_child_idx] = parent
      #sonraki çocukları da kontrol etmek için idx'i çocuk node'un indexine eşitliyoruz.
      idx = larger_child_idx
    print("HEAP RESTORED! {0}".format(self.heap_list))
    print("") 

  #node'un en büyük çocuk node'unu bulmak için:
  def get_larger_child_idx(self, idx):
    #eğer sağ çocuğu yoksa direk en büyük çocuk soldaki olacaktır
    if self.right_child_idx(idx) > self.count:
      print("There is only a left child")
      return self.left_child_idx(idx)
    else:
      #2 çocuğunda olduğu durumda değerleri alıyoruz hangisi büyükse direk onu döndürüyoruz.
      left_child = self.heap_list[self.left_child_idx(idx)]
      right_child = self.heap_list[self.right_child_idx(idx)]
      if left_child > right_child:
        print("Left child "+ str(left_child) + " is larger than right child " + str(right_child))
        return self.left_child_idx(idx)
      else:
        print("Right child " + str(right_child) + " is larger than left child " + str(left_child))
        return self.right_child_idx(idx)
"""

def heapsort(lst):
  sort = []
  max_heap = MaxHeap()
  for idx in lst:
    max_heap.add(idx)
  while max_heap.count > 0:
    max_value = max_heap.retrieve_max()
    sort.insert(0, max_value)
  return sort

"""
denemek için:
y_list = [99, 22, 61, 10, 21, 13, 23]
sorted_list = heapsort(my_list)
print(sorted_list)
"""
