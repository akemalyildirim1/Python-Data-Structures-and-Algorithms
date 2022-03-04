from collections import deque
#deque -> Double Ended Queue
#for more info : https://www.geeksforgeeks.org/deque-in-python/


# Breadth-first search function
#breadth-first yöntemini kullanarak tree'de eleman aramak için :
def bfs(root_node, goal_value):

  #kütüphaneden eklediğimiz deque veri tipini önce path_queue ismiyle initialize ediyoruz.
  # initialize frontier queue
  path_queue = deque()

  # add root path to the frontier
  #ağaçtaki her elemanın pathinin ilk elemanı root olacağı için ilk başta bunu direk ekliyoruz.
  initial_path = [root_node]
  #appendleft methodu deque tipindeki variable'ların soluna ekleme yapar (append en sağa yapıyor)
  path_queue.appendleft(initial_path)
  
  # search loop that continues as long as
  # there are paths in the frontier
  #path_queue boş olana kadar bir döndü döndürücez(eğer istediğimiz eleman bulunursa döngü duracak)
  while path_queue:
    # get the next path and node 
    # then output node value
    #önce path_quenun en son elemanını atıyoruz ve bunu bir değişkene veriyoruz.
    #değişkenin en sağındaki eleman döngüde aktif olarak çocuklarını da bulmamız gereken elemandır. Bu nedenle current_node -1. indexte.
    current_path = path_queue.pop()
    current_node = current_path[-1]
    print(f"Searching node with value: {current_node.value}")

    # check if the goal node is found
    #istediğimiz değeri bulursa fonksiyonu path olarak döndürüyor.
    if current_node.value == goal_value:
      return current_path

    # add paths to children to the  frontier
    #eğer istediğimiz değeri bulamamışsak çocuklarını da  queuya ekleyip kontrol etmemiz gerekiyor bunun için alttaki döngüyü kullanıyoruz.
    for child in current_node.children:
      #her çocuğun kendi pathi ayrı olmalı bu nedenle kopyalarken içindeki verileri kopyalıyoruz referansı değil.
      new_path = current_path[:]
      new_path.append(child)
      path_queue.appendleft(new_path)

  # return an empty path if goal not found
  return None