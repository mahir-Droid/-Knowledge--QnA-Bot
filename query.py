import networkx as nx

# Initialize graph
G = nx.DiGraph()

# Add triples to the graph
triples = [
    ("Douglas Adams", "author_of", "The Hitchhiker's Guide to the Galaxy"),
    ("The Hitchhiker's Guide to the Galaxy", "published_in", "1979")
]
for subj, pred, obj in triples:
    G.add_edge(subj, obj, relation=pred)

# Query the graph
def query_graph(graph, entity):
    return [(nbr, graph[entity][nbr]['relation']) for nbr in graph.neighbors(entity)]

print(query_graph(G, "Mostafa Mushsharat"))
