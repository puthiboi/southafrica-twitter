from pyvis.network import Network
import pandas as pd

FILTER = 32         #not recommended to go under 8
TYPE = 'barnes_hut' #set to 'repulsion' to change
SHOW_EDGES = True   #set to False to turn of edges (only recommended with 'repulsion' method)  

"""
    visualization.py is used for the Network Graph Visualization of the collected data. 
    It reads the data, filters the data to only include accounts with the minimum amount of connections set by 'FILTER'
    Change 'FILTER' and 'TYPE' to change network size and method.
"""

#### Initiates the network

net = Network(height='100%', width='100%', bgcolor='#222222', font_color='white')


#### Sets the physics layout of the network

if TYPE == 'barnes_hut':
    net.barnes_hut()
else:
    net.repulsion(node_distance=400, spring_length=400)


def filter_by_freq(df: pd.DataFrame, column: str, min_freq: int) -> pd.DataFrame:
    """Filters the DataFrame based on the value frequency in the specified column.

    :param df: DataFrame to be filtered.
    :param column: Column name that should be frequency filtered.
    :param min_freq: Minimal value frequency for the row to be accepted.
    :return: Frequency filtered DataFrame.
    """
    # Frequencies of each value in the column.
    freq = df[column].value_counts()
    # Select frequent values. Value is in the index.
    frequent_values = freq[freq >= min_freq].index
    # Return only rows with value frequency above threshold.
    return df[df[column].isin(frequent_values)]


#### Read and prepare the data

data = pd.read_csv('network_data.csv')
data = filter_by_freq(data,'screen_name', FILTER)

sources = data['screen_name']
targets = data['Target']
weights = data['Weight']

edge_data = zip(sources, targets, weights)


#### Prepare the network

l = []
for e in edge_data:
    src = e[0]
    dst = e[1]
    w = 0.1

    net.add_node(src, src, title=src)
    l.append(src)
    net.add_node(dst, dst, title=dst, hidden=True)
      
    if SHOW_EDGES is True:
        if dst in l:
            net.add_edge(src, dst)
    else:
        net.add_edge(src, dst, hidden=True)
    
neighbor_map = net.get_adj_list()

for node in net.nodes:
    node['title'] += ' Neighbors:<br>' + '<br>'.join(neighbor_map[node['id']])
    node['value'] = len(neighbor_map[node['id']])*10

#### Export to html

net.show_buttons()
net.show('data10_experimental.html')
