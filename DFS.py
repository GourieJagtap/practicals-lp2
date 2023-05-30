def dfs(visited, graph, node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbor in graph[node]:
            dfs(visited, graph, neighbor)

def main():
    visited = set()  # To keep track of DFS visited nodes
    n = int(input("Enter number of nodes: "))
    graph = {}

    for i in range(1, n+1):
        edges = int(input("Enter number of edges for node {}: ".format(i)))
        graph[i] = []
        for j in range(edges):
            neighbor = int(input("Enter neighbor {} for node {}: ".format(j+1, i)))
            graph[i].append(neighbor)
            graph.setdefault(neighbor, [])  # Initialize empty neighbor list
            graph[neighbor].append(i)  # Add reverse edge for undirected graph

    print("The following is DFS:")
    dfs(visited, graph, 1)
    print()

if __name__ == "__main__":
    main()

#---------------------------------------------------------------------------

#OUTPUT
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
# The following is DFS:
# 1 2 4 5 3
#
# Process finished with exit code 0

#---------------------------------------------------------------------------

# DFS THEORY:
# DFS (Depth-First Search) is a graph traversal algorithm that explores as far as possible along each branch before backtracking. It starts at a chosen node, visits the adjacent unvisited nodes, and recursively applies the same process to them. It continues this process until all nodes have been visited or a certain condition is met. DFS is commonly used for graph-related tasks such as finding paths, detecting cycles, and determining connected components.

#---------------------------------------------------------------------------

# EXPLAINATION OF CODE:
# Certainly! Here's an explanation of the code line by line:

####################################
# ```python
# def dfs(visited, graph, node):
#     if node not in visited:
#         print(node, end=" ")
#         visited.add(node)
#         for neighbor in graph[node]:
#             dfs(visited, graph, neighbor)
# ```
####################################

# - This defines a depth-first search (DFS) function that takes in the `visited` set, `graph` dictionary, and the current `node` as parameters. It performs a recursive DFS traversal on the graph.
# - If the `node` is not in the `visited` set, it prints the `node`, adds it to the `visited` set, and recursively calls `dfs` for each `neighbor` of the `node` in the `graph`.

####################################
# ```python
# def main():
#     visited = set()  # To keep track of DFS visited nodes
#     n = int(input("Enter number of nodes: "))
#     graph = {}
# ```
####################################

# - The `main` function initializes an empty `visited` set to keep track of visited nodes during DFS.
# - It prompts the user to enter the number of nodes in the graph and stores it in `n`.
# - It also initializes an empty `graph` dictionary to store the adjacency list representation of the graph.

####################################
# ```python
# for i in range(1, n+1):
#     edges = int(input("Enter number of edges for node {}: ".format(i)))
#     graph[i] = []
#     for j in range(edges):
#         neighbor = int(input("Enter neighbor {} for node {}: ".format(j+1, i)))
#         graph[i].append(neighbor)
#         graph.setdefault(neighbor, [])  # Initialize empty neighbor list
#         graph[neighbor].append(i)  # Add reverse edge for undirected graph
# ```
####################################

# - This loop iterates over each node in the graph.
# - For each node, it prompts the user to enter the number of edges (neighbors) for that node and stores it in `edges`.
# - It initializes an empty list for the node in the `graph` dictionary.
# - It then iterates `edges` number of times to get the neighbors of the node.
# - For each neighbor, it prompts the user to enter the neighbor's value and adds it to the list of neighbors for the current node in `graph`.
# - It also uses `graph.setdefault(neighbor, [])` to ensure that an empty list is created for the neighbor if it doesn't already exist in the `graph` dictionary. This initializes an empty neighbor list for each node, preventing a KeyError when adding reverse edges for undirected graph representation.

####################################
# ```python
# print("The following is DFS:")
# dfs(visited, graph, 1)
# print()
# ```
####################################

# - This code prints a message indicating that the following output is the DFS traversal of the graph.
# - It then calls the `dfs` function with the `visited` set, `graph` dictionary, and the starting node as arguments to perform the DFS traversal.
# - Finally, it prints a newline character to separate the output from the prompt.

####################################
# ```python
# if __name__ == "__main__":
#     main()
# ```
####################################

# - This condition checks if the script is being run directly (not imported as a module).
# - If it is the main script, it calls the `main` function to start the program.

