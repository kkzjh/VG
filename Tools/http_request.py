import requests
from Tools.do_log import DoLog
from config.data import Data
import urllib3
# urllib3.disable_warnings()
from requests.packages.urllib3.exceptions import InsecureRequestWarning

class HttpRequest:
    @staticmethod
    def http_request(url, data, http_method, cookie=None):
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)# 忽略requests证书警告
        try:
            header = {"content-type": "appliation/json",
                      "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36",
                      "token": Data.token}
            if http_method.upper() == 'GET':
                res = requests.get(url, json=data, cookies=cookie, headers=header, verify=False)
            elif http_method.upper() == 'POST':
                res = requests.post(url, json=data, cookies=cookie, headers=header, verify=False)
        except BaseException as e:
            DoLog().error('错误是{}'.format(e))
            raise e
        return res

if __name__ == '__main__':

    url = 'https://x.test.viglle.com/api'
    data = {
            "api":"login@index",
            "data":{
                    "username": "13522272526",
                    "password": "123456"
            }
    }

    re = HttpRequest().http_request(url, data, "post")
    print(re)
    print(re.json()["data"]["token"])
