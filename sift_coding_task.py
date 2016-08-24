import csv
import networkx as nx
import matplotlib.pyplot as plt


filename = 'D:/Internship/userdata.csv'


G = nx.Graph()
dict = {}
with open(filename, 'rb') as csvfile:
    filereader = csv.reader(csvfile, delimiter = ',')
    next(filereader, None)
    for row in filereader:
        #print ','.join(row)
        graph_nodes = row[2:4]
        #print graph_nodes



        for node in graph_nodes:
            if node not in G:
                G.add_node(node)

        node1 = graph_nodes[0]
        node2 = graph_nodes[1]
        if not G.has_edge(node1, node2):
            G.add_edge(node1, node2 )
            G[node1][node2]['length'] = 1

        else:
            lengt = G[node1][node2]['length']
            G[node1][node2]['length'] = lengt + 1



#print list(G.nodes())
#plotting
pos = nx.spring_layout(G)

nx.draw(G, pos, with_labels = True)
nx.draw_networkx_nodes(G, pos, nodelist = G.nodes())
edge_labels = nx.get_edge_attributes(G, 'length')
nx.draw_networkx_edge_labels(G, pos, edge_labels= edge_labels)
plt.show()











