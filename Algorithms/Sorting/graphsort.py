"""
Depth First Search and Bread First Search
"""

"""
DFS:

depth-first search, known as DFS follows each possible path to its end

"""

def dfs(graph, current_vertex, target_value, visited = None):
  #4 inputu var:
  #graph, bu kodda dictionary olarak alınıyor. eğer farklı bir türde alınırsa for döngüsü içinde graph'in komşularını belirten kısmı düzenlemek yeterli olacaktır.
  #current_vertex: başlanıç verteximiz
  #visited'ı inputa ekleme nedenimiz kodun recursive olması
  if visited is None:
    #eğer visited tanımlanmadıysa boş bir liste olarak koda devam edecek
    visited = []
  #current_vertex'i okuduğumuz için ve tekrar okumamak için visited listesine ekliyoruz.
  visited.append(current_vertex)
  #eğer current_verteximiz aradığımız değerse içinde gezdiğimiz nodeların listesi olan visited'ı döndürüyoruz.
  if current_vertex is target_value:
    return visited
  
  #eğer bulamamışsak komşu nodelara geçmemiz gerekiyor:
  for neighbor in graph[current_vertex]:
    #eğer komşu hala gezilmemiş ise onun edgelerini de gezmek için recursive bir şekilde bu fonskiyonu çağırıyoruz.
    if neighbor not in visited:
      path = dfs(graph, neighbor, target_value, visited)
      #eğer path bulunmuşsa direk return edebiliyoruz.
      if path:
        return path
      
      
"""
BFS:

BFS is primarily concerned with the shortest path that exists between two points

Using a queue will help us keep track of the current vertex and its corresponding path.

breadth-first search, known as BFS broadens its search from the point of origin to an ever-expanding circle of neighboring vertices

"""

def bfs(graph, start_vertex, target_value):
#graph, bu kodda dictionary olarak alınıyor. eğer farklı bir türde alınırsa for döngüsü içinde graph'in komşularını belirten kısmı düzenlemek yeterli olacaktır.
  #başlangıç pathi olarak sadece start_vertexini ekliyoruz çünkü her pathin başında onun olmaı gerekiyor.
  path = [start_vertex]
  #daha sonra queue'ya ekleyeceğimiz vertex_and_path'i önce vertex adı sonra da onun şuana kadar sahip olduğu pathi ekleyerek gideceğiz
  vertex_and_path = [start_vertex, path]
  bfs_queue = [vertex_and_path]
  #başta visitedı boş vırakıyoruz.
  visited = set()
  while bfs_queue:
    #queu'nun front elemanını queuedan çıkarıp elimize gelen değerin vertex ve path değerlerini bulup onlar üstünden işleme devam ediyoruz.
    current_vertex, path = bfs_queue.pop(0)
    #current_verteximiz artık gezildiği için visited'a ekleniyor. visited bir set olduğu için .add methodu kullanıldı.
    visited.add(current_vertex)
    #current_vertexin komşularına da bakmak için döngü oluşturuyoruz.
    for neighbor in graph[current_vertex]:
      #eğer daha önceden bu vertexe bakılmışsa döngü devam ediyor
      #eğer bkaılmamış ise ve aradığımız değeri bulmuşsak path'e bu değeri ekleyip sonucu buluyoruz.
      #ama eğer aradığımız değeri bulamamışsak queue'ya bu değeri ve path+bu değeri ekleyerek sonraki nodelarına da bakmak için döngüyü devam ettiriyoruz.
      if neighbor not in visited:
        if neighbor is target_value:
          return path + [neighbor]
        else:
          bfs_queue.append([neighbor, path + [neighbor]])



"""
Kontrol etmek için bunu kullanabiliriz:

some_hazardous_graph = {
    'lava': set(['sharks', 'piranhas']),
    'sharks': set(['piranhas', 'bees']),
    'piranhas': set(['bees']),
    'bees': set(['lasers']),
    'lasers': set([])
  }

print(bfs(some_hazardous_graph, 'sharks', 'bees'))
print(dfs(some_hazardous_graph, 'sharks', 'bees'))

"""