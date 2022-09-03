import sys
import tweepy
import csv
import pandas as pd
import json

MAX_COUNT = 250

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


df = pd.read_csv("friendlist.csv")
screen_name_list = df['screen_name'].tolist()
follower_count = df['friends_count'].tolist()

result = zip(screen_name_list, follower_count)


def tweep(screen_name, max_count):
    friends_list = []
    for friend in tweepy.Cursor(api.get_friends, screen_name=screen_name).items(max_count):
        friends_list.append(friend)
    
    my_list_of_dicts = []
    for each_json in friends_list:
        my_list_of_dicts.append(each_json._json)
    
    print(" MY LIST OF DICTS")
    print(len(my_list_of_dicts)) 


    with open('friends_list.txt', 'w') as file:
            file.write(json.dumps(my_list_of_dicts, indent=4))

    my_demo_list = []
    
    with open('friends_list.txt', encoding='utf-8') as json_file:  
        all_data = json.load(json_file)
        for each_dictionary in all_data:
            friend_id = each_dictionary['id_str']
            name = each_dictionary['name']
            screen_namee = each_dictionary['screen_name']
            location = each_dictionary['location']
            description = each_dictionary['description']
            friends_count = each_dictionary['friends_count']
            my_demo_list.append({'friend_id': str(friend_id),
                                'name': str(name),
                                'screen_name': str(screen_namee),
                                'location': str(location),
                                'description': str(description),
                                'friends_count': int(friends_count)
                                })
            user_json = pd.DataFrame(my_demo_list, columns = 
                                    ['friend_id', 'name', 
                                    'screen_name', 'location', 
                                    'description', 'friends_count'])
       
        user_json['Target'] = screen_name
        user_json['Weight'] = 1
        print(" USER JSON")
        print(user_json.shape)
        csv_name = screen_name + '.csv'
        user_json.to_csv (csv_name, index = False, header=True)
    
    return user_json


for x in result:
    if x[1] == 0:
        continue
    else:
        user_json = tweep(x[0], MAX_COUNT)
        user_json.to_csv (x[0] + '.csv', index = False, header=True)         
        df = pd.concat([df, user_json], ignore_index = True, axis = 0)

df.to_csv ('final.csv', index = False, header=True)