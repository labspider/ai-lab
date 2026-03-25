from collections import deque

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

def bfs(graph, root):
    visited = []
    queue = deque([root])

    while queue:
        # Remove the first node from the queue
        node = queue.popleft()
        visited.append(node)
        
        # Add all children of the current node to the queue
        for neighbor in graph[node]:
            queue.append(neighbor)
            
    return visited

# Execute BFS
print("BFS Result:", " ".join(map(str, bfs(tree, 1))))