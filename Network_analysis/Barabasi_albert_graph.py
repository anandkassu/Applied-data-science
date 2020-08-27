import networkx as nx
import matplotlib.pyplot as plt


#always_receive connected graph
G=nx.barabasi_albert_graph(10,2,seed=0)
nx.draw_networkx(G)
print("av clusting :{}".format(nx.average_clustering(G)))
print("av shotest path :{} ".format(nx.average_shortest_path_length(G)))
plt.show()