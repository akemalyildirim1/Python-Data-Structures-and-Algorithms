"""
A Binary Search Tree is an efficient data structure for fast (O(log N)) data storage and retrieval.

It is a specialized tree data structure that is made up of a root node, and at most two child branches, or subtrees. 
 
"""
"""
a BinarySearchTree class containing value, depth, and left and right child nodes.

an .insert() method to place a node of a specified value at the correct location in the Binary Search Tree. 
The time efficiency of this operation is O(logN) for a balanced tree - if there are N nodes in the BST, the max depth of a balanced tree is log(N). 
So, this method makes at most log(N) value comparisons. In the worst case of an imbalanced tree (all values on one side), the performance would be O(N).

a .get_node_by_value() method to retrieve a node in the tree by its value. The time efficiency of this operation is also O(logN) for a balanced tree - if there are N nodes in the BST,
 the max depth of the tree is log(N), so this method makes at most log(N) value comparisons. 
 In the worst case of an imbalanced tree (all values on one side), the performance would be O(N).
 
a .depth_first_traversal() method to print the inorder traversal of the Binary Search Tree. This visits every single node, so if there are N nodes, the time efficiency for traversal is O(N)

"""

class BinarySearchTree:
  
  #Constructor
  def __init__(self, value, depth=1):
    self.value = value
    self.depth = depth
    #sol ve sağ çocuklar başlangıçta yok olarak veriliyor.
    self.left = None
    self.right = None

  #ağaca eleman eklemek için!
  def insert(self, value):
    #recursive şekilde çalışıypr
    if (value < self.value):
      #eğer verilen değer parent node'dan daha küçükse sol ağaca eklenmesi gerekiyor
      if (self.left is None):
        #eğer parent node'un sol node'u oluşturulmamışsa bu node'u oluşturuyor.
        self.left = BinarySearchTree(value, self.depth + 1)
        print(f'Tree node {value} added to the left of {self.value} at depth {self.depth + 1}')
      else:
        #eğer parent node'un zaten sol node'u var ise bunla da karşılaştırmayı yapmak için recursive şekilde aynı fonksiyonu çağırıyoruz.
        self.left.insert(value)
    else:
      #eğer verilen değer parent node'dan daha büyük veya eşit ise sağ ağaca eklenmesi gerekiyor
      if (self.right is None):
        #eğer parent node'un sağ ağacı oluşturulmamışsa bu node'u oluşturuyor
        self.right = BinarySearchTree(value, self.depth + 1)
        print(f'Tree node {value} added to the right of {self.value} at depth {self.depth + 1}')
      else:
        #eğer parent node'un zaten sağ node'u var ise bunla da karşılaştırmayı yapmak için recursive şekilde aynı fonksiyonu çağırıyoruz.
        self.right.insert(value)
        
  #ağaçta search yapmak için!!
  def get_node_by_value(self, value):
    #eğer istenilen değer üzerinde olduğumuz node'un değeriyle aynıysa direk değeri return ediyor.
    if (self.value == value):
      return self
    #eğer istediğimiz değer node'dan küçükse ve o node'un sol node'u var ise sol ağaç içinde o değeri aramak için recursive şekilde aynı fonksiyonu çağırıyoruz
    elif ((self.left is not None) and (value < self.value)):
      return self.left.get_node_by_value(value)
    
    #eğer istediğimiz değer node'dan büyükse ve node'un sağ node'u var ise sağ ağaç içinde o değeri aramak için recursive bir şekilde aynı fonksiyonu çağrıyoruz.
    elif ((self.right is not None) and (value >= self.value)):
      return self.right.get_node_by_value(value)
    
    #eğer bulamamışsa None olarak dönüyor.
    else:
      return None
    
  #inorder şekilde traverse etmek için!!
  def depth_first_traversal(self):
    #inorder traversede önce sol node, sonra kendi sonra sağ node'u bastırması gerekiyor.
    #bunun için önce sol node'daki ağacı inceliyoruz ve ardından printliyoruz
    #bu işlemden sonra da sağ ağaçtakileri çağırıp kontrol ediyoruz.
    if (self.left is not None):
      self.left.depth_first_traversal()
    print(f'Depth={self.depth}, Value={self.value}')
    if (self.right is not None):
      self.right.depth_first_traversal()
