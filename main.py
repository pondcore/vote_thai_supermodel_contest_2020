import requests, time
from numpy import random

t=0
vote = 0
vote_num = 5
e0fc5480-a1e5-4ea5-a59d-6a3d8be8d499
url = 'https://gz9ofg2pnc.execute-api.ap-southeast-1.amazonaws.com/Prod/api/items/TSM20200304/vote'
payload0 = {'iid': vote_num, 'uid': 'c6d7f831-71a1-46e6-9e64-2ed8665f0dc5', 'react': 'vote'}
payload1 = {'iid': vote_num, 'uid': '10fb5ac9-3dcc-4b19-b8bf-e5df4548492c', 'react': 'vote'}
payload2 = {'iid': vote_num, 'uid': '83f1cdf4-05bb-4468-bb42-060649446f1a', 'react': 'vote'}
payload3 = {'iid': vote_num, 'uid': '0cf024b4-96a5-41a5-8e14-9dee92279864', 'react': 'vote'}
payload4 = {'iid': vote_num, 'uid': '7866a8bd-a91f-41c4-81e6-200d9b04b164', 'react': 'vote'}
payload5 = {'iid': vote_num, 'uid': 'e0fc5480-a1e5-4ea5-a59d-6a3d8be8d499', 'react': 'vote'}
r0 = requests.post(url, data=payload0)
r1 = requests.post(url, data=payload1)
r2 = requests.post(url, data=payload2)
r3 = requests.post(url, data=payload3)
r4 = requests.post(url, data=payload4)
r5 = requests.post(url, data=payload5)
print(r0.json()['list'])
print(r1.json()['list'])
print(r2.json()['list'])
print(r3.json()['list'])
print(r4.json()['list'])
print(r5.json()['list'])
while(True):
    t+=1
    time.sleep(1)
    if time.time()*1000 > int(r0.json()['list']['nextVoteTime']) :
        time.sleep(random.randint(3))
        r0 = requests.post(url, data=payload0)
        vote += 1
        print(r0.json()['list'])
    if time.time()*1000 > int(r1.json()['list']['nextVoteTime']) :
        time.sleep(random.randint(3))
        r1 = requests.post(url, data=payload1)
        vote += 1
        print(r1.json()['list'])
    if time.time()*1000 > int(r2.json()['list']['nextVoteTime']) :
        time.sleep(random.randint(3))
        r2 = requests.post(url, data=payload2)
        vote += 1
        print(r2.json()['list'])
    if time.time()*1000 > int(r3.json()['list']['nextVoteTime']) :
        time.sleep(random.randint(3))
        r3 = requests.post(url, data=payload3)
        vote += 1
        print(r3.json()['list'])
    if time.time()*1000 > int(r4.json()['list']['nextVoteTime']) :
        time.sleep(random.randint(3))
        r4 = requests.post(url, data=payload4)
        vote += 1
        print(r4.json()['list'])
    if time.time()*1000 > int(r5.json()['list']['nextVoteTime']) :
        time.sleep(random.randint(3))
        r5 = requests.post(url, data=payload5)
        vote += 1
        print(r5.json()['list'])
    print(vote)
    if t%2 == 0 :
        print('/')
        if t == 10:
            t = 0
    else:
        print('\\')