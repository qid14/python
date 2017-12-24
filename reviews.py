import bs4
import requests
import json

data_list = []


def pprint(n, url):
    tempurl = url
    tempurl = tempurl + str(n)
    print('here is the new url:----------', tempurl, n)
    assert isinstance(tempurl, object)
    response = requests.get(tempurl)
    soup = bs4.BeautifulSoup(response.text, "lxml")
    tag = soup.find("table", class_="FbOuterYukon")
    dict2 = {}
    dict1 = {}
    dictMerged2 = {}
    for idx, tr in enumerate(tag.find_all('tr')):
        # pass

        print idx, tr
        tds = tr.find_all('td')
        if idx <> 0:
            # print idx,tr
            # tds = tr.find_all('td')
            print tds
            if idx % 2 == 0:
                try:
                    dict1 = {
                    'category': tds[1].contents[0],
                    'Price': float(tds[2].string[4:])}
                except:
                    print('except here is the new url:----------')
            else:
                print('else ???here is the new url:----------')
        else:
            dict2 = {

                    'feedbacktime': tds[3].string
                }
            if (dict1 != {} and dict2 != {}):
                dictMerged2 = dict(dict2, **dict1)
            if (idx % 2) == 0:
                data_list.append(dictMerged2)
        print(data_list)
    return data_list


root_url = 'http://feedback.ebay.com/ws'
index_url = root_url + '/eBayISAPI.dll?ViewFeedback2&ftab=AllFeedback&userid=adp1018&iid=-1&de=off&items=200&interval=0&searchInterval=30&mPg=8836&page='

FILE_PATH = 'testddd'
FILE_NAME = 'adp1018.json'

for x in range(2, 17):
    pprint(x, index_url)
    fname = FILE_PATH + '/' + FILE_NAME
    print fname
    f = open(fname, 'w')
    f.write("[")

    jsObj = json.dumps(data_list)

    for ip in data_list:
        print ip
        jsObj = json.dumps(ip)
        print jsObj
        f.write(jsObj)
        f.write(',\n')
f.write(']')
f.close()
