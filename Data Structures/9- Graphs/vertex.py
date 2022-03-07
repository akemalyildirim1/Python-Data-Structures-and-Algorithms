"""
Uses a dictionary as an adjacency list to store connected vertices.

Connected vertex names are keys and the edge weights are values.

Has methods to add edges and return a list of connected vertices.

"""


class Vertex:
  #constructor:
  def __init__(self, value):
    #edge'leri dictionary olarak tutuyoruz, edge'in keyi bağlı olduğu vertex'in değeri pair'i o edge'in weight'i
    self.value = value
    self.edges = {}

  #Vertex'e edge eklemek için. Eğer weight verilmez ise 0 olarak ekleniyor.
  def add_edge(self, vertex, weight = 0):
    self.edges[vertex] = weight
  
  #Vertex'in edgelerini almak için. .keys()-> fonksiyonu dict_keys() dönüyor bunu da listeye çevirmek için list() kullanıyoruz.
  def get_edges(self):
    return list(self.edges.keys())
