import requests

url = "https://aweme.snssdk.com/aweme/v1/aweme/favorite/?max_cursor=0&user_id=1415793882432974&count=20&retry_type=no_retry&iid=1319012797003741&device_id=2550465705552974&ac=wifi&channel=tengxun_new&aid=1128&app_name=aweme&version_code=670&version_name=6.7.0&device_platform=android&ssmix=a&device_type=Nexus+6P&device_brand=google&language=zh&os_api=23&os_version=6.0.1&uuid=867686020581318&openudid=848d1fd3a4902e98&manifest_version_code=670&resolution=1440*2392&dpi=560&update_version_code=6702&_rticket=1597376561158&ts=1597376560&app_type=normal&js_sdk_version=1.16.0.0&sec_user_id=MS4wLjABAAAA3SzwcEZ9vGD1s2Pv_xyaMKSe9W4AEoUEn1lwCzXKGUrcNuxrLUKa5Gn-qiF22LRJ"

payload = {}
headers = {
  'Host': 'aweme.snssdk.com',
#   'Cookie': 'odin_tt=759702ca076e1beb3e34c0ac01efb807982ad58f86640df1fc5c9ff5717a873c2c4befcca2c7970861591d9bd82571d8b98a679b7fab73a93ef59507670a3d78; install_id=1319012797003741; ttreq=1$7fa392085bed74b80949d61ed932455c5ac611ce; qh[360]=1',
  'X-SS-REQ-TICKET': '1597376561165',
  'X-Tt-Token': '0056566c650a867fff3f4953c0b547cc7a72bcb9312ec31430b4c049f9448a48402dcff93513d0f4eec05df06606686e445e',
  'sdk-version': '1',
  'User-Agent': 'com.ss.android.ugc.aweme/670 (Linux; U; Android 6.0.1; zh_CN; Nexus 6P; Build/MTC20L; Cronet/58.0.2991.0)',
  'X-Gorgon': '03006cc0000093d002b3a76ab9a8fc85164f7b81af5558d4418d',
  'X-Khronos': '1597376561',
  'X-Pods': ''
}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text)


#####################

params = (
    ('max_cursor', '0'),
    ('user_id', '1415793882432974'),
    ('count', '20'),
    ('retry_type', 'no_retry'),
    ('iid', '1319012797003741'),
    ('device_id', '2550465705552974'),
    ('ac', 'wifi'),
    ('channel', 'tengxun_new'),
    ('aid', '1128'),
    ('app_name', 'aweme'),
    ('version_code', '670'),
    ('version_name', '6.7.0'),
    ('device_platform', 'android'),
    ('ssmix', 'a'),
    ('device_type', 'Nexus 6P'),
    ('device_brand', 'google'),
    ('language', 'zh'),
    ('os_api', '23'),
    ('os_version', '6.0.1'),
    ('uuid', '867686020581318'),
    ('openudid', '848d1fd3a4902e98'),
    ('manifest_version_code', '670'),
    ('resolution', '1440*2392'),
    ('dpi', '560'),
    ('update_version_code', '6702'),
    ('_rticket', '1597376561158'),
    ('ts', '1597376560'),
    ('app_type', 'normal'),
    ('js_sdk_version', '1.16.0.0'),
    ('sec_user_id', 'MS4wLjABAAAA3SzwcEZ9vGD1s2Pv_xyaMKSe9W4AEoUEn1lwCzXKGUrcNuxrLUKa5Gn-qiF22LRJ'),
)

# url = 'https://aweme.snssdk.com/aweme/v1/aweme/favorite/'