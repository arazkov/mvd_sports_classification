 
import json

with open('sport_data.json','r') as js:
    balls = json.load(js)

ind = balls['body'][0].index('pull_ups')

for i in balls['body']:
    if i[ind] == '15':
        print(i[0])
