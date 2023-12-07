from config.data import Data

test_data = [{"test_code": "1",
              "title": "正常登陆",
              "url": Data().url,
              "data": {
                  "api": "login@index",
                  "data": {
                      "username": "13522272526",
                      "password": "123456"
                  }
              },
              "http_method": "post",
              "expected": 200},
             # --------------------------------------------------
             {"test_code": "2",
              "title": "异常登陆-空密码",
              "url": Data().url,
              "data": {
                  "api": "login@index",
                  "data": {
                      "username": "13522272526",
                      "password": ""
                  }
              },
              "http_method": "post",
              "expected": 500},
             # --------------------------------------------------
             {"test_code": "3",
              "title": "异常登陆-错误密码",
              "url": Data().url,
              "data": {
                  "api": "login@index",
                  "data": {
                      "username": "13522272526",
                      "password": "123455"
                  }
              },
              "http_method": "post",
              "expected": 500},
             # --------------------------------------------------
             {"test_code": "4",
              "title": "异常登陆-空手机号",
              "url": Data().url,
              "data": {
                  "api": "login@index",
                  "data": {
                      "username": "",
                      "password": "12345"
                  }
              },
              "http_method": "post",
              "expected": 500},
             # --------------------------------------------------
             {"test_code": "5",
              "title": "异常登陆-12位错误手机号",
              "url": Data().url,
              "data": {
                  "api": "login@index",
                  "data": {
                      "username": "135222725211",
                      "password": "123456"
                  }
              },
              "http_method": "post",
              "expected": 500},
             # --------------------------------------------------
             {"test_code": "6",
              "title": "异常登陆-10位手机号",
              "url": Data().url,
              "data": {
                  "api": "login@index",
                  "data": {
                      "username": "1352227252",
                      "password": "123456"
                  }
              },
              "http_method": "post",
              "expected": 500},
             # --------------------------------------------------
             {"test_code": "7",
              "title": "异常登陆-未注册手机号",
              "url": Data().url,
              "data": {
                  "api": "login@index",
                  "data": {
                      "username": "13522272590",
                      "password": "123456"
                  }
              },
              "http_method": "post",
              "expected": 500}
             ]
