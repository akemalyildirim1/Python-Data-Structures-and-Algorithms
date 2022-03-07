"""

Can be initialized as a directed graph, where edges are set in one direction.

Stores every vertex inside a dictionary

Vertex data is the key and the vertex instance is the value.

Has methods to add vertices, edges between vertices, and determine if a path exists between two vertices.

"""

class Graph:
  #constructor:
  def __init__(self, directed = False):
    #eğer directed tanımlanmadıysa veya False olarak tanımlandıysa bi-directional gibi düşünülüyor.
    #eğer directed True tanımlandıysa directional bir graph oluşturuluyor.
    #graph'in içindeki vertex'ler dictionary içinde tutuluyor. Key elemanı vertex'in değeri,pair elemanı da vertex'in kendisi.
    self.graph_dict = {}
    self.directed = directed

  #graph'e vertex eleman eklemek için!
  def add_vertex(self, vertex):
    #dictionary'e key olarak değeri, pair olarak vertex'i ekliyoruz
    self.graph_dict[vertex.value] = vertex

  #iki vertexi edgelemek için.
  def add_edge(self, from_vertex, to_vertex, weight = 0):
    #eğer weight verilmezse 0 olarak giriliyor.
    #from_vertex'ten direk olarak to_vertex'e bir edge ekliyoruz.
    self.graph_dict[from_vertex.value].add_edge(to_vertex.value, weight)
    #eğer graph directional değil ise to_vertex'e de edge ekleniyor, eğer directional ise eklenmiyor.
    if not self.directed:
      self.graph_dict[to_vertex.value].add_edge(from_vertex.value, weight)

  #path olup olmadığını kontrol etmek için!
  def find_path(self, start_vertex, end_vertex):
    #listenin içine ilk vertexin değerini atıyoruz.
    start = [start_vertex]
    #cycle halinde sonsuz döngüye girmemek için seen dictionary'si oluşturup gezdiğimiz vertexleri buna True şeklinde ekliyoruz.
    seen = {}
    #start'ın içi boşalana kadara döngüye sokuyoruz.
    while len(start) > 0:
      #önce startın ön elemanını alıp current_vertex'e eşitleyip listeden atıyoruz.
      current_vertex = start.pop(0)
      #bunu da seen dictionaryisine atıp True olarak pairliyoruz.
      seen[current_vertex] = True
      print("Visiting " + current_vertex)
      #eğer aradığımz değeri bulmuşsak True döndürüyoruz.
      if current_vertex == end_vertex:
        return True
      else:
        #gezilecek vertexleri current_edge'in vertexini graph'in içindeki dictionary değişkeninden çekiyoruz 
        vertices_to_visit = set(self.graph_dict[current_vertex].edges.keys())
        #eğer bunlar seen dictionaryisinde kayıtlı değilse start listesinin sağına bu değerleri ekleyip bunları da döngüde gezerek aradığımız noktayı arıyoruz.
        start += [vertex for vertex in vertices_to_visit if vertex not in seen]
    #eğer döngü bittiğinde hala True dönmemişse o vertex'e ulaşamıyoruz demektir. Böylece False döndürüyoruz.
    return False
