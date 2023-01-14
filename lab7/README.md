# Lab 7

## Task 2

Import into GraphDB Free.

### 2.1

#### Statement 1

>:Juliet :hasChild :Ann .

Ann hasMother Juliet, hasMother is a sub-property of hasParent and hasChild is the inverse of hasParent. So by that logic this statement is correct.

```SPARQL
PREFIX : <http://city.ac.uk/kg/lab7/>
select * where { 
    :Juliet :hasChild ?o .
} limit 100
```

One result

#### Statement 2

>:Ann a :Child .

There is not actually a property of child in the graph and we have no information on Ann's age. So she may be Juliet's child, but we do not know if she is actually a child.

```SPARQL
PREFIX : <http://city.ac.uk/kg/lab7/>
select * where { 
    :Ann a :Child .
} limit 100 
```

No results

## Task 3

### Task 3.1

Count cities in countries

```SPARQL
PREFIX lab6: <http://www.semanticweb.org/ernesto/inm713/lab6/>
PREFIX : <http://city.ac.uk/kg/lab7/>
SELECT DISTINCT ?country (COUNT(?city) as ?Number_City) WHERE { 
    ?country lab6:hasCity ?city .
} 
GROUP BY ?country
ORDER BY DESC(?Number_City)
```
