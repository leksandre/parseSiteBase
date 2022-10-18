import pprint
# from googleapiclient.discovery import build
import optparse
import time
import sys
import os
import re
import threading
import datetime
import random
import json
import psycopg2
import string
import psutil
import subprocess
from random import shuffle
import urllib.parse
from bs4 import BeautifulSoup
from datetime import timezone
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem
try:
    import requests
except ImportError:  # if requests module isn't installed
    if sys.platform.startswith('linux'):  # if platform is linux
        print(" please install requests  module in Debian")
        sys.exit(" sudo apt-get install python-requests ")
    else:
        print(" install requets module for python here : https://pypi.python.org/pypi/requests/2.9.1 or try: pip install requests")
        sys.exit()
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

software_names = [SoftwareName.CHROME.value]
operating_systems = [OperatingSystem.WINDOWS.value,
                     OperatingSystem.LINUX.value]


user_agent_rotator = UserAgent(
    software_names=software_names, operating_systems=operating_systems, limit=100)


name = sys.argv[0].split('/')[-1]
com = 'pgrep -f ' + name

global siteGenDiv20
siteGenDiv20s = sys.argv
siteGenDiv20s.pop(0)
print('siteGenDiv20s',siteGenDiv20s)
siteGenDiv20=int(siteGenDiv20s[0])
if siteGenDiv20>9 or siteGenDiv20<0:
  siteGenDiv20=0

totalQueries = 0

p = subprocess.Popen([com], stdout=subprocess.PIPE, shell=True)
res = p.communicate()[0]

if isinstance(res, bytes):
    res = res.decode("utf-8")
res = [str(x) for x in res.split('\n') if len(x) > 0]


# if len(res) > 0:
#     print('Already running!')
#     print('Exit!')
#     exit()
#     exit()
#     exit()


proxies = {
    'http': 'socks5h://localhost:9050',
    'https': 'socks5h://localhost:9050',
}


class Response1:
    def __init__(self, code1, text1):
        self.status_code = code1
        self.text = text1


num11 = 10
relsite = 1
safe11 = 'off'
counttreads = 0
lastcomment = 0
prev_numpost = 0
lastip = 0
restTorStart = 0
nowH = 0
relsite = 0
safe11 = 'active'
datelist = ['d', 'w', 'm', 'y']
targetlist = []
visitedUrl = []
alreadyAdded = []

blockThread = False
emptylist = []


targetlist3 = ['xamarin', 'ксамарин', 'ксомарин', 'AppGyver', 'App Gyver', 'Аппгайвер', ' Ionic ', 'PhoneGap', 'Phone Gap', 'Sencha Touch', 'SenchaTouch', 'CodeName One', 'CodeNameOne', 'React Native', 'ReactNative', 'Appcelerator', ' PWA ', ' PWA,', ' PWA.', ' pwa ', ' pwa,', ' pwa.', 'GoodBarber', 'Good Barber', 'Shoutem', 'Swiftic', 'AppInstitute', 'App Institute', 'Appy Pie', 'AppyPie', 'Bizness Apps', 'BiznessApps', 'AppYourself', 'App Yourself', 'Mobile Roadie', 'MobileRoadie', 'AppMachine', 'App Machine', 'Mobincube', 'AppsBuilder', 'Apps Builder', 'MobAppCreator', 'Mob App Creator', 'MobApp Creator',
               'AppMakr', 'App Makr', 'IBuild App', 'IBuildApp', 'BuildFire', 'Build Fire', 'Appery.io', 'Gamesalad', 'Zoho Creator', 'ZohoCreator', 'Zengine', 'Зенджин', 'Taplytics', 'Тэплитикс', 'Salesforce', 'Salesforce1', 'Mobile Roadie', 'MobileRoadie', 'Мобайл Роуди', 'Мобикарт', 'MobiCart', 'Гудбарбер', 'GoodBarber', 'Good Barber', 'GameSalad', 'Game Salad', 'Геймсэлэд', 'EachScape', 'Each Scape', ' Ичскейп ', 'BuildFire', 'Bizness Apps', 'BiznessApps', 'AppNotch', 'App Notch', 'AppMakr', 'App Makr', 'App Machine', 'AppMachine', 'Appery.io', 'AppBuilder', 'App Builder', 'App Factory', 'AppFactory', 'app.cat']


def find_phrases2(filename, phrases):
    with open(filename) as file:
        str1 = file.read()
        if len(str1) == 0:
            return False
        text = '\n'.join(str1.split())  # normalize whitespace
    start = text.find(phrases)
    if start == -1:
        return False
    else:
        return True


def find_phrases(filename, phrases):
    with open(filename) as file:
        str1 = file.read()
        if len(str1) == 0:
            return False
        text = ' '.join(str1.split())  # normalize whitespace
    start = text.find(phrases)
    if start == -1:
        return False
    else:
        return True
    # return filter(text.__contains__, phrases) # return phrases themselves


def getip():
    # print('---')
    try:
        r45 = requests.get('https://ident.me', proxies=proxies, timeout=1)
    except requests.exceptions.Timeout as e:
        print("\r SSL Error with : "+str(e))
        restartTor()
        return Response1("201", '')
        # continue
    except requests.exceptions.RequestException as e:
        print("\r Error with  Credentials: "+str(e))
        restartTor()
        return Response1("201", '')
    except requests.ConnectionError:
        print("Can't connect to the site, sorry")
        return Response1("201", '')
        # continue
    print(r45.text)
    # print('---')
    return r45


global time1lastrestart1
time1lastrestart1 = datetime.datetime.now()
# /////////////////////////////////////////////////


def restartTor(sec=0):
    global time1lastrestart1
    global torWath
    # global restTorStart
    # restTorStart = restTorStart+1
    # if restTorStart > 12000:
    #     restTorStart = 0
    #     time.sleep(sec*10)

    diff1 = (datetime.datetime.now()-time1lastrestart1).seconds
    if diff1 < torWath:
        return 0
    # subprocess.run(["brew", "services", "restart", "tor"])
    # subprocess.run(["brew", "services", "reload", "tor"])
    # subprocess.run(["killall", "-HUP", "tor"])
    subprocess.run(["pkill", "-HUP", "tor"])
    time1lastrestart1 = datetime.datetime.now()
    # getip()
    if sec == 0:
        sec = 0.001
    time.sleep(sec)


def getCountryCode(ip=''):
    # print('---')
    try:
        r45 = requests.get('https://freegeoip.app/json/' +
                           str(ip), proxies=proxies, timeout=1)
    except requests.exceptions.Timeout as e:
        print("\r SSL Error with : "+str(e))
        restartTor()
        return 0
        # continue
    except requests.exceptions.RequestException as e:
        print("\r Error with  Credentials: "+str(e))
        restartTor()
        return 0
    except requests.ConnectionError:
        print("Can't connect to the site, sorry")
        return 0
        # continue
    print(r45.text)
    d = json.JSONDecoder()
    rval = d.decode(r45.text)
    countryCode = rval['country_code']
    # print('---')
    return countryCode


def switchProxyIfNeedForCountry():
    while getCountryCode(getip().text) != 'RU':
        restartTor()


def switchProxyIfNeedForGoogle():
    while google() != '200':
        restartTor()


def switchProxyIfNeed(target, targetlist3):
    if target not in targetlist3:
        while getCountryCode(getip().text) != 'RU' and google() != '200' and random.randint(1, 10) > 1:
            restartTor()
    getCountryCode(getip().text)


def google():
    q = 'mobsted'
    randUa = user_agent_rotator.get_random_user_agent()
    headersget = {
        # random.choice(ua14) , #
        'User-Agent': randUa,
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    }
    # s = requests.Session()
    q = '+'.join(q.split())
    url = 'https://www.google.com/search?q=' + q + '&ie=utf-8&oe=utf-8'
    try:
        r = requests.get(url, headers=headersget,
                         proxies=proxies, timeout=1)
    except requests.exceptions.Timeout as e:
        print("\r SSL Error with : "+str(e))
        restartTor()
        return '201'

    except requests.exceptions.RequestException as e:
        print("\r Error with  Credentials: "+str(e))
        restartTor()
        return '201'

    # print ('google target :'+str(r.status_code) + ' q:'+str(q))
    print('google target :'+str(r.status_code))
    return str(r.status_code)
    # soup = BeautifulSoup(r.text, "html.parser")
    # output = []
    # for searchWrapper in soup.find_all('h3', {'class':'r'}): #this line may change in future based on google's web page structure
    #    url = searchWrapper.find('a')["href"]
    #    text = searchWrapper.find('a').text.strip()
    #    result = {'text': text, 'url': url}
    #    output.append(result)
    # return output


def find_all(a_str, sub):
    a_str = a_str.lower()
    sub = sub.lower()
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1:
            return
        yield start
        start += len(sub)


def makeGetRequest(url, main):

    if url[-4].find('.jpg') > -1:
        return None
    if url[-4].find('.png') > -1:
        return None
    if url[-5].find('.tiff') > -1:
        return None
    if url[-4].find('.tif') > -1:
        return None
    if url[-4].find('.bmp') > -1:
        return None
    if url[-5].find('.jpeg') > -1:
        return None
    if url[-4].find('.gif') > -1:
        return None
    if url[-4].find('.eps') > -1:
        return None
    if url[-4].find('.raw') > -1:
        return None
    
    nproxy=False
    if url.find('.php') > -1:
        print((url, main))
    # if url.find('video')>-1:
    # print('(url, main)')
    # print((url, main))
    str1, str2, *_ = main.split('//')
    if url.find(str2) == -1:
        return None
    global visitedUrl
    if(random.randint(1,99999)==9):
        visitedUrl=[]
    if str(url) in visitedUrl:
        return None
    visitedUrl.append(url)
    if(random.randint(1,1000)==1):
      print(url)
    counttryes = 0
    global httpTimeOut
    while True:
        useTor = True
        r = Response1("0", '')
        counttryes = counttryes+1
        if counttryes > 2:
            return None
        if counttryes > 1:
            nproxy = not nproxy
        try:

            randUa = user_agent_rotator.get_random_user_agent()
            # print ('randUa:'+str(randUa))
            if not nproxy:
             useTor = False
             r = requests.get(url, headers={
                'origin': url,
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'user-agent': randUa
             }, timeout=httpTimeOut, allow_redirects=True)  # , allow_redirects=True
            else:
             r = requests.get(url, headers={
                'origin': url,
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'user-agent': randUa
             }, proxies=proxies, timeout=httpTimeOut, allow_redirects=True)
            # print ('status_code:'+str(r.status_code))
            # print ('r.text:'+str(r.text)[0:100])
            # print(r.headers)
            # print(r.headers['Content-Type'])
            if r.history:
                # print("Request was redirected")
                # for resp in r.history:
                #     print(r.status_code, resp.url)
                # print("Final destination:")
                # print(r.status_code, r.url)
                return makeGetRequest(r.url,main)

            if str(r.headers['Content-Type']).find('text/html') == -1 and str(r.headers['Content-Type']).find('application/json') == -1:
                return None
        except requests.ConnectionError as e:  # if host don't exist
            # print(url)
            # print('requests.HTTPError:'+str(requests))
            # print("[-] host die  ConnectionError: "+str(e))
            # sys.exit()
            if useTor:
             restartTor()
            # time.sleep(10)
            continue
        except requests.HTTPError as e:
            print("[-] host die  HTTPError: "+str(e))
            if useTor:
             restartTor()
            # time.sleep(1)
            continue
        except requests.exceptions.ConnectTimeout as e:
            print("[-] host die  ConnectTimeout: "+str(e))
            # time.sleep(random.randint(1,3))
            if useTor:
             restartTor()
            # time.sleep(1)
            continue
        except requests.exceptions.ReadTimeout as e:
            if(random.randint(1,1000)==1):
              print("[-] host die  ReadTimeout: "+str(e))
            # time.sleep(random.randint(1,3))
            if useTor:
             restartTor()
            # time.sleep(1)
            continue
        except requests.exceptions.Timeout as e:
            print("[-] host die  Timeout: "+str(e))
            # time.sleep(random.randint(1,3))
            if useTor:
             restartTor()
            # time.sleep(1)
            continue
        except requests.exceptions.TooManyRedirects as e:
            print("[-] host die TooManyRedirects: "+str(e))
            # time.sleep(random.randint(1,3))
            if useTor:
             restartTor()
            # time.sleep(1)
            continue
        except requests.exceptions.RequestException as e:
            # catastrophic error. bail.
            # print("[-] host die RequestException: "+str(e))

            if (str(str(e))).find('Failed to parse:') != -1:
                # return None
                continue
        except:
            if useTor:
             restartTor()
            # time.sleep(1)
            continue
            # sys.exit(1)

        if int(r.status_code) != 200:
            # print("restart tor r.status_code= "+str(r.status_code))
            if useTor:
             restartTor()
            # time.sleep(1)
            # return None
            continue

        d = json.JSONDecoder()
        if r.text == None:
            print("[-] empty result from  "+str(url))
            restartTor()
            continue
        try:
            items23r = r.text
            if len(items23r) <= 20:
                print("[-] empty result from  "+str(url))
                restartTor()
                continue
        except:
            print('I got a KeyError - reason r.text ')
            print(repr(r.text))
            if useTor:
             restartTor()
            continue
        if len(str(items23r)) == 0:
            if useTor:
             restartTor()
            continue
        # print(url)
        # print(r.text[0:100])
        return r.text


def recursiveUrl(url, link, depth, urlMain, strUrl, alreadyAdded, time1start1):
    diff1 = (datetime.datetime.now()-time1start1).seconds
    # print('spentTime seconds:'+str(diff1))
    # global diffTimeProcess
    # if diff1 > diffTimeProcess:
    #     return url
    if link is None:
        return url
    global depthSite
    if depth > depthSite:
        return url
    if len(alreadyAdded) > 2:
        return url
    # print(type(link))
    # print(link['href'])
    if link == '#####':
        link = {'href': '#####'}
    else:
        if isinstance(link, str):
            link = {'href': link}
        else:
            if not link.has_attr('href'):
                return url

    # try:
    #     a1111test = link['href']
    # except ValueError:
    #     return url

    if len(link['href']) < 2:
        return url
    global visitedUrl
    if str(url)+link['href'] in visitedUrl:
        return None

    newUrl = link['href']
    if str(link['href']).find('http://') == -1 and str(link['href']).find('https://') == -1:
        newUrl = str(url) + link['href']

    page = makeGetRequest(newUrl, str(urlMain))
    visitedUrl.append(str(url)+link['href'])
    # print(page[0:100])
    newlink = []
    newlink1 = []
    emails_mailtos = []
    emails_mailtos1 = []
    mailtos = []
    if not page is None:
        emails_mailtos = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", page)
        soup1 = BeautifulSoup(page, 'html.parser')
        mailtos = soup1.select('a[href^=mailto]')
        newlink1 = soup1.select('a')
        newlink = newlink1
        for a in soup1.find_all('a', href=True):
         if a['href']:
          newlink.append(a['href'])
          if (a['href']).find('linkedin.com')>-1:
           mailtos.append(a)
    newUrl = link['href']
    if str(link['href']).find('http://') == -1 and str(link['href']).find('https://') == -1:
        newUrl = str(url) + link['href']
    page2 = makeGetRequest(newUrl, str(urlMain))

    # print(page2[0:100])
    mailtos2 = []
    if not page2 is None:
        emails_mailtos1 = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", page2)
        soup = BeautifulSoup(page2, 'html.parser')
        mailtos2 = soup.select('a[href^=mailto]')
        newlink = soup.select('a')
        for a in soup.find_all('a', href=True):
         if a['href']:
          newlink.append(a['href'])
    # print('mailtos2')
    # print(mailtos2)
    # print('url:'+str(url))
    # print('urlMain:'+str(urlMain))
    # print('alreadyAdded:'+str(alreadyAdded))
    some_list = mailtos+mailtos2+emails_mailtos+emails_mailtos1
    mailtos = list(dict.fromkeys(some_list))

    # print('newlink')
    # print(newlink)
    # time.sleep(20)
    # print('mailtos!!')
    # print(mailtos)
    for i in mailtos:
        if 'href' in i:
            href = i['href']
            try:
                str1, str2 = href.split(':')
            except ValueError:
                continue

            str2 = str2.lower()
            if str2.find('?subject') != -1:
                try:
                    str2, str1 = str2.split('?subject')
                except ValueError:
                    continue
            if str2.find('mailto:') != -1:
                try:
                    str1, str2 = str2.split('ailto:')
                except ValueError:
                    continue
            str2 = str2.strip(' \t\n\r')
            str2 = str2.strip()
            # print(str(str2))
            # global alreadyAdded
            # if not find_phrases(filename11, str2) and not str2 in alreadyAdded:
            #     f = open(filename11, 'a')
            #     f.write(str(str2)+'\n')
            #     f.close()
            #     alreadyAdded.append(str2)
            #     print('++text in file')
            # else:
            #     print('--text already in file')

            if (not str2 in alreadyAdded) and ('@' in str2):
                alreadyAdded.append(str2)
                print('++new mail')
                print(alreadyAdded)
            if (not href in alreadyAdded) and ('@' in href):
                alreadyAdded.append(str2)
                print('++new mail_href')
                print(alreadyAdded)
            # else:
            #     print('--was')

    if newlink is None:
        newlink = newlink1

    if newlink is None:
        return link

    if len(newlink) == 0:
        newlink = newlink1

    if len(newlink) == 0:
        return link
    newlink = list(dict.fromkeys(newlink))
    for link1 in newlink:
        recursiveUrl(url, link1, depth + 1, urlMain, strUrl, alreadyAdded, time1start1)

        # while threading.active_count() > 9999:
        #     time.sleep(random.randint(10, 30))
        # # print('startTime:'+str(datetime.datetime.now()))
        # thread = threading.Thread(
        #     target=recursiveUrl, args=(url, link1, depth + 1, urlMain, strUrl, alreadyAdded, time1start1))
        # thread.daemon = True
        # thread.start()


def makeGetRequestAddData(url, data, nproxy=False):

    new_list = data.copy()
    site1 = new_list.pop(0)
    strForWrite = ';'.join(new_list)
    if True:
        useTor = False
        r = Response1("0", '')

        try:
            randUa = user_agent_rotator.get_random_user_agent()
            data2 = {"site": str(site1), "resText": str(strForWrite),   "resJson": new_list }  #"resJsonArr": data[10],
            r = requests.post(url, headers={
            'origin': url,
            # 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'content-type': 'application/json',
            'user-agent': randUa
            }, timeout=120, allow_redirects=True, json=(data2), verify=False )
            print(r.text)
            # r.close()
        except requests.ConnectionError as e:
            print("[-] host die  ConnectionError: "+str(e))
        except requests.HTTPError as e:
            print("[-] host die  HTTPError: "+str(e))
        except requests.exceptions.ConnectTimeout as e:
            print("[-] host die  ConnectTimeout: "+str(e))
        except requests.exceptions.ReadTimeout as e:
            print("[-] host die  ReadTimeout: "+str(e))
        except requests.exceptions.Timeout as e:
            print("[-] host die  Timeout: "+str(e))
        except requests.exceptions.TooManyRedirects as e:
            print("[-] host die TooManyRedirects: "+str(e))
        except requests.exceptions.RequestException as e:
            print("[-]requests.exceptions.RequestException: "+str(e))
        except:
            print("[-] some excep: ")
            return None

        if int(r.status_code) != 200:
            return None
     
        return r


 


def check_lives(url, urlMain, strUrl, siteData, time1start, strForWrite, n, isShopify, idRecord, linksprofileStr):

    print('idRecord "',idRecord,'"; linksprofileStr "',linksprofileStr,'"; url "',url,'"; urlMain "',urlMain,'"; strUrl "',strUrl,'"; siteData "',siteData,'"; time1start "',time1start,'"; strForWrite "',strForWrite,'"; n ',n,'"; isShopify ', isShopify)
    
    try:
        for x in range(0, 999):
            try:
                    tshema = 'great_paraser'
                    conpg = psycopg2.connect(database=tshema, user=pguser, password=pgpswd,
                            host=pghost, port=pgport) # , options=f'-c search_path={pgschema}'
            except:
                time.sleep(0.2)
                pass
            finally:
                break

        if conpg:
         with conpg:
             with conpg.cursor() as curpg:
                sql = " Set search_path =%(pgdb)s "
                params={"pgdb":pgdb}
                curpg.execute(sql,params)
                # conpg.commit()
        str2 = url.replace('http://', '')
        str2 = str2.replace('https://', '')
        if conpg:
         with conpg:
             with conpg.cursor() as curpg:
                if len(strForWrite)>0:
                  if str(strForWrite).find("@") > -1:
                    sql = " Update projects set \"Emails\"=%(strForWrite)s where id=%(id)s "
                    params={"strForWrite":strForWrite,"id":idRecord}
                    curpg.execute(sql,params)
                if len(linksprofileStr)>2:
                    sql = " Update projects set \"profileUrl\"=%(linksprofileStr)s where id=%(id)s "
                    params={"linksprofileStr":linksprofileStr,"id":idRecord}
                    curpg.execute(sql,params)
                if isShopify:
                    sql = " Update projects set  \"isShopify\"=%(isShopify)s where id=%(id)s "
                    params={"isShopify":isShopify,"id":idRecord}
                    curpg.execute(sql,params)
                
                sql = " Update projects set  \"LastModified\" = now() where id=%(id)s "
                params={"isShopify":isShopify,"id":idRecord}
                curpg.execute(sql,params)
                conpg.commit()

            # #   for x in range(0, 99):
            # #     try:
            # #         curpg.execute(sql,params)
            # #         conpg.commit()
            # #     except:
            # #         time.sleep(1)
            # #         pass
            # #     finally:
            # #         break
            #   if protocol!='https://' and protocol!='http://':
            #     if site16=='None':
            #       site16='0'
            #     sql = " Update projects set tryesnotproxy=%(tryesnotproxy)s where id=%(id)s"
            #     params={"tryesnotproxy":int(str(site16 or 0))+1,"id":site0}
            #     curpg.execute(sql,params)
            #     print('protocol update - ',int(str(site16 or 0)),'  ',siteData1)
            #     # conpg.commit()

            #     # for x in range(0, 99):
            #     #     try:
            #     #         curpg.execute(sql,params)
            #     #         conpg.commit()
            #     #     except:
            #     #         time.sleep(1)
            #     #         pass
            #     #     finally:
            #     #       break

            #     if int(str(site16 or 0))>17:#10
            #         sql = " Update projects set statussite=%(statussite)s where id=%(id)s"
            #         params={"statussite":'not work',"id":site0}
            #         curpg.execute(sql,params)
            #         # # 

            #         # for x in range(0, 99):
            #         #     try:
            #         #         curpg.execute(sql,params)
            #         #         conpg.commit()
            #         #     except:
            #         #         time.sleep(1)
            #         #         pass
            #         #     finally:
            #         #         break
            #     conpg.commit()
    except psycopg2.DatabaseError as e:
        print('Error %s' % e)



def main33(url, urlMain, strUrl, n, time1start, idRecord):
    isShopify = False;
    # rtext = makeGetRequest('http://'+str(url), 'http://'+str(urlMain))
    rtext = makeGetRequest(str(url), str(urlMain))
    links = [url+'/']
    emails_mailtos = []
    linksprofileStr = ''
    if rtext is None:
        return False
    if not rtext is None:
        emails_mailtos = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", rtext)
        if rtext.find('cdn.shopify.com') != -1:
            isShopify = True;
            print('url "',url,'"; isShopify ', isShopify)
        else:
          if rtext.find('.shopify.com') != -1:
            isShopify = True;
            print('url "',url,'"; isShopify v2 ', isShopify)
        soup = BeautifulSoup(rtext, 'html.parser')
        #links = []; #soup.find_all('a')
        linksprofile = [] #soup.find_all("a", class_="header__icon header__icon--account link focus-inset small-hide")
        for a in soup.find_all('a', href=True):
            # print(a['href'])
            # print(str(a['href']))
            if(len(str(a['href']))==0):
                continue
            # print(str(a['href'])[0])
            if str(a['href'])[0]!='/':
                links.append(a['href']);
            else:
                links.append(url+a['href']);

            if a['href'].find('/account/login') != -1:
                linksprofile.append(a['href'])
            if a['href'].find('?locale=') != -1:
                linksprofile.append(a['href'])
        some_linksprofile = linksprofile
        linksprofile = list(dict.fromkeys(some_linksprofile))
        linksprofileStr = json.dumps(linksprofile)

    # rtext = makeGetRequest('https://'+str(url), 'https://'+str(urlMain))
    # rtext = makeGetRequest(str(url), str(urlMain))
    # links2 = []
    # if not rtext is None:
    #     if rtext.find('cdn.shopify.com') != -1:
    #         isShopify = True;
    #         print('url "',url,'"; isShopify ', isShopify)
    #     else:
    #      if rtext.find('.shopify.com') != -1:
    #         isShopify = True;
    #         print('url "',url,'"; isShopify v2 ', isShopify)
    #     soup = BeautifulSoup(rtext, 'html.parser')
    #     links2 = soup.find_all('a')

    # some_list = links + links2
    some_list = links
    links = list(dict.fromkeys(some_list))

    
    # print('links')
    # print(links)

    alreadyAdded1 = emails_mailtos
    alreadyAdded1.append(strUrl)

    Object1 = '#####'
    # recursiveUrl('http://'+str(url), Object1, 0,
    #              'http://'+str(urlMain), strUrl, alreadyAdded1, time1start)
    # recursiveUrl('https://'+str(url), Object1, 0,
    #              'https://'+str(urlMain), strUrl, alreadyAdded1, time1start)
    recursiveUrl(str(url), Object1, 0,
                 str(urlMain), strUrl, alreadyAdded1, time1start)

    for link in links:
        # print('link')
        # print(link)
        # recursiveUrl('http://'+str(url), link, 0,
        #              'http://'+str(urlMain), strUrl, alreadyAdded1, time1start)
        # recursiveUrl('https://'+str(url), link, 0,
        #              'https://'+str(urlMain), strUrl, alreadyAdded1, time1start)
        recursiveUrl(str(url), link, 0,
                     str(urlMain), strUrl, alreadyAdded1, time1start)
    # links.append()
    # print('result links')
    # print(result1)
    # print('result mails')
    # print(result2)
    strForWrite = ';'.join(alreadyAdded1)
    jsonStr = json.dumps(alreadyAdded1)
    if len(alreadyAdded1)>1 or isShopify: 
        # print('wrote')
        print(strForWrite) 

        thread = threading.Thread(
            target=check_lives, args=(url, urlMain, strUrl, alreadyAdded1, datetime.datetime.now(),jsonStr,n, isShopify, idRecord, linksprofileStr))
        thread.daemon = True
        thread.start()        
        

def fromBase():
    global siteGenDiv20
    print('siteGenDiv20',siteGenDiv20)
    try:
        tshema = 'great_paraser'
        conpg = psycopg2.connect(database=tshema, user=pguser, password=pgpswd,
                                host=pghost, port=pgport, options=f'-c search_path={tshema}')
        curpg = conpg.cursor(name='foo11')
        if conpg:
         with conpg:
             with conpg.cursor() as curpg:
               sql = "SELECT  domain, protocol, id FROM projects  where (\"protocol\"='https://' or  \"protocol\"='http://') and ( \"profileUrl\" is null or \"Emails\" is null or  \"Emails\" = '' or \"Emails\" not like '%@%') and MOD(id,10)="+str(siteGenDiv20)+" order by \"LastModified\" asc;" 
               #sql = "SELECT  domain, protocol, id FROM projects  where domain='shopmajorskylights.com' order by \"LastModified\" desc;" 
               
               curpg.execute(sql)
               res1 = curpg.fetchall()
            #    print('res1 %s' % len(res1[0]))
               return res1
    except psycopg2.DatabaseError as e:
        print('Error %s' % e)


# uniqlines = set(open(fname,'r', encoding='utf-8').readlines())
# gotovo = open(fname,'w', encoding='utf-8').writelines(set(uniqlines))

# f = open(fname, 'r')
# text = f.readlines()
# f.close()
# random.shuffle(text)

# f = open(fname, 'w')
# f.writelines(text)
# f.close()
global httpTimeOut
httpTimeOut = 0
global torWath
torWath = 2
global diffTimeProcess
diffTimeProcess = 3
global depthSite
depthSite = 4
first = True

maxProcCount = 499

i1 = 0

pgdb = 'great_paraser'
pguser = 'postgres'
pgpswd = 'blabla'
pghost = '0.1.1.1'
pgport = '5432'
# pgschema = 'great_paraser'
max_process_count = 2
d1 = json.JSONDecoder()



while True:


    if torWath > 10:
        torWath=2
    if diffTimeProcess>25:
        diffTimeProcess=3
    if depthSite > 15:
         depthSite=4
    if httpTimeOut > 5:
        httpTimeOut = 0

    torWath = torWath + 1
    diffTimeProcess = diffTimeProcess + 2
    depthSite = depthSite+1
    httpTimeOut = httpTimeOut+1
    
    print(str(threading.active_count())+' - threading.active_count()')
    print(str(torWath)+' - torWath')
    print(str(diffTimeProcess)+' - diffTimeProcess')
    print(str(depthSite)+' - depthSite')
    print(str(httpTimeOut)+' - httpTimeOut')

    siteGen = fromBase()
    if not siteGen:
        time.sleep(300)
        continue
    print(str(len(siteGen))+' - len(siteGen)')
    shuffle(siteGen)
    for siteData in siteGen:
        # print(siteData[0])
        str2 = str(siteData[0])
        str2 = str2.replace('http://', '')
        str2 = str2.replace('https://', '')
        if len(str2) < 3:
            continue

        str1 = siteData[1]+str2.strip()
        str2 = siteData[1]+str2.strip()

        if threading.active_count() < maxProcCount:
            # print('startTime:'+str(datetime.datetime.now()))
            thread = threading.Thread(
                target=main33, args=(str1, str1, str2, i1, datetime.datetime.now(), siteData[2]))
            thread.daemon = True
            thread.start()
            # time.sleep(random.randint(10, 30))
            # time.sleep(14)
            if(random.randint(1,1000)==1):
                print('--------------------------------'+str(str1))
        else:
            # print('---')
            # print('sleep')
            time.sleep(120)
            # restartTor()
            # try:
            #     r45 = requests.get('https://ident.me',
            #                        proxies=proxies, timeout=1000)
            # except requests.exceptions.Timeout as e:
            #     print("\r SSL Error with : "+str(e))
            #     restartTor(5)

            # except requests.exceptions.RequestException as e:
            #     print("\r Error with  Credentials: "+str(e))
            #     restartTor(5)

            # print(r45.text)

            # print('---')
    first = False

# for i in range(0, 61):
#     print('current active process:'+str(threading.active_count()))
#     time.sleep(60)
while threading.active_count() > 1:
    print('--')
    time.sleep(300)
print('exit')
