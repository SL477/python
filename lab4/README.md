# lab4

## Section 2

### 2.1

#### Statement 1, Father rdfs:subclassof :Person

Yes, line 12

#### Statement 2, :Woman rdfsLsubClassOf :Person

Yes, line 8

#### Statement 3, :Juliet a : Person

Yes, Juliet is referenced in line 33 as a hasMother attribute of Ann. A :Mother is a subClass of Person.

#### Statement 4, :Ann a :Child

No, or at least not explicitly set. Ann is a :Person & related by :isChildOf

#### Statement 5, :Ann :isChildOf :Carl

No, :Ann hasFather :Carl. But there is no property going back

#### Statement 6, :Ann :hasParent :Juliet

Yes, :Ann hasMother :Juliet and :hasMother is a subproperty of :hasParent

#### Statement 7, rdfs:range rdf:type rdfs:Resource

Yes

#### Statement 8, :Mother rdfs:subClassOf :Person

Yes, :Mother is a sub class of :Parent, which is a subclass of person
