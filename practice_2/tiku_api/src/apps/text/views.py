from __future__ import unicode_literals
from django.views.decorators.csrf import csrf_exempt
from tiku_lib.text import get_latex_text_for_search, get_pure_text_for_search, \
    get_pure_text_for_duplicate
from libs import aft_http
from libs.aft_http import Status


@csrf_exempt
def puretext(request):

    if request.method=="POST":
        try:
            datas={}
            data = request.POST.get('html', '')
            '''
            由html获取带有latex信息的纯文本
            :param request:
            :return:
            '''
            dd= get_latex_text_for_search(data)
            datas['text_latex']=dd
            '''
            由html获取纯文本(不带有latex信息)
            :param request:
            :return: 纯文本
            '''
            dd = get_pure_text_for_search(data)
            datas['text'] = dd
            '''
            由html获取纯文本(不带标点，不带空格，不带latex信息)
            :param request:html
            :return: 纯文本
            '''
            dd = get_pure_text_for_duplicate(data)
            datas['text_pure'] = dd
            responcse = aft_http.return_json_response_meta(Status.SUCCESS,
                                                           'success',datas)
            return responcse
        except Exception as a:
            print(a)
    responcse=aft_http.return_json_response_meta(Status.INVALID_PARAMS,'error')
    return  responcse

