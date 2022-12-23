import requests, json,time
import urllib3
from common.path import data_position
from common.getYaml import url
from common.readLog import Log
from common.sendDingTalk import SendDingTalk


class Interface:
    log = Log(__name__)
    logger = log.getLog()

    def getToken(self):
        file = data_position + "/cookie.txt"
        with open(file, 'r') as f:
            cookieVlaue = f.read()
            str = cookieVlaue.index("%22ey")
            str2 = cookieVlaue.index("%22%2C%22refresh_token")
            test_str = cookieVlaue[str+3:str2]
        return test_str

    def getQiyeToken(self):
        file = data_position + "/cookie.txt"
        with open(file, 'r') as f:
            cookieVlaue = f.read()
            str =cookieVlaue.index("%22%2C%22refresh_token")
            test_str = cookieVlaue[37:str]
        print("cookie:",test_str)
        return test_str

    def getUserInfo(self):
        userInfo = ""
        tokenValue = self.getToken()
        headers = {
            "authorization": "Bearer " + tokenValue
        }
        urlInfo = url['url']['testUrl']
        # url = "https://misheji.wxbjq.top/get/personal/info"
        interfaceUrl = urlInfo + "/get/personal/info"
        user = requests.request('post', url=interfaceUrl, headers=headers).text
        time.sleep(2)
        userInfo = json.loads(user)
        self.logger.info("Interface：请求info接口后解析json获取到的值:%s" % userInfo)
        login_status = userInfo['status']
        self.logger.info("接口返回状态值:%d" % login_status)
        if login_status == '0':
            SendDingTalk().sendDingTalkMsg("请求用户信息接口返回状态码为0")
            userInfo == ""
        else:
            print(userInfo)
            return userInfo

    # 获取url 状态码
    def getUrlStatus(testUrl):
        tokenValue = Interface().getToken()
        headers = {
            "authorization": "Bearer " + tokenValue
        }
        urllib3.disable_warnings()
        result = requests.request('get', url=testUrl, headers=headers, verify=False).status_code
        return result

    def get_ck(self):
        auth = Interface().getToken()
        url = 'https://sc.isheji.com/api/user/info'
        head = {
            "Content-Type": "application/json",
            "authorization": "Bearer " + auth
        }
        urllib3.disable_warnings()
        res = requests.request(method='get', url=url, headers=head)
        value = res.json()['data']['identity']
        return value
    # 企业url状态
    def get_qiye_url_status(testUrl):
        auth = Interface().getQiyeToken()
        head = {
            "Content-Type": "application/json",
            "token": "Bearer " + auth
        }
        urllib3.disable_warnings()
        result = requests.request('get', url=testUrl, headers=head, verify=False).status_code
        return result

    # 获取团队成员
    def get_temp_member_num(self):
        urlInfo = url['url']['testUrl']
        try:
            apiUrl = urlInfo+"/api/user/info"
            member_num = []
            auth = Interface().getQiyeToken()
            head = {
                "Content-Type": "application/json",
                "authorization": "Bearer " + auth
            }
            urllib3.disable_warnings()
            res = requests.request(method='get', url=apiUrl, headers=head).text
            print("res-->",res)
            data = json.loads(res)
            current_team_members = data['data']['current_team_members'] # 团队最大成员数
            current_team_members_canuse = data['data']['current_team_members_canuse'] # 团队剩余成语数
            member_num.append(current_team_members)
            member_num.append(current_team_members_canuse)
            return member_num
        except:
            SendDingTalk().sendDingTalkMsg("/api/user/info接口数据获取失败")
            self.logger.info("/api/user/info接口数据获取失败")

# status_code = Interface.getUrlStatus("https://www.isheji.com/")
# print(status_code)
# SendDingTalk().sendDingTalkMsg("https://idea.isheji.com/"+"返回状态码为:"+str(status_code))
#
# user = []
# for i in range(0,20):
#     aa = Interface().getUserInfo()
#     print(aa)
#     is_vip = aa['data']['is_vip']
#     print(is_vip)
# vip_type = aa['data']['vip_type']
# company_vip_end_time = aa['data']['company_vip_end_time']
# company_vip_level = aa['data']['company_vip_level']
# user.append(is_vip)  # 是否会员
# user.append(vip_type)  # 普通/终身
# user.append(company_vip_end_time)  # 企业会员到期日期
# user.append(company_vip_level)  # 企业会员等级
# print(company_vip_level)
# print(type(company_vip_level))
# print("------",user[3])


    # def a(self):
    #     url = "https://login.isheji.com/api/login/mobile"
    #
    #     payload={'mobile': '16619783425',
    #              'password': '111111',
    #              'register_type': '1',
    #              'utm_type': 'BD渠道',
    #              'utm_source': 'BJQ',
    #              'utm_plan': 'sy',
    #              'utm_page': 'xmtpt',
    #              'utm_unit': 'tpbj',
    #              'utm_keyword': '47952'
    #             }
        # headers = {
        #     'Cookie': 'authorization=%7B%22access_token%22%3A%22eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJVc2VySWQiOjU1MzM4MywiZXhwIjoxNjQ4MjY1MTUzLCJpc3MiOiIxNjYxOTc4MzQyNSJ9.E_F2ByTl-v_gggSb9QwmkJYOhKrNQUZyq2aDWzXlanM%22%2C%22refresh_token%22%3A%22%22%2C%22access_token_life_time%22%3A86400%2C%22refresh_token_life_time%22%3A0%2C%22access_token_expires_at%22%3A%222022-03-26T11%3A25%3A53.563823438%2B08%3A00%22%2C%22refresh_token_expires_at%22%3A%220001-01-01T00%3A00%3A00Z%22%7D'
        # }
        # response = requests.request("POST", url,  data=payload)
        #print(response.cookies.values())
        # print(response.text)
        # info = json.loads(response.text)
        # print(info['data']['token']['access_token'])
        # token = info['data']['token']['access_token']
        # testUrl = "https://www.isheji.com/get/personal/info"
        # headers = {
        #     'Authorization': "Bearer"+" "+token
        # }
        #response = requests.request("POST", url=testUrl,  headers=headers)
        #print(response.text)

#     def getToken(self):
#         file = data_position+"/cookie.txt"
#         with open(file,'r') as f:
#             cookieVlaue = f.read()
#             str = cookieVlaue.index("{%22access_token%22:%22")
#             # str = cookieVlaue.split(";")[3]
#             # print(cookieVlaue.split(";")[3])
#             print(str)
#             test_str = cookieVlaue[str:str+176]
#             print(test_str)
#             print(test_str[23:])

# if __name__ == '__main__':
#     a = Interface().getUserInfo()
#     print(a)
