import requests, time
from numpy import random

t=0
vote = 0
vote_num = 5
payload = []
r = []
url = 'https://gz9ofg2pnc.execute-api.ap-southeast-1.amazonaws.com/Prod/api/items/TSM20200304/vote'

payload.append({'iid': vote_num, 'uid': 'c6d7f831-71a1-46e6-9e64-2ed8665f0dc5', 'react': 'vote'})
payload.append({'iid': vote_num, 'uid': '10fb5ac9-3dcc-4b19-b8bf-e5df4548492c', 'react': 'vote'})
payload.append({'iid': vote_num, 'uid': '83f1cdf4-05bb-4468-bb42-060649446f1a', 'react': 'vote'})
payload.append({'iid': vote_num, 'uid': '0cf024b4-96a5-41a5-8e14-9dee92279864', 'react': 'vote'})
payload.append({'iid': vote_num, 'uid': '7866a8bd-a91f-41c4-81e6-200d9b04b164', 'react': 'vote'})
payload.append({'iid': vote_num, 'uid': 'e0fc5480-a1e5-4ea5-a59d-6a3d8be8d499', 'react': 'vote'})
payload.append({'iid': vote_num, 'uid': 'c0ce087b-f903-4c55-bcb6-63b071f1fbc1', 'react': 'vote'})
payload.append({'iid': vote_num, 'uid': '8071e29e-2b28-4c90-abec-089a6b3636ac', 'react': 'vote'})
payload.append({'iid': vote_num, 'uid': 'ac942a4a-d2c9-4abb-b9d0-db353309b473', 'react': 'vote'})
payload.append({'iid': vote_num, 'uid': 'ae043892-8d2f-42ca-83c1-843445106f40', 'react': 'vote'})
payload.append({'iid': vote_num, 'uid': 'ac74f81e-cdf0-458e-a809-29370000b85a', 'react': 'vote'})
payload.append({'iid': vote_num, 'uid': 'f5447d0c-edcb-4995-889d-8573a2d436ad', 'react': 'vote'})
payload.append({'iid': vote_num, 'uid': '30fb5fac-0583-41e3-bd40-5e6f896c8d38', 'react': 'vote'})
payload.append({'iid': vote_num, 'uid': '1618cc85-3201-41a5-984a-72f73f131245', 'react': 'vote'})
payload.append({'iid': vote_num, 'uid': 'adcd22bd-8d63-4b78-8bce-db2a4d0a4dab', 'react': 'vote'})
payload.append({'iid': vote_num, 'uid': 'c7aa764b-41ba-4b5e-8096-6639be366179', 'react': 'vote'})
payload.append({'iid': vote_num, 'uid': 'ffccf3bc-666d-4a35-9b38-2b773a688c4a', 'react': 'vote'})
payload.append({'iid': vote_num, 'uid': '23d309d7-8442-480a-b41f-45071f813b20', 'react': 'vote'})
payload.append({'iid': vote_num, 'uid': '95107163-abb5-4174-ad79-d6aaa65195fd', 'react': 'vote'})
payload.append({'iid': vote_num, 'uid': '1ac883f5-ac1c-4c2f-9955-c94237c6d212', 'react': 'vote'})
payload.append({'iid': vote_num, 'uid': '5f24e1da-d4c3-4989-9316-5fd5441145d2', 'react': 'vote'})
payload.append({'iid': vote_num, 'uid': 'b5450d6c-e2f4-4bbe-a29a-c0c0f40acfd6', 'react': 'vote'})
payload.append({'iid': vote_num, 'uid': '37b554cf-355f-44b0-8a29-56e0565e03e3', 'react': 'vote'})
payload.append({'iid': vote_num, 'uid': '2937d933-4aa2-4083-a0e9-32b238f2f9b1', 'react': 'vote'})
payload.append({'iid': vote_num, 'uid': '7cd9c536-339e-4f52-ab99-37908d3a1a2f', 'react': 'vote'})
payload.append({'iid': vote_num, 'uid': 'fe05958c-6961-4187-8b38-81875fdff74b', 'react': 'vote'})
payload.append({'iid': vote_num, 'uid': 'e968ba51-933b-4b9b-b75a-9898e7d13f63', 'react': 'vote'})
payload.append({'iid': vote_num, 'uid': '0445addb-3d21-42e7-9188-cc6e25ced04d', 'react': 'vote'})
payload.append({'iid': vote_num, 'uid': '65eb81e6-6eac-4009-8c56-4a240eee90e4', 'react': 'vote'})
payload.append({'iid': vote_num, 'uid': '5ef985e2-9233-41f8-bdfa-7e691a079b8a', 'react': 'vote'})
payload.append({'iid': vote_num, 'uid': '5e8aee2e-8023-44c6-bdd0-6a92a3a328e3', 'react': 'vote'})
payload.append({'iid': vote_num, 'uid': '73d88f02-f972-429b-983c-42d2ae91ffde', 'react': 'vote'})
payload.append({'iid': vote_num, 'uid': '09262e39-4a4c-491a-8980-3d00b82f9523', 'react': 'vote'})
payload.append({'iid': vote_num, 'uid': '9561bec0-d626-4c13-8d8b-7506411e0e37', 'react': 'vote'})
payload.append({'iid': vote_num, 'uid': 'a5e1d8e1-a326-46d4-afc7-52cb25bbfc44', 'react': 'vote'})
payload.append({'iid': vote_num, 'uid': '48d0961d-e74d-41d0-9eab-c1fd2b24c43d', 'react': 'vote'})
payload.append({'iid': vote_num, 'uid': 'c3f64b93-bc05-4358-9d8f-9d054a03b1a5', 'react': 'vote'})
payload.append({'iid': vote_num, 'uid': '41cea5a1-ab73-477b-8079-6a33e4c2614e', 'react': 'vote'})
payload.append({'iid': vote_num, 'uid': '4988ca0c-252f-4c7b-a5f2-b20aaab5de05', 'react': 'vote'})
payload.append({'iid': vote_num, 'uid': '8d1af531-36e5-4f04-9416-175a5bdddfe2', 'react': 'vote'})
payload.append({'iid': vote_num, 'uid': 'c763a85b-5ed6-4df7-95d8-58ccf2416a70', 'react': 'vote'})
payload.append({'iid': vote_num, 'uid': '63705fe8-cbd5-4633-86f2-18e01b16952c', 'react': 'vote'})
payload.append({'iid': vote_num, 'uid': '26a20b42-f1ea-4f3b-b1dc-02083b8ac600', 'react': 'vote'})
payload.append({'iid': vote_num, 'uid': '7fb2a071-8a8d-44d8-9d5b-26e75c1d92a1', 'react': 'vote'})
payload.append({'iid': vote_num, 'uid': '018968b4-b53f-4576-88ec-2666022ffb52', 'react': 'vote'})
payload.append({'iid': vote_num, 'uid': '7d6e6c3d-7113-4598-bae2-239ffbbaf342', 'react': 'vote'})
payload.append({'iid': vote_num, 'uid': '906c724a-6fa1-4703-a6f3-aac167a3dcf0', 'react': 'vote'})
payload.append({'iid': vote_num, 'uid': 'e172bbda-1e7b-45dd-9089-3dd71d0af6ec', 'react': 'vote'})
payload.append({'iid': vote_num, 'uid': '8adae4cd-dd57-457e-b6ff-1416fc50de9f', 'react': 'vote'})
payload.append({'iid': vote_num, 'uid': 'b773da5c-b192-4fa1-af37-85f994289c49', 'react': 'vote'})
payload.append({'iid': vote_num, 'uid': 'a0e989b3-1fec-4e6a-93f6-8c4a48474200', 'react': 'vote'})
payload.append({'iid': vote_num, 'uid': '4bc15328-ad5b-4a7a-85f1-b551d4c790c8', 'react': 'vote'})
payload.append({'iid': vote_num, 'uid': '138c39ce-68b5-4e35-a62d-43959343b7fb', 'react': 'vote'})
payload.append({'iid': vote_num, 'uid': '4cc3cd34-3ebb-44f7-a4b4-bfce3909c707', 'react': 'vote'})
payload.append({'iid': vote_num, 'uid': 'd2f6c799-08f1-4071-b3f3-3b454de5110d', 'react': 'vote'})
payload.append({'iid': vote_num, 'uid': '66cbe05e-3201-498c-9574-cfcb02a361ae', 'react': 'vote'})
payload.append({'iid': vote_num, 'uid': 'd0c755f3-43e3-4225-bdeb-ef57950f8b6d', 'react': 'vote'})
payload.append({'iid': vote_num, 'uid': 'b974e163-8ba3-42e9-83a0-60c237bd32cd', 'react': 'vote'})
payload.append({'iid': vote_num, 'uid': 'ae95cc45-3827-4763-a7ae-a1b916c7011b', 'react': 'vote'})
payload.append({'iid': vote_num, 'uid': '8a13b59e-b403-4712-8f53-482b6f0fe6fc', 'react': 'vote'})
payload.append({'iid': vote_num, 'uid': '328c9988-82c6-4815-90ae-2f99d03de15e', 'react': 'vote'})
payload.append({'iid': vote_num, 'uid': 'c7f9e20b-fd00-4160-ad1d-3554484da679', 'react': 'vote'})
payload.append({'iid': vote_num, 'uid': '315fa244-a578-4960-b029-1e898b391a1c', 'react': 'vote'})
payload.append({'iid': vote_num, 'uid': '0446a5b7-569e-48a5-885c-db831ef286e6', 'react': 'vote'})
payload.append({'iid': vote_num, 'uid': '0939c96b-e24b-42cc-aa1b-18288aea90dc', 'react': 'vote'})
payload.append({'iid': vote_num, 'uid': '24ec892e-947e-48db-98da-b3899f449480', 'react': 'vote'})
payload.append({'iid': vote_num, 'uid': 'f83276de-e260-4702-9378-f2c0ac692ed1', 'react': 'vote'})
payload.append({'iid': vote_num, 'uid': '9dcdf119-ee4c-4b7a-8e07-bf7a0ab8a9b7', 'react': 'vote'})
payload.append({'iid': vote_num, 'uid': '4a01f822-adc2-49d8-a90d-4887846ff73f', 'react': 'vote'})
payload.append({'iid': vote_num, 'uid': '9e758db5-4952-4bb1-b033-f3c72b84094f', 'react': 'vote'})
payload.append({'iid': vote_num, 'uid': '060e6911-8e67-43ce-971d-f01f485fdd9f', 'react': 'vote'})

for i in range(len(payload)):
    r.append(requests.post(url, data=payload[i]))

for j in range(len(payload)):
    print(r[j].json()['list'])

while(True):
    t+=1
    time.sleep(1)
    for k in range(len(payload)):
        if time.time()*1000 > int(r[k].json()['list']['nextVoteTime']) :
            time.sleep(1)
            r[k] = requests.post(url, data=payload[k])
            vote += 1
            print(r[k].json()['list'])
    print(vote)
    if t%2 == 0 :
        print('/')
        if t == 10:
            t = 0
    else:
        print('\\')