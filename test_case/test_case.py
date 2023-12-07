import unittest
from Tools.http_request import HttpRequest
from Tools.get_data import GetData
from config.data import Data
from Tools.autonumber import AutoNumber
from Tools.do_log import DoLog
import warnings


class TestHttpRequest(unittest.TestCase):

    def setUp(self) -> None:
        warnings.simplefilter('ignore', ResourceWarning)

    # 登陆
    def test_login(self):
        DoLog().info('开始执行用例{}:{}'.format("test_login", "正常登陆"))
        url = Data().url
        data = {
            "api": "login@index",
            "data": {
                "username": "13522272526",
                "password": "123456"
            }
        }
        runner = HttpRequest().http_request(url, data, 'post')
        if runner.cookies:
            setattr(GetData, 'cookie', runner.cookies)
        try:
            self.assertEqual(200, runner.json()['code'])
        except BaseException as e:
            DoLog().info('执行用例错误{}！！！！！！'.format(e))
            raise e
        finally:
            DoLog().error('获取到的结果是{}'.format(runner.json()))

    # 新增客户
    def test_adduser(self):
        DoLog().info('开始执行用例{}:{}'.format("test_adduser", "新增客户{}".format(AutoNumber.autonumber())))
        url = Data().url
        data = {
    "api": "user@add",
    "data": {
        "pid": "",
        "name": "客户名称{}".format(AutoNumber.autonumber()),
        "type": 1,
        "short_name": "客户简称{}".format(AutoNumber.autonumber()),
        "code": "PP{}".format(AutoNumber.tcode()),
        "registered_capital": "100",
        "business_id": 2,
        "business_license_end_time": "",
        "business_license_time_type": 2,
        "pid_attachmentObj": {},
        "legal_person": "张三",
        "ein": "12345",
        "found_time": 1647273.6,
        "yyzz_attachmentObj": {
            "staticpath": "http://static.test.viglle.com/",
            "filepath": "202203/45b75830-4442-8ee8-d8e6-2b44c971ce7a.png",
            "filename": "WechatIMG7.png"
        },
        "yyzz_attachment": "202203/45b75830-4442-8ee8-d8e6-2b44c971ce7a.png"
    }
        }
        runner = HttpRequest().http_request(url, data, 'post', getattr(GetData, 'cookie'))
        try:
            self.assertEqual(200, runner.json()['code'])
        except BaseException as e:
            DoLog().info('执行用例错误{}！！！！！！'.format(e))
            raise e
        finally:
            DoLog().error('获取到的结果是{}'.format(runner.json()))


    # 提交供应商
    def test_addsupplier(self):
        DoLog().info('开始执行用例{}:{}'.format("test_addsupplier", "新增供应商{}".format(AutoNumber.autonumber())))
        url = Data().url

        data = {
    "api": "supplier@add",
    "data": {
        "operate_type": 2,
        "supplier_info": {
            "type": 4,
            "name": "供应商名称1{}".format(AutoNumber.autonumber()),
            "short_name": "供应商简称1{}".format(AutoNumber.autonumber()),
            "xt_short_name": "星图简称",
            "pgy_short_name": "蒲公英简称",
            "id_number": "123456",
            "is_share": 2,
            "qr_code": "",
            "idcard_prove": "202203/b38d33df-33a4-8eb9-ca62-499b56c255ea.png",
            "supplier_code": "PP{}".format(AutoNumber.tcode()),
            "is_payment": 1,
            "payment_time": "10"
        },
        "bank_info": {
            "type": 1,
            "real_name": "开户名",
            "bank_card": "6222023452546508903",
            "open_bank": "中国民生银行",
            "bank_branch": "中国民生银行股份有限公司北京门头沟支行",
            "bank_prove": "202203/423c2028-c298-9cff-05d8-c25f5b6dadfa.png"
        },
        "invoice_info": {
            "title": "公司",
            "ein": "123456789",
            "address": "单位地址",
            "phone": "13522272526",
            "bank_card": "6222023452546508903",
            "open_bank": "中国农业银行",
            "bank_branch": "中国农业银行迪拜人民币清算行",
            "invoice_prove": "202203/3ab9ec3d-f49d-fc28-ad6c-68cc939028cc.png",
            "fp_attachment": "202203/f2396c16-6458-9052-69e2-726ad8b0190d.png"
        },
        "contact_info": [
            {
                "contact": "姓名",
                "position": "职位",
                "phone": "13522272535",
                "email": "1@qq.com"
            }
        ]
    }
}
        runner = HttpRequest().http_request(url, data, 'post', getattr(GetData, 'cookie'))
        try:
            self.assertEqual(200, runner.json()['code'])
        except BaseException as e:
            DoLog().info('执行用例错误{}！！！！！！'.format(e))
            raise e
        finally:
            DoLog().error('获取到的结果是{}'.format(runner.json()))

    # 新增抖音未抓取资源
    def test_adddouyinf(self):
        DoLog().info('开始执行用例{}:{}'.format("test_adddouyinf", "新增抖音未抓取资源{}".format(AutoNumber.autonumber())))
        url = Data().url
        data = {
    "api": "resource@add",
    "data": {
        "platform": 5,
        "tags": "美妆",
        "link": "https://v.douyin.com/N52wxNT/",
        "account_id": "",
        "account_code": "664746762{}".format(AutoNumber.autonumber()),
        "real_link": "",
        "avatar_url": "",
        "name": "来自葫芦岛的执着风爪{}".format(AutoNumber.autonumber()),
        "desc": "账号简介",
        "sex": "",
        "focus_num": "30",
        "fans_num": "26",
        "works_num": "1",
        "like_num": "1",
        "auth_info": "认证信息",
        "area": "地区",
        "is_grab": "",
        "average_read_num": "111",
        "average_interaction_num": "222",
        "supplier_id": 66,
        "recommend_remark": "333",
        "cooperation_remark": "444"
    }
}
        runner = HttpRequest().http_request(url, data, 'post', getattr(GetData, 'cookie'))
        try:
            self.assertEqual(200, runner.json()['code'])
        except BaseException as e:
            DoLog().info('执行用例错误{}！！！！！！'.format(e))
            raise e
        finally:
            DoLog().error('获取到的结果是{}'.format(runner.json()))

    # 新增抖音抓取资源
    def test_adddouyint(self):
        DoLog().info('开始执行用例{}:{}'.format("test_adddouyint", "新增抖音抓取资源{}".format(AutoNumber.autonumber())))
        url = Data().url
        data = {
    "api": "resource@add",
    "data": {
        "platform": 5,
        "tags": "美妆",
        "link": "https://v.douyin.com/N52wxNT/test",
        "account_id": "",
        "account_code": "664746762{}".format(AutoNumber.autonumber()),
        "real_link": "",
        "avatar_url": "",
        "name": "来自葫芦岛的执着风爪{}".format(AutoNumber.autonumber()),
        "desc": "账号简介",
        "sex": "",
        "focus_num": "30",
        "fans_num": "26",
        "works_num": "1",
        "like_num": "1",
        "auth_info": "认证信息",
        "area": "地区",
        "is_grab": "1",
        "average_read_num": "111",
        "average_interaction_num": "222",
        "supplier_id": 66,
        "recommend_remark": "333",
        "cooperation_remark": "444"
    }
}
        runner = HttpRequest().http_request(url, data, 'post', getattr(GetData, 'cookie'))
        try:
            self.assertEqual(200, runner.json()['code'])
        except BaseException as e:
            DoLog().info('执行用例错误{}！！！！！！'.format(e))
            raise e
        finally:
            DoLog().error('获取到的结果是{}'.format(runner.json()))

    # 新增微信未抓取资源
    def test_addweixinf(self):
        DoLog().info('开始执行用例{}:{}'.format("test_addweixinf", "新增微信未抓取资源{}".format(AutoNumber.autonumber())))
        url = Data().url
        data = {
    "api": "resource@add",
    "data": {
        "platform": 1,
        "tags": "搞笑",
        "link": "",
        "account_id": "MzI3NDYxNTEyNg==",
        "account_code": "gyxc01{}".format(AutoNumber.autonumber()),
        "real_link": "",
        "avatar_url": "http://wx.qlogo.cn/mmhead/Q3auHgzwzM49ZVKJntz4ge8IzOaWibmBQUom2VWbgfnYAzFxbG7hYKQ/0",
        "name": "表情窝{}".format(AutoNumber.autonumber()),
        "desc": "表情窝唯一取图号，其它均为假冒。每日分享热门表情包，让你有用不完的图",
        "sex": "",
        "focus_num": "",
        "fans_num": "",
        "works_num": "",
        "like_num": "",
        "auth_info": "个人",
        "area": "北京",
        "is_grab": "",
        "comment_num": "",
        "repost_num": "",
        "level": "",
        "industry": "",
        "id": "",
        "cooperation_remark": "444",
        "recommend_remark": "333",
        "is_sign": "",
        "platform_name": "",
        "supplier_id": 66,
        "average_read_num": "111",
        "average_interaction_num": "222"
    }
}
        runner = HttpRequest().http_request(url, data, 'post', getattr(GetData, 'cookie'))
        try:
            self.assertEqual(200, runner.json()['code'])
        except BaseException as e:
            DoLog().info('执行用例错误{}！！！！！！'.format(e))
            raise e
        finally:
            DoLog().error('获取到的结果是{}'.format(runner.json()))

    # 新增微信抓取资源
    def test_addweixint(self):
        DoLog().info('开始执行用例{}:{}'.format("test_addweixint", "新增微信抓取资源{}".format(AutoNumber.autonumber())))
        url = Data().url
        data = {
    "api": "resource@add",
    "data": {
        "platform": 1,
        "tags": "搞笑",
        "link": "",
        "account_id": "MzI3NDYxNTEyNg==",
        "account_code": "gyxc01{}".format(AutoNumber.autonumber()),
        "real_link": "",
        "avatar_url": "http://wx.qlogo.cn/mmhead/Q3auHgzwzM49ZVKJntz4ge8IzOaWibmBQUom2VWbgfnYAzFxbG7hYKQ/0",
        "name": "表情窝{}".format(AutoNumber.autonumber()),
        "desc": "表情窝唯一取图号，其它均为假冒。每日分享热门表情包，让你有用不完的图",
        "sex": "",
        "focus_num": "",
        "fans_num": "",
        "works_num": "",
        "like_num": "",
        "auth_info": "个人",
        "area": "北京",
        "is_grab": 1,
        "comment_num": "",
        "repost_num": "",
        "level": "",
        "industry": "",
        "id": "",
        "cooperation_remark": "444",
        "recommend_remark": "333",
        "is_sign": "",
        "platform_name": "",
        "supplier_id": 66,
        "average_read_num": "111",
        "average_interaction_num": "222"
    }
}
        runner = HttpRequest().http_request(url, data, 'post', getattr(GetData, 'cookie'))
        try:
            self.assertEqual(200, runner.json()['code'])
        except BaseException as e:
            DoLog().info('执行用例错误{}！！！！！！'.format(e))
            raise e
        finally:
            DoLog().error('获取到的结果是{}'.format(runner.json()))

    # 新增微博未抓取资源
    def test_addweibof(self):
            DoLog().info('开始执行用例{}:{}'.format("test_addweixint", "新增微博未抓取资源{}".format(AutoNumber.autonumber())))
            url = Data().url
            data = {
    "api": "resource@add",
    "data": {
        "platform": 3,
        "tags": "搞笑",
        "link": "https://weibo.com/u/6338469755",
        "account_id": "6338469755",
        "account_code": "633846975{}".format(AutoNumber.autonumber()),
        "real_link": "https://weibo.com/u/6338469755",
        "avatar_url": "https://tvax2.sinaimg.cn/crop.0.0.829.829.180/006UXzx9ly8ggwirbk7wvj30n10n10tv.jpg?KID=imgbed,tva&Expires=1648300233&ssig=aMkun1YfL1",
        "name": "我的微博爱抽风{}".format(AutoNumber.autonumber()),
        "desc": "✨972e",
        "auth_info": "认证信息",
        "focus_num": 7,
        "fans_num": 3,
        "works_num": 0,
        "like_num": 0,
        "comment_num": 0,
        "repost_num": 0,
        "is_grab": "",
        "area": "北京",
        "average_read_num": "111",
        "average_interaction_num": "222",
        "supplier_id": 66,
        "recommend_remark": "333",
        "cooperation_remark": "444"
    }
}
            runner = HttpRequest().http_request(url, data, 'post', getattr(GetData, 'cookie'))
            try:
                self.assertEqual(200, runner.json()['code'])
            except BaseException as e:
                DoLog().info('执行用例错误{}！！！！！！'.format(e))
                raise e
            finally:
                DoLog().error('获取到的结果是{}'.format(runner.json()))

    # 新增微博抓取资源
    def test_addweibot(self):
            DoLog().info('开始执行用例{}:{}'.format("test_addweixint", "新增微博抓取资源{}".format(AutoNumber.autonumber())))
            url = Data().url
            data = {
    "api": "resource@add",
    "data": {
        "platform": 3,
        "tags": "搞笑",
        "link": "https://weibo.com/u/6338469755",
        "account_id": "6338469755",
        "account_code": "633846975{}".format(AutoNumber.autonumber()),
        "real_link": "https://weibo.com/u/6338469755",
        "avatar_url": "https://tvax2.sinaimg.cn/crop.0.0.829.829.180/006UXzx9ly8ggwirbk7wvj30n10n10tv.jpg?KID=imgbed,tva&Expires=1648300233&ssig=aMkun1YfL1",
        "name": "我的微博爱抽风{}".format(AutoNumber.autonumber()),
        "desc": "✨972e",
        "auth_info": "认证信息",
        "focus_num": 7,
        "fans_num": 3,
        "works_num": 0,
        "like_num": 0,
        "comment_num": 0,
        "repost_num": 0,
        "is_grab": 1,
        "area": "北京",
        "average_read_num": "111",
        "average_interaction_num": "222",
        "supplier_id": 66,
        "recommend_remark": "333",
        "cooperation_remark": "444"
    }
}
            runner = HttpRequest().http_request(url, data, 'post', getattr(GetData, 'cookie'))
            try:
                self.assertEqual(200, runner.json()['code'])
            except BaseException as e:
                DoLog().info('执行用例错误{}！！！！！！'.format(e))
                raise e
            finally:
                DoLog().error('获取到的结果是{}'.format(runner.json()))

    # 新增小红书未抓取资源
    def test_addxiaohongshuf(self):
        DoLog().info('开始执行用例{}:{}'.format("test_addweixint", "新增小红书未抓取资源{}".format(AutoNumber.autonumber())))
        url = Data().url
        data = {
    "api": "resource@add",
    "data": {
        "platform": 4,
        "tags": "搞笑",
        "link": "https://www.xiaohongshu.com/user/profile/5b3c224ee8ac2b5fc4c1ca4b?xhsshare=CopyLink&appuid=5b3c224ee8ac2b5fc4c1ca4b&apptime=1648103114",
        "account_id": "5b3c224ee8ac2b5fc4c1ca4b",
        "account_code": "94011692{}".format(AutoNumber.autonumber()),
        "real_link": "https://www.xiaohongshu.com/user/profile/5b3c224ee8ac2b5fc4c1ca4b?xhsshare=CopyLink&appuid=5b3c224ee8ac2b5fc4c1ca4b&apptime=1648103114",
        "avatar_url": "https://sns-avatar-qc.xhscdn.com/avatar/6211a38952b8759b2971d4c1.jpg?imageView2/2/w/360/format/webp",
        "name": "来自葫芦岛的执着凤爪{}".format(AutoNumber.autonumber()),
        "desc": "✨972e",
        "auth_info": "",
        "focus_num": 24,
        "fans_num": 7,
        "works_num": 0,
        "like_num": 0,
        "comment_num": "",
        "repost_num": "",
        "is_grab": "",
        "area": "缅甸",
        "average_read_num": "111",
        "average_interaction_num": "222",
        "supplier_id": 66,
        "recommend_remark": "333",
        "cooperation_remark": "444",
        "level": 1,
        "sex": "男",
        "industry": ""
    }
}
        runner = HttpRequest().http_request(url, data, 'post', getattr(GetData, 'cookie'))
        try:
            self.assertEqual(200, runner.json()['code'])
        except BaseException as e:
            DoLog().info('执行用例错误{}！！！！！！'.format(e))
            raise e
        finally:
            DoLog().error('获取到的结果是{}'.format(runner.json()))

    # 新增小红书抓取资源
    def test_addxiaohongshut(self):
        DoLog().info('开始执行用例{}:{}'.format("test_addweixint", "新增小红书抓取资源{}".format(AutoNumber.autonumber())))
        url = Data().url
        data = {
    "api": "resource@add",
    "data": {
        "platform": 4,
        "tags": "搞笑",
        "link": "https://www.xiaohongshu.com/user/profile/5b3c224ee8ac2b5fc4c1ca4b?xhsshare=CopyLink&appuid=5b3c224ee8ac2b5fc4c1ca4b&apptime=1648103114",
        "account_id": "5b3c224ee8ac2b5fc4c1ca4b",
        "account_code": "94011692{}".format(AutoNumber.autonumber()),
        "real_link": "https://www.xiaohongshu.com/user/profile/5b3c224ee8ac2b5fc4c1ca4b?xhsshare=CopyLink&appuid=5b3c224ee8ac2b5fc4c1ca4b&apptime=1648103114",
        "avatar_url": "https://sns-avatar-qc.xhscdn.com/avatar/6211a38952b8759b2971d4c1.jpg?imageView2/2/w/360/format/webp",
        "name": "来自葫芦岛的执着凤爪{}".format(AutoNumber.autonumber()),
        "desc": "✨972e",
        "auth_info": "",
        "focus_num": 24,
        "fans_num": 7,
        "works_num": 0,
        "like_num": 0,
        "comment_num": "",
        "repost_num": "",
        "is_grab": 1,
        "area": "缅甸",
        "average_read_num": "111",
        "average_interaction_num": "222",
        "supplier_id": 66,
        "recommend_remark": "333",
        "cooperation_remark": "444",
        "level": 1,
        "sex": "男",
        "industry": ""
    }
}
        runner = HttpRequest().http_request(url, data, 'post', getattr(GetData, 'cookie'))
        try:
            self.assertEqual(200, runner.json()['code'])
        except BaseException as e:
            DoLog().info('执行用例错误{}！！！！！！'.format(e))
            raise e
        finally:
            DoLog().error('获取到的结果是{}'.format(runner.json()))

    # 新增b站未抓取资源
    def test_addbzhanf(self):
            DoLog().info('开始执行用例{}:{}'.format("test_addweixint", "新增b站未抓取资源{}".format(AutoNumber.autonumber())))
            url = Data().url
            data = {
    "api": "resource@add",
    "data": {
        "platform": 6,
        "tags": "搞笑",
        "link": "https://b23.tv/q60qIxk",
        "account_id": "642694252",
        "account_code": "64269425{}".format(AutoNumber.autonumber()),
        "real_link": "https://space.bilibili.com/642694252?share_medium=iphone&share_plat=ios&share_session_id=E37BA245-F00E-4505-9919-76ABF8D65F67&share_source=COPY&share_tag=s_i&timestamp=1648103384&unique_k=q60qIxk",
        "avatar_url": "http://i1.hdslb.com/bfs/face/8efdd838f4bedd50a00309ca6f1a210f6ced55d3.jpg",
        "name": "我的bili爱抽风{}".format(AutoNumber.autonumber()),
        "desc": "这个就是个性签名",
        "auth_info": "认证信息",
        "focus_num": 1,
        "fans_num": 0,
        "works_num": "10",
        "like_num": "",
        "comment_num": "",
        "repost_num": "",
        "is_grab": "",
        "area": "",
        "average_read_num": "111",
        "average_interaction_num": "222",
        "supplier_id": 66,
        "recommend_remark": "333",
        "cooperation_remark": "444",
        "level": 2,
        "sex": "保密",
        "industry": "",
        "is_sign": 1
    }
}
            runner = HttpRequest().http_request(url, data, 'post', getattr(GetData, 'cookie'))
            try:
                self.assertEqual(200, runner.json()['code'])
            except BaseException as e:
                DoLog().info('执行用例错误{}！！！！！！'.format(e))
                raise e
            finally:
                DoLog().error('获取到的结果是{}'.format(runner.json()))

    # 新增b站未抓取资源
    def test_addbzhant(self):
        DoLog().info('开始执行用例{}:{}'.format("test_addbzhant", "新增b站抓取资源{}".format(AutoNumber.autonumber())))
        url = Data().url
        data = {
            "api": "resource@add",
            "data": {
                "platform": 6,
                "tags": "搞笑",
                "link": "https://b23.tv/q60qIxk",
                "account_id": "642694252",
                "account_code": "64269425{}".format(AutoNumber.autonumber()),
                "real_link": "https://space.bilibili.com/642694252?share_medium=iphone&share_plat=ios&share_session_id=E37BA245-F00E-4505-9919-76ABF8D65F67&share_source=COPY&share_tag=s_i&timestamp=1648103384&unique_k=q60qIxk",
                "avatar_url": "http://i1.hdslb.com/bfs/face/8efdd838f4bedd50a00309ca6f1a210f6ced55d3.jpg",
                "name": "我的bili爱抽风{}".format(AutoNumber.autonumber()),
                "desc": "这个就是个性签名",
                "auth_info": "认证信息",
                "focus_num": 1,
                "fans_num": 0,
                "works_num": "10",
                "like_num": "",
                "comment_num": "",
                "repost_num": "",
                "is_grab": "",
                "area": "",
                "average_read_num": "111",
                "average_interaction_num": "222",
                "supplier_id": 66,
                "recommend_remark": "333",
                "cooperation_remark": "444",
                "level": 2,
                "sex": "保密",
                "industry": "",
                "is_sign": 1
            }
        }
        runner = HttpRequest().http_request(url, data, 'post', getattr(GetData, 'cookie'))
        try:
            self.assertEqual(200, runner.json()['code'])
        except BaseException as e:
            DoLog().info('执行用例错误{}！！！！！！'.format(e))
            raise e
        finally:
            DoLog().error('获取到的结果是{}'.format(runner.json()))

    # 新增知乎未抓取资源
    def test_addzhihuf(self):
        DoLog().info('开始执行用例{}:{}'.format("test_addzhihuf", "新增知乎未抓取资源{}".format(AutoNumber.autonumber())))
        url = Data().url
        data = {
    "api": "resource@add",
    "data": {
        "platform": 7,
        "tags": "搞笑",
        "link": "www.zhihu.com",
        "account_id": "",
        "account_code": "1000{}".format(AutoNumber.autonumber()),
        "real_link": "",
        "avatar_url": "",
        "name": "知乎账号昵称{}".format(AutoNumber.autonumber()),
        "desc": "账号简介",
        "auth_info": "",
        "focus_num": "100",
        "fans_num": "",
        "works_num": "200",
        "like_num": "",
        "comment_num": "",
        "repost_num": "",
        "is_grab": "",
        "area": "北京",
        "average_read_num": "111",
        "average_interaction_num": "222",
        "supplier_id": 66,
        "recommend_remark": "333",
        "cooperation_remark": "444",
        "level": "",
        "sex": "",
        "industry": "所在行业",
        "is_sign": ""
    }
}
        runner = HttpRequest().http_request(url, data, 'post', getattr(GetData, 'cookie'))
        try:
            self.assertEqual(200, runner.json()['code'])
        except BaseException as e:
            DoLog().info('执行用例错误{}！！！！！！'.format(e))
            raise e
        finally:
            DoLog().error('获取到的结果是{}'.format(runner.json()))

    # 新增视频号未抓取资源
    def test_addshipinhaof(self):
            DoLog().info('开始执行用例{}:{}'.format("test_addshipinhaof", "新增视频号未抓取资源{}".format(AutoNumber.autonumber())))
            url = Data().url
            data = {
    "api": "resource@add",
    "data": {
        "platform": 2,
        "tags": "美妆",
        "link": "",
        "account_id": "v2_060000231003b20faec8c5e48d19c5d2cc07eb3db07767baa143d3d1d404298520186b9efcdd@finder",
        "account_code": "v2_060000231003b20faec8c5e48d19c5d2cc07eb3db07767baa143d3d1d404298520186b9efcdd@finder{}".format(AutoNumber.autonumber()),
        "real_link": "",
        "avatar_url": "http://wx.qlogo.cn/finderhead/Ib5852jAyb9Zylu7teeDic4Pn2yG8X2dD2ia8C6knP9wpo07w4cdPG4g/0",
        "name": "网易文案视频{}".format(AutoNumber.autonumber()),
        "desc": "如果爱是甘拜下风，我跪拜桑延。",
        "auth_info": "认证信息",
        "focus_num": "",
        "fans_num": "",
        "works_num": "",
        "like_num": "",
        "comment_num": "",
        "repost_num": "",
        "is_grab": "",
        "area": "北京",
        "average_read_num": "111",
        "average_interaction_num": "222",
        "supplier_id": 66,
        "recommend_remark": "333",
        "cooperation_remark": "444",
        "level": "",
        "sex": "男",
        "industry": "",
        "is_sign": ""
    }
}
            runner = HttpRequest().http_request(url, data, 'post', getattr(GetData, 'cookie'))
            try:
                self.assertEqual(200, runner.json()['code'])
            except BaseException as e:
                DoLog().info('执行用例错误{}！！！！！！'.format(e))
                raise e
            finally:
                DoLog().error('获取到的结果是{}'.format(runner.json()))

    # 新增视频号抓取资源
    def test_addshipinhaot(self):
            DoLog().info('开始执行用例{}:{}'.format("test_addshipinhaot", "新增视频号抓取资源{}".format(AutoNumber.autonumber())))
            url = Data().url
            data = {
    "api": "resource@add",
    "data": {
        "platform": 2,
        "tags": "美妆",
        "link": "",
        "account_id": "v2_060000231003b20faec8c5e48d19c5d2cc07eb3db07767baa143d3d1d404298520186b9efcdd@finder",
        "account_code": "v2_060000231003b20faec8c5e48d19c5d2cc07eb3db07767baa143d3d1d404298520186b9efcdd@finder{}".format(AutoNumber.autonumber()),
        "real_link": "",
        "avatar_url": "http://wx.qlogo.cn/finderhead/Ib5852jAyb9Zylu7teeDic4Pn2yG8X2dD2ia8C6knP9wpo07w4cdPG4g/0",
        "name": "网易文案视频{}".format(AutoNumber.autonumber()),
        "desc": "如果爱是甘拜下风，我跪拜桑延。",
        "auth_info": "认证信息",
        "focus_num": "",
        "fans_num": "",
        "works_num": "",
        "like_num": "",
        "comment_num": "",
        "repost_num": "",
        "is_grab": 1,
        "area": "北京",
        "average_read_num": "111",
        "average_interaction_num": "222",
        "supplier_id": 66,
        "recommend_remark": "333",
        "cooperation_remark": "444",
        "level": "",
        "sex": "男",
        "industry": "",
        "is_sign": ""
    }
}
            runner = HttpRequest().http_request(url, data, 'post', getattr(GetData, 'cookie'))
            try:
                self.assertEqual(200, runner.json()['code'])
            except BaseException as e:
                DoLog().info('执行用例错误{}！！！！！！'.format(e))
                raise e
            finally:
                DoLog().error('获取到的结果是{}'.format(runner.json()))

    # 新增快手未抓取资源
    def test_addkuaishouf(self):
        DoLog().info('开始执行用例{}:{}'.format("test_addweixint", "新增快手未抓取资源{}".format(AutoNumber.autonumber())))
        url = Data().url
        data = {
    "api": "resource@add",
    "data": {
        "platform": 10,
        "tags": "搞笑",
        "link": "https://v.kuaishou.com/giUur8",
        "account_id": "690465835",
        "account_code": "z2223647{}".format(AutoNumber.autonumber()),
        "real_link": "https://c.kuaishou.com/fw/user/z22236470?fid=690465835&cc=share_copylink&followRefer=151&shareMethod=TOKEN&kpn=KUAISHOU&subBiz=PROFILE&shareId=16844628932344&shareToken=X-SmVss75Ijn1NR&shareMode=APP&originShareId=16844628932344&appType=1&shareObjectId=690465835&shareUrlOpened=0&timestamp=1648104754143",
        "avatar_url": "https://p2.a.yximgs.com/uhead/AB/2022/02/22/19/BMjAyMjAyMjIxOTE0NTFfNjkwNDY1ODM1XzFfaGQ5NjVfMzcx_s.jpg",
        "name": "樱樱子鸭{}".format(AutoNumber.autonumber()),
        "desc": "这就是个人介绍吧o",
        "auth_info": "认证信息",
        "focus_num": 2,
        "fans_num": 18,
        "works_num": 15,
        "like_num": "100",
        "comment_num": "",
        "repost_num": "",
        "is_grab": "",
        "area": "北京",
        "average_read_num": "111",
        "average_interaction_num": "222",
        "supplier_id": 66,
        "recommend_remark": "333",
        "cooperation_remark": "444",
        "level": "",
        "sex": "女",
        "industry": "",
        "is_sign": ""
    }
}
        runner = HttpRequest().http_request(url, data, 'post', getattr(GetData, 'cookie'))
        try:
            self.assertEqual(200, runner.json()['code'])
        except BaseException as e:
            DoLog().info('执行用例错误{}！！！！！！'.format(e))
            raise e
        finally:
            DoLog().error('获取到的结果是{}'.format(runner.json()))

    # 新增快手抓取资源
    def test_addkuaishout(self):
        DoLog().info('开始执行用例{}:{}'.format("test_addkuaishout", "新增快手抓取资源{}".format(AutoNumber.autonumber())))
        url = Data().url
        data = {
    "api": "resource@add",
    "data": {
        "platform": 10,
        "tags": "搞笑",
        "link": "https://v.kuaishou.com/giUur8",
        "account_id": "690465835",
        "account_code": "z2223647{}".format(AutoNumber.autonumber()),
        "real_link": "https://c.kuaishou.com/fw/user/z22236470?fid=690465835&cc=share_copylink&followRefer=151&shareMethod=TOKEN&kpn=KUAISHOU&subBiz=PROFILE&shareId=16844628932344&shareToken=X-SmVss75Ijn1NR&shareMode=APP&originShareId=16844628932344&appType=1&shareObjectId=690465835&shareUrlOpened=0&timestamp=1648104754143",
        "avatar_url": "https://p2.a.yximgs.com/uhead/AB/2022/02/22/19/BMjAyMjAyMjIxOTE0NTFfNjkwNDY1ODM1XzFfaGQ5NjVfMzcx_s.jpg",
        "name": "樱樱子鸭{}".format(AutoNumber.autonumber()),
        "desc": "这就是个人介绍吧o",
        "auth_info": "认证信息",
        "focus_num": 2,
        "fans_num": 18,
        "works_num": 15,
        "like_num": "100",
        "comment_num": "",
        "repost_num": "",
        "is_grab": 1,
        "area": "北京",
        "average_read_num": "111",
        "average_interaction_num": "222",
        "supplier_id": 66,
        "recommend_remark": "333",
        "cooperation_remark": "444",
        "level": "",
        "sex": "女",
        "industry": "",
        "is_sign": ""
    }
}
        runner = HttpRequest().http_request(url, data, 'post', getattr(GetData, 'cookie'))
        try:
            self.assertEqual(200, runner.json()['code'])
        except BaseException as e:
            DoLog().info('执行用例错误{}！！！！！！'.format(e))
            raise e
        finally:
            DoLog().error('获取到的结果是{}'.format(runner.json()))

    # 新增其他资源
    def test_addqita(self):
            DoLog().info('开始执行用例{}:{}'.format("test_addqita", "新增其他资源{}".format(AutoNumber.autonumber())))
            url = Data().url
            data = {
                "api": "resource@add",
                "data": {
                    "platform": 9,
                    "tags": "时尚",
                    "platform_name": "平台名称",
                    "link": "www.baidu.com/2",
                    "name": "账号昵称{}".format(AutoNumber.autonumber()),
                    "account_code": "000{}".format(AutoNumber.autonumber()),
                    "desc": "账号简介",
                    "industry": "所在行业",
                    "focus_num": "6",
                    "works_num": "4",
                    "area": "北京",
                    "average_read_num": "11",
                    "average_interaction_num": "22",
                    "is_grab": 2,
                    "supplier_id": 66,
                    "recommend_remark": "33",
                    "cooperation_remark": "44"
                }
            }
            runner = HttpRequest().http_request(url, data, 'post', getattr(GetData, 'cookie'))
            try:
                self.assertEqual(200, runner.json()['code'])
            except BaseException as e:
                DoLog().info('执行用例错误{}！！！！！！'.format(e))
                raise e
            finally:
                DoLog().error('获取到的结果是{}'.format(runner.json()))

    # 新增服务资源
    def test_addfuwu(self):
            DoLog().info('开始执行用例{}:{}'.format("test_addqita", "新增服务资源{}".format(AutoNumber.autonumber())))
            url = Data().url
            data = {
    "api": "resource@add",
    "data": {
        "platform": 8,
        "tags": "搞笑",
        "link": "",
        "account_id": "",
        "account_code": "10000{}".format(AutoNumber.autonumber()),
        "real_link": "",
        "avatar_url": "",
        "name": "服务账号昵称{}".format(AutoNumber.autonumber()),
        "desc": "账号简介",
        "auth_info": "",
        "focus_num": "",
        "fans_num": "",
        "works_num": "",
        "like_num": "",
        "comment_num": "",
        "repost_num": "",
        "is_grab": 2,
        "area": "",
        "average_read_num": "111",
        "average_interaction_num": "222",
        "supplier_id": 66,
        "recommend_remark": "333",
        "cooperation_remark": "444",
        "level": "",
        "sex": "",
        "industry": "所在行业",
        "is_sign": ""
    }
}
            runner = HttpRequest().http_request(url, data, 'post', getattr(GetData, 'cookie'))
            try:
                self.assertEqual(200, runner.json()['code'])
            except BaseException as e:
                DoLog().info('执行用例错误{}！！！！！！'.format(e))
                raise e
            finally:
                DoLog().error('获取到的结果是{}'.format(runner.json()))

    def tearDown(self) -> None:
        pass

if __name__ == '__main__':
    unittest.main()

