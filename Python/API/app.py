import requests

def get_function(endpoint, name):

    baseurl = 'https://eldenring.fanapis.com/api/'

    # Make the GET request
    r = requests.get(baseurl + endpoint.lower())

    data = r.json()

    # Remove the 'info' object if it exists
    if 'info' in data:
        del data['info']

    #Look for the infromation inside "data"
    lookIn = data['data']

    for i in range(len(lookIn)):
        if lookIn[i]['name'] == name:
            found_data = lookIn[i]
            del found_data['image']
            print(found_data)
            break

get_function('bosses', "Ancestor Spirit")