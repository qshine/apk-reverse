import requests

headers = {
    'authority': 'www.amemv.com',
    'accept': 'application/json',
    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
    'x-requested-with': 'XMLHttpRequest',
    # 'sec-fetch-site': 'same-origin',
    # 'sec-fetch-mode': 'cors',
    # 'sec-fetch-dest': 'empty',
    # 'referer': 'https://www.amemv.com/share/user/62081600644',
    # 'accept-language': 'zh,en;q=0.9,pt;q=0.8,pl;q=0.7,zh-CN;q=0.6',
}

params = (
    ('user_id', '62081600644'),
    ('sec_uid', ''),
    ('count', '21'),
    ('max_cursor', '0'),
    ('aid', '1128'),
    ('_signature', '2..FTRAZhNKoCc8iW8.kSNv.xV'),
    ('dytk', 'caf651e2cb880caae4109178baba37f2'),
)

response = requests.get('https://www.amemv.com/web/api/v2/aweme/like/', headers=headers, params=params)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://www.amemv.com/web/api/v2/aweme/like/?user_id=62081600644&sec_uid=&count=21&max_cursor=0&aid=1128&_signature=2..FTRAZhNKoCc8iW8.kSNv.xV&dytk=caf651e2cb880caae4109178baba37f2', headers=headers)

print(response.text)