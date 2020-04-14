# -*-coding:utf8-*-
# ! 解决html里中文乱码的问题

import requests

def CodeUtils():
    req = requests.get("https://www.dytt8.net/html/gndy/jddy/20160320/50523.html")
    if req.encoding == 'ISO-8859-1':
        encodings = requests.utils.get_encodings_from_content(req.text)
        print(encodings)
        if encodings:
            encoding = encodings[0]
        else:
            encoding = req.apparent_encoding
        # encode_content = req.content.decode(encoding, 'replace').encode('utf-8', 'replace')
        global encode_content
        encode_content = req.content.decode(encoding, 'replace')  # 如果设置为replace，则会用?取代非法字符；
    print(encode_content)
    with open('test.html', 'w', encoding='utf-8') as f:
        f.write(encode_content)
