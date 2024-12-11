from rdflib import Graph

# Load RDF data
g = Graph()
g.parse("extracted_file.rdf",format="xml")

# Explore triples
for subj, pred, obj in g:
    print(f"Subject: {subj}, Predicate: {pred}, Object: {obj}")
