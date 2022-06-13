import py4cytoscape as p4c
import pandas as pd

# Import the class
import kmapper as km

# Some sample data
from py4cytoscape import create_network_from_data_frames
from sklearn import datasets

from ConvertingToDataFrame import df

data, labels = datasets.make_circles(n_samples=5000, noise=0.03, factor=0.3)

# Initialize
mapper = km.KeplerMapper(verbose=1)

# Fit to and transform the data
projected_data = mapper.fit_transform(data, projection=[0, 1])  # X-Y axis

# Create a cover with 10 elements
cover = km.Cover(n_cubes=10)

# Create dictionary called 'graph' with nodes, edges and meta-information
graph = mapper.map(projected_data, data, cover=cover)
k = list(graph['links'].items())
v = list(graph['nodes'].items())

source = []
target=[]
node_id=[]
node_members=[]
node_count=[]


for i in v:
    node_id.append(i[0])
    node_count.append(len(i[1]))
    node_members.append(i[1])

for i in k:
    n = len(i[1])
    for j in range(n):
        source.append(i[0])
        target.append(i[1][j])

#print(v)
#print(source)
#print(target)
#print(node_count)
#print(node_id)
#print(node_members)

node_data = {'id': node_id,
             'members': node_members,
             'membercount':node_count}
nodes = pd.DataFrame(data=node_data, columns=['id', 'members', 'membercount'])
edge_data = {'source':source,
             'target':target,
             }
edges = pd.DataFrame(data=edge_data, columns=['source', 'target'])

create_network_from_data_frames(nodes, edges, title='From node & edge dataframe')

