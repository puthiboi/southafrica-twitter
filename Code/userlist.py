from pydoc import describe
import sys
import tweepy
import csv
import pandas as pd
import time
import json

try:
    from credentials import consumer_key, consumer_secret, access_token, access_token_secret
except ModuleNotFoundError:
    sys.exit('credentials.py does not exist in src/ folder. '
             'See README.md for instructions.')
except ImportError as import_error:
    sys.exit(f'{import_error}\nCheck for spelling.')

# use those defined keys to login to twitter using tweepy
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

# get the usernames of all user followed by VFPlus and add them to a csv

friends_list = []
for friend in tweepy.Cursor(api.get_friends, screen_name="VFPlus").items():
    friends_list.append(friend)


my_list_of_dicts = []
for each_json in friends_list:
    my_list_of_dicts.append(each_json._json)

with open('friends_list.txt', 'w') as file:
        file.write(json.dumps(my_list_of_dicts, indent=4))

my_demo_list = []
with open('friends_list.txt', encoding='utf-8') as json_file:  
    all_data = json.load(json_file)
    for each_dictionary in all_data:
        friend_id = each_dictionary['id_str']
        name = each_dictionary['name']
        screen_name = each_dictionary['screen_name']
        location = each_dictionary['location']
        description = each_dictionary['description']
        friends_count = each_dictionary['friends_count']
        my_demo_list.append({'friend_id': str(friend_id),
                             'name': str(name),
                             'screen_name': str(screen_name),
                             'location': str(location),
                             'description': str(description),
                             'friends_count': int(friends_count)
                            })
        #print(my_demo_list)
        user_json = pd.DataFrame(my_demo_list, columns = 
                                  ['friend_id', 'name', 
                                   'screen_name', 'location', 
                                   'description', 'friends_count'])

count_row = user_json.shape[0]
weight = []
target = []
for user in range(count_row):
    weight.append(1)
    target.append("VFPlus")
user_json['Target'] = target
user_json['Weight'] = weight

user_json.to_csv ('friendlist.csv', index = False, header=True)



'''
friend.id_str
friend.name
friend.screen_name
friend.location
friend.description
'''

