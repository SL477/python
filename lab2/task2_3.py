# from loadAndSaveGraph import loadTriplesAndSaveToTargetFormat

# loadTriplesAndSaveToTargetFormat("ernesto_foaf.rdf", "rdf/xml", "rdf/turtle")

from rdflib import Graph
def loadTriplesAndSave():

    #Example from  https://www.stardog.com/tutorials/data-model/
   
    g = Graph()
    g.parse("ernesto_foaf.rdf", format="xml")
    #g.parse("http://link477.com/foaf.rdf", format="xml")
    
    
    print("The graph contains '" + str(len(g)) + "' triples.")
    
    
        
    for s, p, o in g:
        print((s.n3(), p.n3(), o.n3()))
    
    print("Saving graph to 'ernesto_foaf.ttl'")
    g.serialize(destination='ernesto_foaf.ttl', format='ttl')

if '__main__' == __name__:
    loadTriplesAndSave()