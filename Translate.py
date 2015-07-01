# -*- coding: utf-8 -*-
import json
import sys
import requests
reload(sys)
sys.setdefaultencoding('utf-8')

def translate(sentence):
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc'
    data = {s
            "type" : "AUTO",
            "i" : sentence,
            "doctype" : "json",
            "xmlVersion" : "1.8",
            "keyfrom" : "fanyi.web",
            "ue" : "UTF-8",
            "action" : "FY_BY_CLICKBUTTON",
            "typoResult" : "true"
        }
    content = requests.post(url, data).content
    mydict = json.loads(content)
    return mydict.get('translateResult')[0][0].get('tgt')
if __name__ == '__main__':
    while 1:
        sentence = raw_input(u'请输入要翻译的句子：')
        print translate(sentence)