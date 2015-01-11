
'''
GRAPH OBJECT
'''
class Graph():
    def __init__(self, edges):
        self.edges = []
        for e in edges:
            edge = {}
            edge['head'] = e[0]
            edge['tail'] = e[1]
            edge['weight'] = e[2]
            self.edges.append(edge)

        self.vertices = []
        for e in self.edges:
                self.vertices.append(e['head'])
                self.vertices.append(e['tail'])
        
        
        
'''
dijkstra_shortest_path(graph, source, dest)
Calculates the path and weight of the shortest path between source and dest in the graph.
'''
def dijkstra_shortest_path(graph, source, dest):
    distance = 0
    distances = {}
    for vertex in graph.vertices:
        distances[vertex] = float('inf')
    previous = {}
    weights = {}
    for vertex in graph.vertices:
        previous[vertex] = None
    distances[source] = 0

    vertices_copy = graph.vertices[:]
    adjacent_vertex = {vertex: set() for vertex in graph.vertices}

    for edge in graph.edges:
        adjacent_vertex[edge['head']].add((edge['tail'], edge['weight']))
    
    while vertices_copy:
        vertex = min(vertices_copy, key=lambda vertex: distances[vertex])
        vertices_copy.remove(vertex)
        if distances[vertex] == float('inf') or vertex == dest:
            break
        for v, weight in adjacent_vertex[vertex]:
            alternate = distances[vertex] + weight
            if alternate < distances[v]:      
                distances[v] = alternate
                previous[v] = vertex
        weights[previous[v]] = distances[v]
    distance =  distances[dest]
    shortest_path, vertex = [], dest
    while previous[vertex]:
        shortest_path.insert(0, vertex)
        vertex = previous[vertex]
    shortest_path.insert(0, vertex)
   
    return shortest_path, distance

 
'''
Runs the Shortest Path for file that is passed in

'''
def algo_runner(file_name):
    print 'Running ' + file_name
    points = []
    with open(file_name, 'r') as f:
        i = 0
        for line in f:
            if i != 0:
                line = line.replace('\r\n', '')
                x = line.split( ' ')
                points.append( (x[0],x[1],int(x[2])))
            i =  i + 1
    graph = Graph(points)
    points, distance = dijkstra_shortest_path(graph, "A", "B")
    print distance
    print str(points)


 
if __name__ == '__main__':

    #Test Files Runs
    algo_runner('Case1.txt')
    algo_runner('Case2.txt')
    algo_runner('Case3.txt')


			
