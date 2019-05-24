import requests
import time
import json
import random


def main():
    url_start = "https://www.lagou.com/jobs/list_华为?labelWords=&fromSearch=true&suginput="
    url_parse = "https://www.lagou.com/jobs/positionAjax.json?px=default&needAddtionalResult=false"
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Referer': 'https://www.lagou.com/jobs/list_%E5%8D%8E%E4%B8%BA?px=default&city=%E5%85%A8%E5%9B%BD',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }
    counter = 1
    with open("huawei_positions_on_lagou.txt", "w", encoding="utf-8") as record:
        for x in range(1, 18):
            data = {
                'first': 'true',
                'pn': str(x),
                'kd': '华为'
                    }
            s = requests.Session()
            s.get(url_start, headers=headers, timeout=3)  # 请求首页获取cookies
            cookie = s.cookies  # 为此次获取的cookies
            response = s.post(url_parse, data=data, headers=headers, cookies=cookie, timeout=3)  # 获取此次文本
            print("get from page %d" % x)
            time.sleep(10 * random.random())
            response.encoding = response.apparent_encoding
            text = json.loads(response.text)
            info = text["content"]["positionResult"]["result"]
            for i in info:
                record.write("==========职位%d=========== \n" % counter)
                record.write("工作地点:"+i["city"]+"\n")
                stationname = i["stationname"]
                if not stationname:
                    stationname = "无"
                record.write("地区位置:"+stationname+"\n")
                companyFullName = i["companyFullName"]
                record.write("公司名称:"+companyFullName+"\n")
                positionName = i["positionName"]
                record.write("岗位名称:"+positionName+"\n")
                salary = i["salary"]
                record.write("薪酬待遇:"+salary+"\n")
                # print(i["companySize"])
                # companySize = i["companySize"]
                skillLables = i["skillLables"]
                if len(skillLables) == 0:
                    skillLables = "无"
                record.write("技能标签:"+str(skillLables)+"\n")
                createTime = i["createTime"]
                record.write("创建时间:"+createTime+"\n")
                # print(i["district"])
                # district = i["district"]
                workYear = i["workYear"]
                record.write("工作年限: "+workYear+"\n")
                education = i["education"]
                record.write("学历要求:"+education+"\n")
                counter += 1


def transform_csv():
    counter = 1
    with open("huawei_positions_on_lagou.txt", "r", encoding="utf-8") as reader, \
         open("csv_format.txt", "w", encoding="utf-8") as writer:
        first_line = "职位编号,工作地点,地区,公司名称,岗位名称,薪酬待遇,技能标签,创建时间,工作年限,学历要求"
        writer.write(first_line+"\n")
        for line in reader.readlines():
            if line.startswith("="):
                writer.write(str(counter)+",")
            elif line.startswith("学历要求"):
                writer.write(line.split(":")[1])
                counter += 1
            else:
                s = line.split(":")[1]
                s = s.replace("，", " ").replace(",", " ")
                writer.write(s.replace("\n", "")+",")


if __name__ == '__main__':
    # main()
    transform_csv()
