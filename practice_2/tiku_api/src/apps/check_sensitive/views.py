from __future__ import unicode_literals
from django.views.decorators.csrf import csrf_exempt
from apps.check_sensitive.word import word
from libs import aft_http
from libs.aft_http import Status
import json
import re
import logging

LOGGING_FORMAT = '%(asctime)-15s:%(levelname)s: %(message)s'
logging.basicConfig(format=LOGGING_FORMAT, level=logging.INFO,
                    filename='apps/check_sensitive/sensitive.log', filemode='a',)


def bianli(set_datas,datas,html_data):
    list1 = []
    for data in datas:
        if data in set_datas:
            for  word_data in word.get(data):
                if word_data in html_data:
                    list1.append(word_data)
    return list1

@csrf_exempt
def sensitive(request):
    '''
    用来检查敏感词
    :param request:
    :return:
    '''
    if request.method=="POST":
        list1=[]
        try:
            html_data = json.loads(request.POST.get('data'))
            data = re.findall("[\u4e00-\u9fa5A-Za-z0-9]", html_data)
            set_datas=set(data)
            data=''.join(data)
            if not data:
                data = {
                    'key': list1
                    }
                res = aft_http.return_json_response_meta(
                    Status.SUCCESS,
                    'success', data)
                return res
            if len(set_datas) <=len(word):
                list1=bianli(word,set_datas,html_data)
                data={
                    'key':list1
                    }
                res = aft_http.return_json_response_meta(
                    Status.SUCCESS,
                    'success', data)
                return res
            else:
                list1 = bianli(set_datas, word, html_data)
                data = {
                    'key': list1
                    }
                res = aft_http.return_json_response_meta(
                    Status.SUCCESS,
                    'success', data)
                return res


        except Exception as a:
            logging.error(a)
    else:
        res=aft_http.return_json_response_meta(Status.INVALID_PARAMS,'error')
        return  res
