from collections import defaultdict

def bfs(visited, graph, node, queue):
    visited.add(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s, end=" ")
        for neighbor in graph[s]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

def main():
    visited = set()  # To keep track of BFS visited nodes
    queue = []       # For BFS
    n = int(input("Enter number of nodes: "))
    graph = defaultdict(list)

    for i in range(1, n + 1):
        edges = int(input("Enter number of edges for node {}: ".format(i)))
        for j in range(1, edges + 1):
            neighbor = int(input("Enter neighbor {} for node {}: ".format(j, i)))
            graph[i].append(neighbor)
            graph[neighbor].append(i)  # Add reverse edge for undirected graph

    print("The following is BFS:")
    bfs(visited, graph, 1, queue)

if __name__ == "__main__":
    main()

# OUTPUT:
# Enter number of nodes: 5
# Enter number of edges for node 1: 2
# Enter neighbor 1 for node 1: 2
# Enter neighbor 2 for node 1: 3
# Enter number of edges for node 2: 1
# Enter neighbor 1 for node 2: 4
# Enter number of edges for node 3: 1
# Enter neighbor 1 for node 3: 4
# Enter number of edges for node 4: 1
# Enter neighbor 1 for node 4: 5
# Enter number of edges for node 5: 0
# The following is BFS:
# 1 2 3 4 5
# Process finished with exit code 0


# BFS THEORY:
# BFS (Breadth-First Search) is a graph traversal algorithm that explores all the vertices of a graph in breadth-first order, meaning it visits all the vertices at the same level before moving to the next level. It starts at a chosen node, visits its adjacent nodes, and then visits the neighbors of those nodes, continuing in a level-by-level fashion. BFS uses a queue data structure to keep track of the nodes to be visited. It is often used for tasks such as finding the shortest path between two nodes, solving puzzles, and exploring all reachable nodes in a graph.


# EXPLAINATION:
# Certainly! Here's an explanation of the modified code:
#
# 1. The `bfs` function implements the Breadth-First Search algorithm. It takes four parameters:
#    - `visited`: A set to keep track of visited nodes during the BFS traversal.
#    - `graph`: The graph representation using a defaultdict of lists. It stores the adjacency list of the graph.
#    - `node`: The starting node for the BFS traversal.
#    - `queue`: A list that serves as the queue for BFS.
#
# 2. Inside the `bfs` function, the `visited` set is initialized with the starting node, and the starting node is appended to the queue.
#
# 3. The while loop continues until the queue is empty. In each iteration, it removes the first element from the queue (`queue.pop(0)`) and assigns it to the variable `s`. This represents the current node being visited.
#
# 4. The current node `s` is printed, indicating that it has been visited.
#
# 5. The function then iterates over the neighbors of the current node `s` using the adjacency list `graph[s]`. For each neighbor, it checks if it has not been visited before. If a neighbor is not in the `visited` set, it is added to the set and appended to the queue. This ensures that unvisited neighbors are processed in the subsequent iterations.
#
# 6. The `main` function serves as the entry point of the program. It prompts the user to enter the number of nodes in the graph.
#
# 7. It initializes an empty set `visited` to keep track of visited nodes during BFS and an empty list `queue` to act as the BFS queue.
#
# 8. It creates an empty `defaultdict(list)` called `graph` to represent the graph. This data structure allows adding edges to the graph using the `graph[node].append(neighbor)` syntax, even for previously unseen nodes. It ensures that accessing a non-existent key will create an empty list as the default value.
#
# 9. The program then enters a loop to collect edge information for each node. For each node, it prompts the user to enter the number of edges connected to that node.
#
# 10. Inside the inner loop, it prompts the user to enter the neighbor for each edge and adds the edge to the graph by appending the neighbor to the adjacency list of the current node and vice versa for the undirected graph.
#
# 11. Finally, the program initiates the BFS traversal by calling the `bfs` function with the initial parameters `visited`, `graph`, starting node `1`, and the `queue`.
#
# The BFS algorithm then proceeds to visit nodes in a breadth-first manner, printing the nodes as they are visited.

