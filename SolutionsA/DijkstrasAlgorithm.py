

def dijkstra(graph, start, goal):
    shortest_distance = {} # for keeping the track of updated minimal distance of each nodes.
    predecessor = {} # for keeping track of previous nodes of the traversed nodes which is later used to construct the shortest path from source to goal node.
    unVisitedNodes = graph #for keeping track of unvisited nodes in the graph.
    infinity = float("inf")
    path = []
    for node in unVisitedNodes:
        shortest_distance[node] = infinity
        shortest_distance[start] = 0
    
    # loop until there are nodes in the unvisited nodes list.
    while unVisitedNodes:
        minNode = None # node with minimal distance initially set to None.

        for node in unVisitedNodes:
            if minNode is None:
                minNode = node  # initially set the first node (start node) as minimal node.
            elif shortest_distance[node] < shortest_distance[minNode]:
                minNode = node 

        for childNode, weight in graph[minNode].items():
            if weight + shortest_distance[minNode] < shortest_distance[childNode]:
                shortest_distance[childNode] = weight + shortest_distance[minNode]
                predecessor[childNode] = minNode 
        unVisitedNodes.pop(minNode) #popping out the visited node.

    currentNode = goal
    while currentNode != start:
        try:
            path.insert(0,currentNode)                  # insert current node at the first index of the path and change that current node to its predecessor.
            currentNode = predecessor[currentNode]
        except KeyError:
            print('Path not reachable!')        #path is unreachable if the current node has no predecessor.
            break
    path.insert(0,start)
    if shortest_distance[goal] != infinity:         #checks if the shortest distance of the goal node has been calculated.
        print(f'Shortest distance is: {shortest_distance[goal]}')
        print(f'The shortest path from "{start}" to "{goal}" is: {path}')                   


"""
    Using python dictionary to represent graph 
    where each key represents vertices in the graph and
    the nested dictionary inside a key vertex represents
    the adjancent vertices and their distance from the key vertex.
"""
sample_graph = {
    'a':{'b': 10, 'c': 3},
    'b':{'c': 1, 'd': 2},
    'c':{'d': 8, 'e': 2},
    'd':{'e': 7},
    'e':{'d': 9}
}

print(f'The sample graph represented using nested python dictionary: {sample_graph}')
dijkstra(sample_graph, 'a', 'e')   

# print(f'Shortest distance: {shortest_distance}')