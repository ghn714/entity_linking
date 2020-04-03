import networkx as nx
import numpy as np

def randomWalk(G, d):
    # Choose a random start node
    vertexid = 1
    # Dictionary that associate nodes with the amount of times it was visited
    visited_vertices = {}
    # Store and print path
    path = [vertexid]

    # Restart the cycle
    counter = 0
    # Execute the random walk with size 100,000 (100,000 steps)
    for counter in range(1, d):
        # Extract vertex neighbours vertex neighborhood
        vertex_neighbors = [n for n in G.neighbors(vertexid)]
        # Set probability of going to a neighbour is uniform
        probability = []
        probability = probability + [1. / len(vertex_neighbors)] * len(vertex_neighbors)
        # Choose a vertex from the vertex neighborhood to start the next random walk
        vertexid = np.random.choice(vertex_neighbors, p=probability)
        # Accumulate the amount of times each vertex is visited
        if vertexid in visited_vertices:
            visited_vertices[vertexid] += 1
        else:
            visited_vertices[vertexid] = 1

        # Append to path
        path.append(vertexid)

    print("Path: ", path)
    return path


if __name__ == '__main__':
    # Create Graph
    G = nx.Graph()

    # Add nodes
    G.add_nodes_from(range(0, 9))

    # Add edges
    G.add_edge(0, 1)
    G.add_edge(1, 2)
    G.add_edge(1, 6)
    G.add_edge(6, 4)
    G.add_edge(4, 3)
    G.add_edge(4, 5)
    G.add_edge(6, 7)
    G.add_edge(7, 8)
    G.add_edge(7, 9)
    randomWalk(G, 10)