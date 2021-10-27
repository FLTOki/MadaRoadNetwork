import networkx as nx
import matplotlib.pyplot as plt
from networkx.readwrite import edgelist
from classes.greedy_bfs import BfsTraverser

G = nx.Graph()
nodes = ["SportsComplex", "Siwaka", "Ph.1A", "Ph.1B", "STC", "Phase2", "J1", "Mada", "Phase3", "ParkingLot"]
G.add_nodes_from(nodes)
G.nodes()

G.add_edge("SportsComplex", "Siwaka", weight="0.45")
G.add_edge("Siwaka", "Ph.1A", weight="0.01")
G.add_edge("Siwaka", "Ph.1B", weight="0.23")
G.add_edge("Ph.1A", "Mada", weight="0.85")
G.add_edge("Ph.1B", "Phase2", weight="0.112")
G.add_edge("Ph.1B", "STC", weight="0.5")
G.add_edge("Phase2", "J1", weight="0.6")
G.add_edge("J1", "Mada", weight="0.20")
G.add_edge("Phase3", "ParkingLot", weight="0.35")
G.add_edge("Phase2", "Phase3", weight="0.50")
G.add_edge("STC", "ParkingLot", weight="0.250")
G.add_edge("ParkingLot", "Mada", weight="0.70")
G.add_edge("Phase2", "STC", weight="0.05")
G.add_edge("Ph.1A", "Ph.1B", weight="0.10")

G.nodes["STC"]['pos'] = (0,0)
G.nodes["Ph.1B"]['pos'] = (0,2)
G.nodes["Ph.1A"]['pos'] = (0,4)
G.nodes["Siwaka"]['pos'] = (-2,4)
G.nodes["SportsComplex"]['pos'] = (-4,4)
G.nodes["Phase2"]['pos'] = (2,2)
G.nodes["J1"]['pos'] = (4,2)
G.nodes["Mada"]['pos'] = (6,2)
G.nodes["Phase3"]['pos'] = (4,0)
G.nodes["ParkingLot"]['pos'] = (4,-2)

node_pos = nx.get_node_attributes(G, 'pos')
route_greedy_bfs = BfsTraverser()
routes = route_greedy_bfs.BFS(G, "SportsComplex", "ParkingLot")

print(route_greedy_bfs.visited)
route_list = route_greedy_bfs.visited

node_color = ['#AEEA00' if not node in route_list else '#6200EA' for node in G.nodes()]
purple_colored_edges = list(zip(route_list, route_list[1:]))

edge_color = ['#AEEA00' if not edge in purple_colored_edges else '#6200EA' for edge in G.edges()]
arc_weight = nx.get_edge_attributes(G, 'weigth')
nx.draw_networkx(G, node_pos, node_color = node_color, node_size = 450)
nx.draw_networkx_edges(G, node_pos, width=2, edge_color=edge_color)

nx.draw_networkx_edge_labels(G, node_pos, edge_labels=arc_weight)
plt.axis('off')
plt.show()
