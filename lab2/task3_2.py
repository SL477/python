from rdflib import Graph

g = Graph()
g.parse("tom.ttl", format="ttl")

print("The graph contains '" + str(len(g)) + "' triples.")

for s, p, o in g:
        print((s.n3(), p.n3(), o.n3()))