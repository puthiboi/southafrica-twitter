from pyvis.network import Network
import pandas as pd

net = Network(height='100%', width='100%', bgcolor='#222222', font_color='white')

# set the physics layout of the network
net.barnes_hut()
#net.repulsion(node_distance=400, spring_length=400)
data = pd.read_csv('bigfileSA.csv')

def add_value(df: pd.DataFrame, column: str, value: int) -> pd.DataFrame:
    """Adds a value to the specified column in the DataFrame.

    :param df: DataFrame to be filtered.
    :param column: Column name that should be frequency filtered.
    :param value: Value to be added to the column.
    :return: DataFrame with added value.
    """
    df[column] = df[column] + value
    return df

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

data = filter_by_freq(data,'screen_name', 32)



sources = data['screen_name']
targets = data['Target']
weights = data['Weight']

edge_data = zip(sources, targets, weights)
l = []
for e in edge_data:
    src = e[0]
    #print(src)
    dst = e[1]
    #print(dst)
    w = 0.1
    #print(w)

    net.add_node(src, src, title=src)
    l.append(src)
    net.add_node(dst, dst, title=dst, hidden=True)
    #net.add_edge(src, dst, hidden=True)
    if dst in l:
        net.add_edge(src, dst)
    #net.add_edge(src, dst)
    


neighbor_map = net.get_adj_list()

# add neighbor data to node hover data
for node in net.nodes:
    node['title'] += ' Neighbors:<br>' + '<br>'.join(neighbor_map[node['id']])
    node['value'] = len(neighbor_map[node['id']])*10


#net.show_buttons(filter_=['physics'])
net.show_buttons()

net.show('data10_experimental.html')

'''
    Long und Lat verwenden für Location Map
'''

