import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import bipartite 


G=nx.Graph()

G.add_nodes_from([
    'A',"B","C","D"], bipartite=0)

G.add_nodes_from([1,2,3],
    bipartite=1)

G.add_edges_from([
    ('A',1),('A',2),('A',3),('B',2),('B',3),('C',1),('C',3),('D',2),('D',3),
    
])
X,Y=bipartite.sets(G)

G1=bipartite.projected_graph(G,X)
G2=bipartite.projected_graph(G,Y)


# for  i in zip(range(1,4),[G,G1,G2]):
#     plt.subplot(3,1,i[0])
#     nx.draw_networkx(i[1])
nx.draw_networkx(G)
plt.show()

