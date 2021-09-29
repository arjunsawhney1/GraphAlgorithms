import graph
from collections import deque

def number_of_shortest_paths(graph, source):
    status = {node: 'undiscovered' for node in graph.nodes}
    distance = {node: float('inf') for node in graph.nodes}
    paths = {node: 0 for node in graph.nodes}
            
    status[source] = 'pending'
    pending = deque([source])
    distance[source] = 0
    # There is one shortest path to the source node of length 0
    paths[source] = 1
        
    while pending:
        u = pending.popleft() 
        for v in graph.neighbors(u):
            if status[v] == 'undiscovered':
                status[v] = 'pending'
                distance[v] = distance[u] + 1
                # The number of paths to a node is equal to the number of 
                # paths to its predecessor node when it is first discovered 
                paths[v] = paths[u]
                pending.append(v)
            else:
                # if node has already been visited by bfs, check if the current 
                # path to node has same length as shortest path
                if distance[u] + 1 ==  distance[v]:
                    # Add 1 to number of paths if it is
                    paths[v] += 1
        
        status[u] = 'visited'
    
    return paths
