'''
Created on 02 Feb 2021

@author: ejimenez-ruiz
'''
from rdflib import Graph

def queryLocalGraph(qry: str):

    #Example from  https://www.stardog.com/tutorials/data-model/
   
    g = Graph()
    g.parse("playground.ttl", format="ttl")
  
    
    
    print("Loaded '" + str(len(g)) + "' triples.")
    
    #for s, p, o in g:
    #    print((s.n3(), p.n3(), o.n3()))
    
        
    #print("Females:")
    
    #qres = g.query(
    #"""SELECT ?thing ?name where {
    #  ?thing tto:sex "female" .
    #  ?thing dbp:name ?name .
    #}""")
    qres = g.query(qry)

    #for row in qres:
    #    #Row is a list of matched RDF terms: URIs, literals or blank nodes
    #    #print("%s is female with name '%s'" % (str(row.thing),str(row.name)))
    #    print(row)
    return qres
        
if __name__ == "__main__":
  #qry = """SELECT ?thing ?name where {
  #    ?thing tto:sex "female" .
  #    ?name dbp:name "Eve" .
  #}
  #"""
  qry = """select ?grandfather where {
	ttr:Eve dbo:parent / dbo:parent ?grandfather  .
}
  """
  res = queryLocalGraph(qry)
  for row in res:
    print(row)

  print("---dogs---")
  #qry = """select * where {
  #?a rdf:type tto:Dog .
  #}"""
  qry = """SELECT * where {
      ?a rdf:type tto:Dog .
      ?a tto:color ?color .
      ?a tto:weight ?weight .
      ?a tto:sex ?sex .
  }"""
  res = queryLocalGraph(qry)
  for row in res:
    print(row)

  print("---pets with owners ---")
  qry = """select ?pname ?pet  where {
    ?person rdf:type dbo:Person .
    ?person dbp:name ?pname
    {?person tto:pet ?pet}
  }"""#?person tto:pet [?pet] .
  res = queryLocalGraph(qry)
  for row in res:
    print(row)

  print("---pets with owners, given---")
  qry = """select ?pet ?owner  where {
    ?pet a [rdfs:subClassOf tto:Animal].
    OPTIONAL {?owner tto:pet ?pet}
  }"""
  res = queryLocalGraph(qry)
  for row in res:
    print(row)

  print("---People with gender and birth date")
  qry = """SELECT ?name ?sex ?bd where {
    ?person rdf:type dbo:Person .
    ?person dbp:name ?name .
    ?person tto:sex ?sex .
    ?person dbp:birthDate ?bd .
  }
  ORDER BY ?sex ASC(?bd)"""
  res = queryLocalGraph(qry)
  for row in res:
    print(row)