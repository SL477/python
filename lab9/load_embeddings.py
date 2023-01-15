# Load back with memory-mapping = read-only, shared across processes.
from gensim.models import KeyedVectors
from sklearn.cluster import KMeans
# import matplotlib.pyplot as plt

wv = KeyedVectors.load("pizza.embeddings", mmap='r')


# vector = wv['pizza']  # Get numpy vector of a word
# print(dir(wv.wv))
vector = wv.wv.get_index('pizza')
print(vector)


#cosine similarity
similarity = wv.wv.similarity('pizza', 'http://www.co-ode.org/ontologies/pizza/pizza.owl#Pizza')
print(similarity)

similarity = wv.wv.similarity('http://www.co-ode.org/ontologies/pizza/pizza.owl#Margherita', 'margherita')
print(similarity)

# task 4.2
print("task 4.2")
similarity = wv.wv.similarity('http://www.co-ode.org/ontologies/pizza/pizza.owl#Hot', 'http://www.co-ode.org/ontologies/pizza/pizza.owl#Medium')
print('Hot & Medium', similarity)

similarity = wv.wv.similarity('CheesyPizza', 'CheeseTopping')
print('CheesyPizza & CheeseTopping', similarity)


# Most similar cosine similarity
result = wv.wv.most_similar(positive=['margherita', 'pizza'])
print(result)

# task 4.3
print('Task 4.3')
result = wv.wv.most_similar(positive=['Hot'])
print('Hot:', result)

#print('CheesyPizza:', wv.wv.most_similar(positive=['http://www.co-ode.org/ontologies/pizza/pizza.owl#CheesyPizza']))

print('Fiorentina:', wv.wv.most_similar(positive=['http://www.co-ode.org/ontologies/pizza/pizza.owl#Fiorentina']))

print('Soho:', wv.wv.most_similar(positive=['http://www.co-ode.org/ontologies/pizza/pizza.owl#Soho']))

# Most similar entities: cosmul
result = wv.wv.most_similar_cosmul(positive=['margherita'])
print(result)

# kmeans = KMeans()
# kmeans.fit(wv.wv.most_similar(positive=['http://www.co-ode.org/ontologies/pizza/pizza.owl#Soho']))
# plt.scatter(kmeans[:, 0], kmeans[:, 1], c=kmeans, cmap='viridis')
# plt.plot()