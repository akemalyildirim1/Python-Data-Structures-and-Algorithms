"""
Tree Implentation:
"""

class TreeNode:

  #Constructor:
  def __init__(self, value):
    #çocukları başta boş bir liste olarak tanımlıyoruz
    self.value = value # data
    self.children = [] # references to other nodes

  def add_child(self, child_node):
    #çocuk ekleme fonksiyonu içine başka bir TreeNode type'ında obje vererek yapıyoruz.
    # creates parent-child relationship
    print("Adding " + child_node.value)
    #aslında bu node'u parent dosyanın children isimli listesine ekliyor.
    self.children.append(child_node) 
    
  def remove_child(self, child_node):
    #çocuk çıkartmak için bir döngü döndürüp bu döngüde istemediğimiz değerleri eklemeyerek yeni bir liste elde edip onu children listesine eşitliyoruz.
    # removes parent-child relationship
    print("Removing " + child_node.value + " from " + self.value)
    self.children = [child for child in self.children 
                     if child is not child_node]

  def traverse(self):
    #döngünün içndeki bütün nodeları dönmek için yapıyoruz.
    # moves through each node referenced from self downwards
    #önce root'u bir listeye atıyoruaz bu listenin içinde işlemi devam ettiriyoruz.
    nodes_to_visit = [self]
    while len(nodes_to_visit) > 0:
      #listenin içinde eleman kalmayana kadar döndürüyoruz.
      #pop methodu bize attığımız elemanı döndürdüğü için current_node değişkenine bu nodeu alıyoruz
      current_node = nodes_to_visit.pop()
      print(current_node.value)
      
      #bu listeye attığımız node'un çocuklarını atarak daha sonra onlara ulaşmış oluyoruz.
      nodes_to_visit += current_node.children
