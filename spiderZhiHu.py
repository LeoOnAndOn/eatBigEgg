import re
import requests

def getAnswer(qid,offset):
    header = {'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/538.36'
    }
    url = "https://www.zhihu.com/api/v4/questions/{}/answers?include=content&limit=10&offset={}&platform=desktop&sort_by=default".format(
        qid,offset)

    res = requests.get(url,headers=header)
    res.encoding = 'utf-8'
    return res.text

def tj():
    qid = '35584877'
    offset = 0
    dic = {}
    p = r'《(.*?)》'
    while offset < 500:
        html = getAnswer(qid,offset)
        if len(html) < 0:
            break
        data = re.findall(p,html)
        for bookname in data:
            if bookname in dic.keys():
                dic[bookname] += 1
            else:
                dic[bookname] = 1            
      
        print('进度：{}/500'.format(offset+10))
        offset += 10
    print(dic)


if __name__ == '__main__':
    tj()