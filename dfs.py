import graph

def biggest_descendent(graph, root, value):        
    """
    This method defines the biggest descendent value of a node u to be the largest value of any node which is a descendent of u in the given tree graph. This is accomplished using a Depth First Search.
    """
    status = {node: 'undiscovered' for node in graph.nodes}
    # biggest dict initialized to holds values in value dictionary
    biggest = {node: value[node] for node in graph.nodes}
    
    # We use DFS as it visits the leaf nodes before parent nodes. We assign 
    # the biggest descendent from the bottom-up
    dfs(graph, root, status, biggest)
    
    # biggest holds the values of the biggest descendents for each node 
    # after DFS is complete
    return biggest


def dfs(graph, u, status, biggest):
    """
    Helper method to biggest_descendent. Implements recursive DFS algorithm to assign the biggest value among the children of node u to node u in the biggest dictionary
    """
    status[u] = 'pending'
    
    # In a tree, all neighbors are children
    for v in graph.neighbors(u):
        if status[v] == 'undiscovered':
            # Recursive call ensures that leaf nodes are marked visited first
            dfs(graph, v, status, biggest)
            # Check for biggest value among child nodes and set it as value of 
            # parent node in the biggest dictionary
            if biggest[v] > biggest[u]:
                biggest[u] = biggest[v]
    
    status[u] = 'visited'
