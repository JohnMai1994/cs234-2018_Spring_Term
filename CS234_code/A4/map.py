from graph import Graph


# load_map(filename) return the graph by consuming the filename, str.
# load_map: str -> Graph
def load_map(filename):
  graph = Graph()
  f = open("{0}".format(filename), 'r')

  for line in f.readlines():
    k = line.split(" ")
    for item in k:
      if k[0] == ";":
        break
      a = k[0]
      b = k[1]
      wt = int(k[2])
      graph.add_edge(a,b,wt)
      graph.add_edge(b,a,wt)
  f.close()
  return graph
          
    
# directions(graph, a, b) return the shortest path between a, str, and b, str,
#  in the graph, Graph
# directions: Graph Str Str -> listof(Str)
def directions(graph,a,b):
  shortest_distance = {}  
  predecessor = {}
  graph_list = []
  the_graph = graph
  infinity = 99999999999
  path = []
  for node in the_graph:
    shortest_distance[node] = infinity
    graph_list.append(node)
  shortest_distance[a] = 0


  while graph_list:
    minNode = None
    for node in graph_list:
      if minNode is None:
        minNode = node
      elif shortest_distance[node] < shortest_distance[minNode]:
        minNode = node

    for childNode in the_graph.neighbours(minNode):
      if the_graph.weight(minNode, childNode) + shortest_distance[minNode] < shortest_distance[childNode]:
        shortest_distance[childNode] = the_graph.weight(minNode, childNode) + shortest_distance[minNode]
        predecessor[childNode] = minNode
    graph_list.remove(minNode)
    
    currentNode = b
  while currentNode != a:
    try:
      path.insert(0, currentNode)
      currentNode = predecessor[currentNode]
    except KeyError:
      print('Path not reachable')
      break  
  path.insert(0,a)
    
  return path
