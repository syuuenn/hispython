# encoding: utf-8
from imp import reload

import requests
import json
import time
import hashlib
import random

if __name__ == '__main__':
    import sys

    reload(sys)
    sys.setdefaultencoding('UTF-8')


def translate(text, to='zh-CHS', fr='ja'):
    S = requests.Session()
    target_url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    target_headers = {
        'Referer': 'http://fanyi.youdao.com/',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
    }
    r = str(int(time.time() * 1000) + random.randint(1, 10))
    src = "fanyideskweb" + text + r + "ebSeFb%=XZ%T[KZ)c(sy!"
    tank = hashlib.md5()
    tank.update(src.encode("utf8"))
    sign = tank.hexdigest()
    Form_Data = {
        'i': text,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': r,
        'sign': sign,
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_CLICKBUTTION',
        'typoResult': 'false'
    }
    target_headers[
        'Cookie'] = '___rl__test__cookies=1519371677462; fanyi-ad-closed=1; fanyi-ad-id=40789; JSESSIONID=aaaJ0epv-u81l5kbPSahw; OUTFOX_SEARCH_USER_ID=-1436919211@10.168.8.61; _ga=GA1.2.75737907.1502714379; OUTFOX_SEARCH_USER_ID_NCOO=685806044.3219135'
    target_response = S.post(url=target_url, data=Form_Data, headers=target_headers)
    translateResult = json.loads(target_response.text)
    return '\n'.join(it['tgt'] for it in translateResult['translateResult'][0])


if __name__ == "__main__":
    s = u"じゃあ"
    t = translate(s, to='zh-CHS', fr='ja')

    print(t)
