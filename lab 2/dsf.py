# Defining the tree structure
tree = {
    1: [2, 3],
    2: [4, 5],
    3: [6, 7],
    4: [],
    5: [],
    6: [],
    7: []
}

def dfs(graph, node, visited=None):
    if visited is None:
        visited = []
    
    # Visit the current node
    visited.append(node)
    
    # Recursively visit each child
    for neighbor in graph[node]:
        dfs(graph, neighbor, visited)
        
    return visited

# Execute DFS
print("DFS Result:", " ".join(map(str, dfs(tree, 1))))