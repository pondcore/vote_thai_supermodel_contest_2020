import requests, time
from numpy import random

t=0
vote = 0
vote_num = 5
url = 'https://gz9ofg2pnc.execute-api.ap-southeast-1.amazonaws.com/Prod/api/items/TSM20200304/vote'
payload0 = {'iid': vote_num, 'uid': 'c6d7f831-71a1-46e6-9e64-2ed8665f0dc5', 'react': 'vote'}
payload1 = {'iid': vote_num, 'uid': '10fb5ac9-3dcc-4b19-b8bf-e5df4548492c', 'react': 'vote'}
payload2 = {'iid': vote_num, 'uid': '83f1cdf4-05bb-4468-bb42-060649446f1a', 'react': 'vote'}
payload3 = {'iid': vote_num, 'uid': '0cf024b4-96a5-41a5-8e14-9dee92279864', 'react': 'vote'}
payload4 = {'iid': vote_num, 'uid': '7866a8bd-a91f-41c4-81e6-200d9b04b164', 'react': 'vote'}
payload5 = {'iid': vote_num, 'uid': 'e0fc5480-a1e5-4ea5-a59d-6a3d8be8d499', 'react': 'vote'}
payload6 = {'iid': vote_num, 'uid': 'c0ce087b-f903-4c55-bcb6-63b071f1fbc1', 'react': 'vote'}
payload7 = {'iid': vote_num, 'uid': '8071e29e-2b28-4c90-abec-089a6b3636ac', 'react': 'vote'}
payload8 = {'iid': vote_num, 'uid': 'ac942a4a-d2c9-4abb-b9d0-db353309b473', 'react': 'vote'}
payload9 = {'iid': vote_num, 'uid': 'ae043892-8d2f-42ca-83c1-843445106f40', 'react': 'vote'}
payload10 = {'iid': vote_num, 'uid': 'ac74f81e-cdf0-458e-a809-29370000b85a', 'react': 'vote'}
payload11 = {'iid': vote_num, 'uid': 'f5447d0c-edcb-4995-889d-8573a2d436ad', 'react': 'vote'}
payload12 = {'iid': vote_num, 'uid': '30fb5fac-0583-41e3-bd40-5e6f896c8d38', 'react': 'vote'}
payload13 = {'iid': vote_num, 'uid': '1618cc85-3201-41a5-984a-72f73f131245', 'react': 'vote'}
payload14 = {'iid': vote_num, 'uid': 'adcd22bd-8d63-4b78-8bce-db2a4d0a4dab', 'react': 'vote'}
payload15 = {'iid': vote_num, 'uid': 'c7aa764b-41ba-4b5e-8096-6639be366179', 'react': 'vote'}
payload16 = {'iid': vote_num, 'uid': 'ffccf3bc-666d-4a35-9b38-2b773a688c4a', 'react': 'vote'}
payload17 = {'iid': vote_num, 'uid': '23d309d7-8442-480a-b41f-45071f813b20', 'react': 'vote'}
payload18 = {'iid': vote_num, 'uid': '95107163-abb5-4174-ad79-d6aaa65195fd', 'react': 'vote'}
payload19 = {'iid': vote_num, 'uid': '1ac883f5-ac1c-4c2f-9955-c94237c6d212', 'react': 'vote'}
payload20 = {'iid': vote_num, 'uid': '5f24e1da-d4c3-4989-9316-5fd5441145d2', 'react': 'vote'}
payload21 = {'iid': vote_num, 'uid': 'b5450d6c-e2f4-4bbe-a29a-c0c0f40acfd6', 'react': 'vote'}
payload22 = {'iid': vote_num, 'uid': '37b554cf-355f-44b0-8a29-56e0565e03e3', 'react': 'vote'}
payload23 = {'iid': vote_num, 'uid': '2937d933-4aa2-4083-a0e9-32b238f2f9b1', 'react': 'vote'}
payload24 = {'iid': vote_num, 'uid': '7cd9c536-339e-4f52-ab99-37908d3a1a2f', 'react': 'vote'}
payload25 = {'iid': vote_num, 'uid': 'fe05958c-6961-4187-8b38-81875fdff74b', 'react': 'vote'}
payload26 = {'iid': vote_num, 'uid': 'e968ba51-933b-4b9b-b75a-9898e7d13f63', 'react': 'vote'}
payload27 = {'iid': vote_num, 'uid': '0445addb-3d21-42e7-9188-cc6e25ced04d', 'react': 'vote'}
payload28 = {'iid': vote_num, 'uid': '65eb81e6-6eac-4009-8c56-4a240eee90e4', 'react': 'vote'}
payload29 = {'iid': vote_num, 'uid': '5ef985e2-9233-41f8-bdfa-7e691a079b8a', 'react': 'vote'}
payload30 = {'iid': vote_num, 'uid': '5e8aee2e-8023-44c6-bdd0-6a92a3a328e3', 'react': 'vote'}
payload31 = {'iid': vote_num, 'uid': '73d88f02-f972-429b-983c-42d2ae91ffde', 'react': 'vote'}
payload32 = {'iid': vote_num, 'uid': '09262e39-4a4c-491a-8980-3d00b82f9523', 'react': 'vote'}
payload33 = {'iid': vote_num, 'uid': '9561bec0-d626-4c13-8d8b-7506411e0e37', 'react': 'vote'}
payload34 = {'iid': vote_num, 'uid': 'a5e1d8e1-a326-46d4-afc7-52cb25bbfc44', 'react': 'vote'}
payload35 = {'iid': vote_num, 'uid': '48d0961d-e74d-41d0-9eab-c1fd2b24c43d', 'react': 'vote'}
payload36 = {'iid': vote_num, 'uid': 'c3f64b93-bc05-4358-9d8f-9d054a03b1a5', 'react': 'vote'}
payload37 = {'iid': vote_num, 'uid': '41cea5a1-ab73-477b-8079-6a33e4c2614e', 'react': 'vote'}
payload38 = {'iid': vote_num, 'uid': '4988ca0c-252f-4c7b-a5f2-b20aaab5de05', 'react': 'vote'}
payload39 = {'iid': vote_num, 'uid': '8d1af531-36e5-4f04-9416-175a5bdddfe2', 'react': 'vote'}
r0 = requests.post(url, data=payload0)
r1 = requests.post(url, data=payload1)
r2 = requests.post(url, data=payload2)
r3 = requests.post(url, data=payload3)
r4 = requests.post(url, data=payload4)
r5 = requests.post(url, data=payload5)
r6 = requests.post(url, data=payload6)
r7 = requests.post(url, data=payload7)
r8 = requests.post(url, data=payload8)
r9 = requests.post(url, data=payload9)
r10 = requests.post(url, data=payload10)
r11 = requests.post(url, data=payload11)
r12 = requests.post(url, data=payload12)
r13 = requests.post(url, data=payload13)
r14 = requests.post(url, data=payload14)
r15 = requests.post(url, data=payload15)
r16 = requests.post(url, data=payload16)
r17 = requests.post(url, data=payload17)
r18 = requests.post(url, data=payload18)
r19 = requests.post(url, data=payload19)
r20 = requests.post(url, data=payload20)
r21 = requests.post(url, data=payload21)
r22 = requests.post(url, data=payload22)
r23 = requests.post(url, data=payload23)
r24 = requests.post(url, data=payload24)
r25 = requests.post(url, data=payload25)
r26 = requests.post(url, data=payload26)
r27 = requests.post(url, data=payload27)
r28 = requests.post(url, data=payload28)
r29 = requests.post(url, data=payload29)
r30 = requests.post(url, data=payload30)
r31 = requests.post(url, data=payload31)
r32 = requests.post(url, data=payload32)
r33 = requests.post(url, data=payload33)
r34 = requests.post(url, data=payload34)
r35 = requests.post(url, data=payload35)
r36 = requests.post(url, data=payload36)
r37 = requests.post(url, data=payload37)
r38 = requests.post(url, data=payload38)
r39 = requests.post(url, data=payload39)
print(r0.json()['list'])
print(r1.json()['list'])
print(r2.json()['list'])
print(r3.json()['list'])
print(r4.json()['list'])
print(r5.json()['list'])
print(r6.json()['list'])
print(r7.json()['list'])
print(r8.json()['list'])
print(r9.json()['list'])
print(r10.json()['list'])
print(r11.json()['list'])
print(r12.json()['list'])
print(r13.json()['list'])
print(r14.json()['list'])
print(r15.json()['list'])
print(r16.json()['list'])
print(r17.json()['list'])
print(r18.json()['list'])
print(r19.json()['list'])
print(r20.json()['list'])
print(r21.json()['list'])
print(r22.json()['list'])
print(r23.json()['list'])
print(r24.json()['list'])
print(r25.json()['list'])
print(r26.json()['list'])
print(r27.json()['list'])
print(r28.json()['list'])
print(r29.json()['list'])
print(r30.json()['list'])
print(r31.json()['list'])
print(r32.json()['list'])
print(r33.json()['list'])
print(r34.json()['list'])
print(r35.json()['list'])
print(r36.json()['list'])
print(r37.json()['list'])
print(r38.json()['list'])
print(r39.json()['list'])
while(True):
    t+=1
    time.sleep(1)
    if time.time()*1000 > int(r0.json()['list']['nextVoteTime']) :
        time.sleep(1)
        r0 = requests.post(url, data=payload0)
        vote += 1
        print(r0.json()['list'])
    if time.time()*1000 > int(r1.json()['list']['nextVoteTime']) :
        time.sleep(1)
        r1 = requests.post(url, data=payload1)
        vote += 1
        print(r1.json()['list'])
    if time.time()*1000 > int(r2.json()['list']['nextVoteTime']) :
        time.sleep(1)
        r2 = requests.post(url, data=payload2)
        vote += 1
        print(r2.json()['list'])
    if time.time()*1000 > int(r3.json()['list']['nextVoteTime']) :
        time.sleep(1)
        r3 = requests.post(url, data=payload3)
        vote += 1
        print(r3.json()['list'])
    if time.time()*1000 > int(r4.json()['list']['nextVoteTime']) :
        time.sleep(1)
        r4 = requests.post(url, data=payload4)
        vote += 1
        print(r4.json()['list'])
    if time.time()*1000 > int(r5.json()['list']['nextVoteTime']) :
        time.sleep(1)
        r5 = requests.post(url, data=payload5)
        vote += 1
        print(r5.json()['list'])
    if time.time()*1000 > int(r6.json()['list']['nextVoteTime']) :
        time.sleep(1)
        r6 = requests.post(url, data=payload6)
        vote += 1
        print(r6.json()['list'])
    if time.time()*1000 > int(r7.json()['list']['nextVoteTime']) :
        time.sleep(1)
        r7 = requests.post(url, data=payload7)
        vote += 1
        print(r7.json()['list'])
    if time.time()*1000 > int(r8.json()['list']['nextVoteTime']) :
        time.sleep(1)
        r8 = requests.post(url, data=payload8)
        vote += 1
        print(r8.json()['list'])
    if time.time()*1000 > int(r9.json()['list']['nextVoteTime']) :
        time.sleep(1)
        r9 = requests.post(url, data=payload9)
        vote += 1
        print(r9.json()['list'])
    if time.time()*1000 > int(r10.json()['list']['nextVoteTime']) :
        time.sleep(1)
        r10 = requests.post(url, data=payload10)
        vote += 1
        print(r10.json()['list'])
    if time.time()*1000 > int(r11.json()['list']['nextVoteTime']) :
        time.sleep(1)
        r11 = requests.post(url, data=payload11)
        vote += 1
        print(r11.json()['list'])
    if time.time()*1000 > int(r12.json()['list']['nextVoteTime']) :
        time.sleep(1)
        r12 = requests.post(url, data=payload12)
        vote += 1
        print(r12.json()['list'])
    if time.time()*1000 > int(r13.json()['list']['nextVoteTime']) :
        time.sleep(1)
        r13 = requests.post(url, data=payload13)
        vote += 1
        print(r13.json()['list'])
    if time.time()*1000 > int(r14.json()['list']['nextVoteTime']) :
        time.sleep(1)
        r14 = requests.post(url, data=payload14)
        vote += 1
        print(r14.json()['list'])
    if time.time()*1000 > int(r15.json()['list']['nextVoteTime']) :
        time.sleep(1)
        r15 = requests.post(url, data=payload15)
        vote += 1
        print(r15.json()['list'])
    if time.time()*1000 > int(r16.json()['list']['nextVoteTime']) :
        time.sleep(1)
        r16 = requests.post(url, data=payload16)
        vote += 1
        print(r16.json()['list'])
    if time.time()*1000 > int(r17.json()['list']['nextVoteTime']) :
        time.sleep(1)
        r17 = requests.post(url, data=payload17)
        vote += 1
        print(r17.json()['list'])
    if time.time()*1000 > int(r18.json()['list']['nextVoteTime']) :
        time.sleep(1)
        r18 = requests.post(url, data=payload18)
        vote += 1
        print(r18.json()['list'])
    if time.time()*1000 > int(r19.json()['list']['nextVoteTime']) :
        time.sleep(1)
        r19 = requests.post(url, data=payload19)
        vote += 1
        print(r19.json()['list'])
    if time.time()*1000 > int(r20.json()['list']['nextVoteTime']) :
        time.sleep(1)
        r20 = requests.post(url, data=payload20)
        vote += 1
        print(r20.json()['list'])
    if time.time()*1000 > int(r21.json()['list']['nextVoteTime']) :
        time.sleep(1)
        r21 = requests.post(url, data=payload21)
        vote += 1
        print(r21.json()['list'])
    if time.time()*1000 > int(r22.json()['list']['nextVoteTime']) :
        time.sleep(1)
        r22 = requests.post(url, data=payload22)
        vote += 1
        print(r22.json()['list'])
    if time.time()*1000 > int(r23.json()['list']['nextVoteTime']) :
        time.sleep(1)
        r23 = requests.post(url, data=payload23)
        vote += 1
        print(r23.json()['list'])
    if time.time()*1000 > int(r24.json()['list']['nextVoteTime']) :
        time.sleep(1)
        r24 = requests.post(url, data=payload24)
        vote += 1
        print(r24.json()['list'])
    if time.time()*1000 > int(r25.json()['list']['nextVoteTime']) :
        time.sleep(1)
        r25 = requests.post(url, data=payload25)
        vote += 1
        print(r25.json()['list'])
    if time.time()*1000 > int(r26.json()['list']['nextVoteTime']) :
        time.sleep(1)
        r26 = requests.post(url, data=payload26)
        vote += 1
        print(r26.json()['list'])
    if time.time()*1000 > int(r27.json()['list']['nextVoteTime']) :
        time.sleep(1)
        r27 = requests.post(url, data=payload27)
        vote += 1
        print(r27.json()['list'])
    if time.time()*1000 > int(r28.json()['list']['nextVoteTime']) :
        time.sleep(1)
        r28 = requests.post(url, data=payload28)
        vote += 1
        print(r28.json()['list'])
    if time.time()*1000 > int(r29.json()['list']['nextVoteTime']) :
        time.sleep(1)
        r29 = requests.post(url, data=payload29)
        vote += 1
        print(r29.json()['list'])
    if time.time()*1000 > int(r30.json()['list']['nextVoteTime']) :
        time.sleep(1)
        r30 = requests.post(url, data=payload30)
        vote += 1
        print(r30.json()['list'])
    if time.time()*1000 > int(r31.json()['list']['nextVoteTime']) :
        time.sleep(1)
        r31 = requests.post(url, data=payload31)
        vote += 1
        print(r31.json()['list'])
    if time.time()*1000 > int(r32.json()['list']['nextVoteTime']) :
        time.sleep(1)
        r32 = requests.post(url, data=payload32)
        vote += 1
        print(r32.json()['list'])
    if time.time()*1000 > int(r33.json()['list']['nextVoteTime']) :
        time.sleep(1)
        r33 = requests.post(url, data=payload33)
        vote += 1
        print(r33.json()['list'])
    if time.time()*1000 > int(r34.json()['list']['nextVoteTime']) :
        time.sleep(1)
        r34 = requests.post(url, data=payload34)
        vote += 1
        print(r34.json()['list'])
    if time.time()*1000 > int(r35.json()['list']['nextVoteTime']) :
        time.sleep(1)
        r35 = requests.post(url, data=payload35)
        vote += 1
        print(r35.json()['list'])
    if time.time()*1000 > int(r36.json()['list']['nextVoteTime']) :
        time.sleep(1)
        r36 = requests.post(url, data=payload36)
        vote += 1
        print(r36.json()['list'])
    if time.time()*1000 > int(r37.json()['list']['nextVoteTime']) :
        time.sleep(1)
        r37 = requests.post(url, data=payload37)
        vote += 1
        print(r37.json()['list'])
    if time.time()*1000 > int(r38.json()['list']['nextVoteTime']) :
        time.sleep(1)
        r38 = requests.post(url, data=payload38)
        vote += 1
        print(r38.json()['list'])
    if time.time()*1000 > int(r39.json()['list']['nextVoteTime']) :
        time.sleep(1)
        r39 = requests.post(url, data=payload39)
        vote += 1
        print(r39.json()['list'])
    print(vote)
    if t%2 == 0 :
        print('/')
        if t == 10:
            t = 0
    else:
        print('\\')