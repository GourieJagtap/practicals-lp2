from queue import PriorityQueue
def prim_mst(graph):
    start_vertex = 1  # Start with vertex 1
    visited = set()
    mst = []  # Minimum Spanning Tree
    total_weight = 0  # Total weight of the MST
    # Initialize priority queue to store edges
    edges = PriorityQueue()
    # Start with the first vertex
    visited.add(start_vertex)
    # Add all the edges from the first vertex to the priority queue
    for neighbor, weight in graph[start_vertex]:
        edges.put((weight, start_vertex, neighbor))
    while not edges.empty():
        weight, u, v = edges.get()
        # Check if the destination vertex has been visited
        if v not in visited:
            visited.add(v)
            mst.append((u, v, weight))
            total_weight += weight
            # Add the edges from the newly visited vertex to the priority queue
            for neighbor, weight in graph[v]:
                edges.put((weight, v, neighbor))
    return mst, total_weight
def main():
    graph = {}
    num_vertices = int(input("Enter the number of vertices: "))
    # Initialize the graph with empty lists for each vertex
    for i in range(1, num_vertices + 1):
        graph[i] = []
    # Get the input for each vertex and its connected neighbors
    for i in range(1, num_vertices + 1):
        num_edges = int(input("Enter the number of edges for vertex {}: ".format(i)))
        for j in range(num_edges):
            neighbor, weight = input("Enter the neighbor and weight (format: neighbor weight) for vertex {}: ".format(i)).split()
            graph[i].append((int(neighbor), int(weight)))
    mst, total_weight = prim_mst(graph)
    print("\nMinimum Spanning Tree:")
    for edge in mst:
        u, v, weight = edge
        print("Edge: {} - {}, Weight: {}".format(u, v, weight))
    print("Total Weight of MST:", total_weight)
if __name__ == "__main__":
    main()

#---------------------------------------------------------------------------

#EXPECTED OUTPUT:
# Enter the number of vertices: 6
# Enter the number of edges for vertex 1: 2
# Enter the neighbor and weight (format: neighbor weight) for vertex 1: 2 5
# Enter the neighbor and weight (format: neighbor weight) for vertex 1: 3 10
# Enter the number of edges for vertex 2: 2
# Enter the neighbor and weight (format: neighbor weight) for vertex 2: 4 9
# Enter the neighbor and weight (format: neighbor weight) for vertex 2: 3 1
# Enter the number of edges for vertex 3: 2
# Enter the neighbor and weight (format: neighbor weight) for vertex 3: 2 1
# Enter the neighbor and weight (format: neighbor weight) for vertex 3: 5 2
# Enter the number of edges for vertex 4: 2
# Enter the neighbor and weight (format: neighbor weight) for vertex 4: 5 1
# Enter the neighbor and weight (format: neighbor weight) for vertex 4: 6 1
# Enter the number of edges for vertex 5: 2
# Enter the neighbor and weight (format: neighbor weight) for vertex 5: 4 1
# Enter the neighbor and weight (format: neighbor weight) for vertex 5: 6 3
# Enter the number of edges for vertex 6: 2
# Enter the neighbor and weight (format: neighbor weight) for vertex 6: 4 1
# Enter the neighbor and weight (format: neighbor weight) for vertex 6: 5 3
#
# Minimum Spanning Tree:
# Edge: 1 - 2, Weight: 5
# Edge: 2 - 3, Weight: 1
# Edge: 3 - 5, Weight: 2
# Edge: 5 - 4, Weight: 1
# Edge: 4 - 6, Weight: 1
# Total Weight of MST: 10
#
# Process finished with exit code 0


# #EXPLAINATION:
# Let's go through the code step by step and explain each part:
#
# prim_mst(graph) function:
#
# This function implements the Prim's Minimum Spanning Tree algorithm.
# It takes a weighted graph represented as a dictionary as input.
# It returns the Minimum Spanning Tree (MST) and the total weight of the MST.
# start_vertex variable:
#
# It specifies the starting vertex for the Prim's algorithm. In this code, it is set to 1.
# visited set, mst list, and total_weight variable:
#
# visited is a set to keep track of the visited vertices.
# mst is a list that will store the edges of the Minimum Spanning Tree.
# total_weight will store the total weight of the MST.
# edges PriorityQueue:
#
# This priority queue is used to store the edges of the graph, ordered by their weights.
# The PriorityQueue is imported from the queue module.
# Initialization:
#
# The starting vertex is added to the visited set to mark it as visited.
# Adding edges to the priority queue:
#
# The edges of the starting vertex are added to the priority queue.
# For each neighboring vertex and its weight, a tuple (weight, start_vertex, neighbor_vertex) is added to the edges priority queue.
# Prim's Algorithm loop:
#
# The algorithm continues until the edges priority queue is empty.
# In each iteration, the edge with the minimum weight is removed from the priority queue using edges.get().
# If the destination vertex of the edge has not been visited:
# The destination vertex is marked as visited by adding it to the visited set.
# The edge is added to the mst list.
# The weight of the edge is added to the total_weight.
# The edges of the destination vertex are added to the priority queue for further consideration.
# main() function:
#
# This function is responsible for taking user input and initializing the graph.
# User input:
#
# The number of vertices in the graph is entered by the user.
# For each vertex, the number of edges is entered.
# For each edge, the neighboring vertex and its weight are entered.
# Prim's MST calculation:
#
# The prim_mst() function is called with the graph.
# The Minimum Spanning Tree (MST) and the total weight of the MST are returned.
# Output:
#
# The Minimum Spanning Tree (MST) is displayed, showing each edge and its weight.
# The total weight of the MST is displayed.
# The code follows the Prim's algorithm to find the Minimum Spanning Tree in a weighted graph. It uses a priority queue to store the edges, ensuring that the edge with the minimum weight is always considered next. The output displays the edges of the MST and the total weight of the MST.