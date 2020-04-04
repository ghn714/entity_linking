"""Weisfeiler_Lehman graph kernel.
Python implementation based on: "Weisfeiler-Lehman Graph Kernels", by:
Nino Shervashidze, Pascal Schweitzer, Erik J. van Leeuwen, Kurt
Mehlhorn, Karsten M. Borgwardt, JMLR, 2012.
http://jmlr.csail.mit.edu/papers/v12/shervashidze11a.html
Author : Sandro Vega-Pons, Emanuele Olivetti
"""

import numpy as np
import networkx as nx
import copy


def WLR(graph_list, h=1, node_label=True):

    graphs = graph_list
    lists = []
    k = [0] * (h + 1)
    n_nodes = 0
    n_max = 0

    # Compute adjacency lists and n_nodes, the total number of
    # nodes in the dataset.

    lists = graph_list.adjacency_list()
    n_nodes = n_nodes + graph_list.number_of_nodes()

    # Computing the maximum number of nodes in the graphs. It
    # will be used in the computation of vectorial
    # representation.
    if (n_max < graph_list.number_of_nodes()):
        n_max = graph_list.number_of_nodes()


    # INITIALIZATION: initialize the nodes labels for each graph
    # with their labels or with degrees (for unlabeled graphs)

    labels = []
    label_lookup = {}
    label_counter = 0

    # label_lookup is an associative array, which will contain the
    # mapping from multiset labels (strings) to short labels
    # (integers)

    if node_label is True:
        l_aux = nx.get_node_attributes(graph_list,
                                       'node_label').values()

        # It is assumed that the graph has an attribute
        # 'node_label'
        labels = np.zeros(len(l_aux), dtype=np.int32)

        for j in range(len(l_aux)):
            if not (l_aux[j] in label_lookup):
                label_lookup[l_aux[j]] = label_counter
                labels[j] = label_counter
                label_counter += 1
            else:
                labels[j] = label_lookup[l_aux[j]]
            # labels are associated to a natural number
            # starting with 0.

    else:
        labels = np.array(list(graph_list.degree().keys()))


    # Simplified vectorial representation of graphs (just taking
    # the vectors before the kernel iterations), i.e., it is just
    # the original nodes degree.

    # MAIN LOOP
    it = 0
    new_labels = copy.deepcopy(labels)

    while it < h:
        # create an empty lookup table
        label_lookup = {}
        label_counter = 0

        for v in range(len(lists)):
            # form a multiset label of the node v of the i'th graph
            # and convert it to a string

            long_label = np.concatenate((np.array([labels[v]]),
                                         np.sort(labels
                                                 [lists[v]])))
            long_label_string = str(long_label)
            # print(long_label_string)
            # if the multiset label has not yet occurred, add it to the
            # lookup table and assign a number to it
            if not (long_label_string in label_lookup):
                label_lookup[long_label_string] = label_counter
                new_labels[v] = label_counter
                label_counter += 1
            else:
                new_labels[v] = label_lookup[long_label_string]

        aux = np.bincount(new_labels)

        labels = copy.deepcopy(new_labels)

        it = it + 1
    return label_lookup

if __name__ == '__main__':
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

    print(WLR(G, 2, False))
