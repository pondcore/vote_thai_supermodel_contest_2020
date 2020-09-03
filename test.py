import requests, time
from numpy import random

t=0
vote = 0
vote_num = 5
url = 'https://gz9ofg2pnc.execute-api.ap-southeast-1.amazonaws.com/Prod/api/items/TSM20200304/vote'
payload0 = {'iid': vote_num, 'uid': 'c6d7f831-71a1-46e6-9e64-2ed8665f0dc5', 'react': 'vote'}
r0 = requests.post(url, data=payload0)

while(True):
    t+=1
    time.sleep(1)
    if time.time()*1000 > int(r0.json()['list']['nextVoteTime']) :
        time.sleep(1)
        r0 = requests.post(url, data=payload0)
        vote += 1
        print(r0.json()['list'])

    print(time.time()*1000)
    print(int(r0.json()['list']['nextVoteTime']))
    print(vote)
    if t%2 == 0 :
        print('/')
        if t == 10:
            t = 0
    else:
        print('\\')