import requests
from bs4 import BeautifulSoup
import time
import ssl


def get_json(url, num):
    """
    从网页获取JSON,使用POST请求,加上头部信息
    """

    my_headers = {  
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4)'
                          ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',
            'Host': 'www.lagou.com',
            'Referer': 'https://www.lagou.com/jobs/list_%E5%8D%8E%E4%B8%BA?labelWords=&fromSearch=true&suginput=',
            'X-Anit-Forge-Code': '0',
            'X-Anit-Forge-Token': 'None',  
            'X-Requested-With': 'XMLHttpRequest',
            'Cookie': 'user_trace_token=20190524105411-1c47ced6-fe00-4f1b-9697-49f31052f104; Hm_lvt_4233e74dff0ae5bd0a'
                      '3d81c6ccf756e6=1558666452; _ga=GA1.2.1997636938.1558666452; LGUID=20190524105412-35887f3d-7dcf-'
                      '11e9-a6d2-525400f775ce; _gid=GA1.2.56700240.1558666499; sensorsdata2015jssdkcross=%7B%22distinc'
                      't_id%22%3A%2216ae7c3553f5b4-0e0403c499594-37667003-1296000-16ae7c35540261%22%2C%22%24device_id%'
                      '22%3A%2216ae7c3553f5b4-0e0403c499594-37667003-1296000-16ae7c35540261%22%7D; sajssdk_2015_cross_'
                      'new_user=1; LG_LOGIN_USER_ID=7261689333a914ab9736f91ea5fda1ed363fabe4c8e498ad; LG_HAS_LOGIN=1; '
                      '_putrc=4CECC42D9DE4879C; JSESSIONID=ABAAABAAAIAACBIC96DA553CFAADE97BEDFBA2D2F0EF010; login=true'
                      '; unick=%E9%92%9F%E5%8F%8B%E8%AF%9A; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedM'
                      'yPublish=1; hasDeliver=19; gate_login_token=dda8796d4b26b73d9a45ab7b05f17dbe770ee52692fd46cd; i'
                      'ndex_location_city=%E4%B8%8A%E6%B5%B7; TG-TRACK-CODE=index_search; X_HTTP_TOKEN=a1435d0529c8b46'
                      'f0309668551f895c9e47b228d81; _gat=1; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1558669030; LGSID'
                      '=20190524113710-36527af0-7dd5-11e9-a11a-5254005c3644; PRE_UTM=; PRE_HOST=; PRE_SITE=https%3A%2F'
                      '%2Fwww.lagou.com%2F; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_%25E5%258D%258E%25E4%25'
                      'B8%25BA%3FlabelWords%3D%26fromSearch%3Dtrue%26suginput%3D; LGRID=20190524113710-36527d1d-7dd5-1'
                      '1e9-a11a-5254005c3644; SEARCH_ID=01349bd1c64643278b0ae9519a622731'
            }  

    my_data = {  
            'first': 'true',  
            'pn': num,
            'kd': '华为'}

    res = requests.post(url, headers=my_headers, data=my_data)
    res.raise_for_status()  
    res.encoding = 'utf-8'  
    # 得到包含职位信息的字典  
    page = res.json()  
    return page  


url = "https://www.lagou.com/jobs/positionAjax.json?city=%E4%B8%8A%E6%B5%B7&needAddtionalResult=false"
print(get_json(url, 1))

