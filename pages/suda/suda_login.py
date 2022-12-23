import requests


def get_token():
    url = 'https://www.isheji.com/api/oauth2/access_token'
    head = {
        "api_secret": "WtWLlsQi4LCF4G2yw4sWYGZVfuOszicH",
        "api_key": "61b87025c1e51",
        "grant_type": "client_credentials"
    }
    rea = requests.request(method='post', url=url, json=head)
    rea = rea.json()
    token = rea['data']['access_token']
    return token


token = get_token()
# print(token)


def login_suda():
    url = 'https://www.isheji.com/api/suda/iframe/login'
    head = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + token,
        # "Authorization": "Bearer GvS68in9ml7c5FqbwbIBSRRCweiBisfAmHE7vgYK",
        "api-key": "61b87025c1e51"
    }
    body = {
        "qid": "123"
    }
    res = requests.request(method='post', url=url, headers=head, json=body)
    sign = res.json()
    sign = sign['data']['sign']
    # print("-----",sign)
    return sign

sign = login_suda()


# print(type(sign))
