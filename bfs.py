import dsc40graph
from collections import deque

def assign_good_and_evil(graph):    
    status = {node: 'undiscovered' for node in graph.nodes}
    edges = {node: graph.neighbors(node) for node in graph.nodes}
    
    # Good and evil assignment in status dict
    for node in graph.nodes:
        if status[node] == 'undiscovered':
            bfs(graph, node, status)
    
    # Check if any node's edges have same status as node. Return None if true
    for node in graph.nodes:
        for edge in edges[node]:
            if status[node] == status[edge]:
                return None
    
    # If none of the edges of any node have same status, return status dict 
    return status

    
def bfs(graph, source, status):
    # Good and evil assignment based on distance
    distance = {node: float('inf') for node in graph.nodes}
    
    # Starting node is labelled good
    status[source] = 'good'
    distance[source] = 0
    pending = deque([source])
    
    while pending:
        u = pending.popleft()
        
        for v in graph.neighbors(u):
            # If node is undiscovered, change its status to good if it is at 
            # a distance which is a multiple of 2, else change to evil
            if status[v] == 'undiscovered': 
                distance[v] = distance[u] + 1
                pending.append(v)
        
                if distance[v] % 2 == 0:
                    status[v] = 'good'
                else:
                    status[v] = 'evil'
