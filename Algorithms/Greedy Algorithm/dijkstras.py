from heapq import heappop, heappush
#Dijkstras uses heap to improve to codes complexity. Python has already heap library. So, we dont need to create it again.
from math import inf

#Assumption: Graph is given as dictionary.
graph = {
        'A': [('B', 10), ('C', 3)],
        'C': [('D', 2)],
        'D': [('E', 10)],
        'E': [('A', 7)],
        'B': [('C', 3), ('D', 2)]
    }


def dijkstras(graph, start):
  #type of distances is library
  distances = {}
  
  for vertex in graph:
    #Firstly, we defined all distances as infinity.
    distances[vertex] = inf
  #But only start vertex will have 0 distance.
  distances[start] = 0
  #It is our heapq. 
  vertices_to_explore = [(0, start)]
  
  while vertices_to_explore:
    #vertices_to_explore is the list of tuples. So current_distance is the first element, current_vertex is the second element of the tuple.
    current_distance, current_vertex = heappop(vertices_to_explore)
    
    #we need to consider neighbors of the vertex to find smallest distance.
    for neighbor, edge_weight in graph[current_vertex]:
      #Firstly, we calculate the distance between the neighbor and start point
      new_distance = current_distance + edge_weight
      #If this distance is smaller than the dictionary's distance. We change the dictionary.
      if new_distance < distances[neighbor]:
        distances[neighbor] = new_distance
        heappush(vertices_to_explore, (new_distance, neighbor))
        
  return distances
        
distances_from_d = dijkstras(graph, 'D')
print("\n\nShortest Distances: {0}".format(distances_from_d))
