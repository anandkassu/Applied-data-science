import networkx as nx
import matplotlib.pyplot as plt

G=nx.watts_strogatz_graph(20,2,0.8,seed=0)
# nx.draw_networkx(G)


#to get connected graph
G1=nx.connected_watts_strogatz_graph(20,2,0.8,100,seed=0)
print("av clusting :{}".format(nx.average_clustering(G1)))
print("av shotest path :{} ".format(nx.average_shortest_path_length(G1)))

nx.draw_networkx(G1)


plt.show()