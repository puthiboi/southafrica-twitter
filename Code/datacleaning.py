import pandas as pd

'''
    Used to add 'Target' Column for Network Visualization
'''

df = pd.read_csv("friendlist_target.csv")
count_row = df.shape[0]

weight = []
for user in range(count_row):
    weight.append(1)

df['Weight'] = weight
df.to_csv ('friendlist_target_weight.csv', index = False, header=True)
