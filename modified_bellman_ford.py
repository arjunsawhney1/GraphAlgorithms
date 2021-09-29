import graph

def modified_bellman_ford(graph, weights, source):    
    """
    Bellman-Ford algorithm that returns the dictionary of estimated distances except that est[v] = -float('inf') if there is a negative cycle anywhere along the path from the source to node v
    """
    est = {node: float('inf') for node in graph.nodes}
    est[source] = 0
        
    for i in range(len(graph.nodes) - 1):
        any_changes = False
        
        for (u, v) in graph.edges:
            any_changes = update(u, v, weights, est) or any_changes
        
        if not any_changes:
            break
    
    if any_changes:
        negative_cycle_vertices = []
                
        for (u, v) in graph.edges:
            if update(u, v, weights, est):
                if v not in negative_cycle_vertices:
                    negative_cycle_vertices.append(v)
        
        for v in negative_cycle_vertices:
            est[v] = -float('inf')
    
    return est


def update(u, v, weights, est):
    """
    Update edge (u, v)
    """
    if est[v] > est[u] + weights(u, v):
        est[v] = est[u] + weights(u, v)
        return True
    else:
        return False
