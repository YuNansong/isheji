import requests


def test_api_template_search():
    '''模板搜索接口'''
    url = 'https://isheji.com/api/template/search/'
    head = {
        "api-key": "624d8c05d12a4",
        "x-timestamp": "1647398451",
        "x-signature": "MIQOtVdCAErjvIn4CMIXsm/lUZg="
    }
    res = requests.request(method='get', url=url, headers=head)
    return res


# print(test_api_template_search().json())


def test_api_template_class():
    '''返回模板中心搜索需要的：场景、用途、风格'''
    url = 'https://isheji.com/api/template/class/'
    head = {
        "api-key": "624d8c05d12a4",
        "x-timestamp": "1647398451",
        "x-signature": "IAZRP8LH34VrAu9ciDgk4LjYr2c="
    }
    res = requests.request(method='get', url=url, headers=head)
    return res


# print(test_api_template_class().json())


def test_api_special_newdetail():
    '''接口返回最新专题数据，不按照标签分组返回，带分页'''
    url = 'https://isheji.com/api/special/newdetail/'
    head = {
        "api-key": "624d8c05d12a4",
        "x-timestamp": "1647398451",
        "x-signature": "a37UaEEP9nnR2EZefZasqht23sw="
    }
    res = requests.request(method='get', url=url, headers=head)
    return res


# print(test_api_special_newdetail().json())


def test_api_special_list():
    '''获取爱设计上架中的专题列表'''
    url = 'https://isheji.com/api/special/list/'
    head = {
        "api-key": "624d8c05d12a4",
        "x-timestamp": "1647398451",
        "x-signature": "pqXXEc2WS51xgkv4jdunrkxE/YE="
    }
    res = requests.request(method='get', url=url, headers=head)
    return res

# print(test_api_special_list().json())
# print(test_api_special_list().json()['data'][0]['id'])


def test_api_special_detail():
    '''通过专题 id（专题列表接口专题主 id）获取按标签分组返回模板数据（不带分页）'''
    url = 'https://isheji.com/api/special/detail/'
    body = {"sid": test_api_special_list().json()['data'][0]['id']}
    # print(test_api_special_list().json()['data'][0]['id'])
    head = {
        "api-key": "624d8c05d12a4",
        "x-timestamp": "1647398451",
        "x-signature": "u+Rr5e/2fHOuKSutW112AXHJ4mc="
    }
    res = requests.request(method='get', url=url, params=body, headers=head)
    return res


# print(test_api_special_detail().json())


def test_api_auth_code():
    '''获取用户授权码'''
    url = 'https://isheji.com/api/auth/code/'
    body = {"uid": 2222}
    head = {
        "api-key": "624d8c05d12a4",
        "x-timestamp": "1647398451",
        "x-signature": "2+X9D/q8lhqltU+dLVzmg/PpJd4="
    }
    res = requests.request(method='get', url=url, params=body, headers=head)
    return res

# print(test_api_auth_code().json())


def rang_lst():
    lst = [test_api_template_search, test_api_template_class, test_api_special_newdetail, test_api_special_detail,
           test_api_special_list, test_api_auth_code]
    for i in lst:
        response = i().json()
        print(response)


if __name__ == '__main__':
    rang_lst()
