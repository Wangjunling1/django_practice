# -*- coding: UTF-8 -*-

import requests,json,pymysql
from bs4 import BeautifulSoup


def text_post(data):
    url = " http://172.16.0.7:10086/apis/v1/text/puretext"
    data = {"html": data}
    r = requests.post(url, data=data)
    da=r.text

    return da

def examine_post(data):
    url = "http://172.16.0.7:10086/apis/v1/examine/checkout"
    data = {"data": json.dumps(data,ensure_ascii=False)}
    r = requests.post(url, data=data)
    da=r.text

    return da

def detection(data):
    url = "http://127.0.0.1:8000/apis/v1/check_repeat/detection"
    data = {"data": json.dumps(data,ensure_ascii=False)}
    r = requests.post(url, data=data)
    da=r.text

    return da
def sensitive(data=None):
    url = "http://172.16.0.7:10086/apis/v1/check_sensitive/sensitive"
    data = {"data": json.dumps(data,ensure_ascii=False)}
    r = requests.post(url, data=data)
    da=r.text

    return da
if __name__ == '__main__':
    #一
    # html='<span class="afanti-latex"><table class="aft_option_wrapper" style="width: 100%;"><tbody class="measureRoot"><tr><td class="aft_option" data="A"><i class="aft_option_value">A.</i><div class="aft_option_content"><img src="http://qimg.afanti100.com/data/image/question_image/104/8a2ae3ee10aada99693e5b9f48612da2.png" zmtype="small"/></div></td></tr><tr><td class="aft_option" data="B"><i class="aft_option_value">B.</i><div class="aft_option_content"><img src="http://qimg.afanti100.com/data/image/question_image/104/d6e6f6c8bdb0ac2bac10042a6647d7c5.png" zmtype="small"/></div></td></tr><tr><td class="aft_option" data="C"><i class="aft_option_value">C.</i><div class="aft_option_content"><img src="http://qimg.afanti100.com/data/image/question_image/104/927d5acc3cc04c7a972addba7d7024d3.png" zmtype="small"/></div></td></tr></tbody></table></span>'
    # print(text_post(html))

    #二
    # data = {'question_html': '<p>元素<span class="dG cT " tabindex="0" style="font-size: 121%;">',
    #         'option_html': '',
    #         'answer_all_html': '<div class="aft_question_wrapper">略',
    #         'jieda': '<div class="aft_question_wrapper">',
    #         'fenxi': '<p>元素<img src="http://qimg.afanti100.com/data/image/question_image/104/590e33fa3872d89672b1c91.png"><span class="dG cT " tabindex="0" style="font-size: 121%;">',
    #         'dianping': '<p><span class="dG cT " tabindex="0" style="font-size: 121%;"></span></p>',
    #         'flag': 0}
    # print(examine_post(data))

    #三
    data = {
        'md5': 'xxxxx',
        'source': '3',
        'spider_url': 'xxxxx',
        'question_id': '1'
    }

    print(detection(data))
    # print(sensitive('你是王一个AV大共产党qwetyuiopopasghfjlkxlasmdqwgongheX夜激情'))
