from __future__ import unicode_literals
from django.views.decorators.csrf import csrf_exempt
from tiku_lib.text import get_latex_text_for_search, get_pure_text_for_search, \
    get_pure_text_for_duplicate
from libs import aft_http
from libs.aft_http import Status
import json,requests
from bs4 import BeautifulSoup

def xml(html):
    soup = BeautifulSoup(html, 'lxml')
    return str(soup).replace('<html><body>', '').replace('</body></html>', '')

def get_img(html_string):
    soup = BeautifulSoup(html_string, 'lxml')
    img_list = soup.find_all('img')
    img_list = [img.get('src') for img in img_list]
    for image_url in img_list:
        response = requests.head(image_url)
        if response.status_code!=200:
            return True

@csrf_exempt
def checkout(request):

    if request.method=="POST":
        try:

            i={}
            i['flag']=[]

            data=json.loads(request.POST.get('data',''))

            option_html_ = get_pure_text_for_duplicate(data.get('option_html',''))
            answer_all_html_ = get_pure_text_for_duplicate(data.get('answer_all_html',''))
            jieda_ = get_pure_text_for_duplicate(data.get('jieda',''))
            fenxi_ = get_pure_text_for_duplicate(data.get('fenxi',''))
            dianping_ = get_pure_text_for_duplicate(data.get('dianping',''))

            '''判读是否只有题干'''
            if len(option_html_)>0 or len(answer_all_html_)>0 or  len(jieda_)>0 or len(fenxi_)>0 or len(dianping_)>0:

                str_html = xml(data.get('question_html',''))
                if len(data.get('question_html','')) < len(str_html):
                    i['question_html'] = str_html
                    i['flag'].append(10008)

                '======以下为判断各字段是否只有标签或者答案和解析为略======='
                '''判断选项是否为空'''

                if len(option_html_)<2 and len(data.get('option_html',''))!=0:
                    i['option_html']=''
                    i['flag'].append(10004)
                else:
                    str_html = xml(data.get('option_html',''))
                    if len(data.get('option_html','')) < len(str_html):
                        i['option_html'] = str_html
                        i['flag'].append(10008)


                '''判断答案是否只有标签或者为略'''
                if len(answer_all_html_)<=1 and '略' in answer_all_html_:
                    i['answer_all_html']=''
                    i['flag'].append(10004)
                elif len(answer_all_html_)==0:
                    i['answer_all_html'] = ''
                    i['flag'].append(10004)
                else:
                    str_html = xml(data.get('answer_all_html',''))
                    if len(data.get('answer_all_html','')) < len(str_html):
                        i['answer_all_html'] = str_html
                        i['flag'].append(10008)

                '''判断是否解答、分析是否为空'''

                if len(jieda_)<1 or len(fenxi_)<1 :

                    if len(jieda_)<=1 and len(data.get('jieda',''))!=0:
                        i['jieda']=''
                        i['flag'].append(10004)
                    else:
                        str_html = xml(data.get('jieda',''))
                        if len(data.get('jieda','')) < len(str_html):
                            i['jieda'] = str_html
                            i['flag'].append(10008)


                    if len(fenxi_)<=1 and len(data.get('fenxi',''))!=0:
                        i['fenxi']=''
                        i['flag'].append(10004)
                    else:
                        str_html = xml(data.get('fenxi',''))
                        if len(data.get('fenxi','')) < len(str_html):
                            i['fenxi'] = str_html
                            i['flag'].append(10008)

                    if len(fenxi_)==0 and len(jieda_)==0:
                        i['flag'].append(10009)

                '''检查点评是否为空'''
                if len(dianping_)<1 and len(data.get('dianping',''))!=0 :
                    i['dianping']=''
                    i['flag'].append(10004)
                else:
                    str_html = xml(data.get('dianping',''))
                    if len(data.get('dianping','')) < len(str_html):
                        i['dianping'] = str_html
                        i['flag'].append(10008)

                '========以下为判断各字段中的img是否存在于oss服务器==========='

                if get_img(data.get('question_html','')):
                    i['flag'].append(10002)
                if get_img(data.get('option_html','')):
                    i['flag'].append(10002)
                if get_img(data.get('answer_all_html', '')):
                    i['flag'].append(10002)
                if get_img(data.get('jieda','')):
                    i['flag'].append(10002)
                if get_img(data.get('fenxi','')):
                    i['flag'].append(10002)
                if get_img(data.get('dianping','')):
                    i['flag'].append(10002)

                responcse = aft_http.return_json_response_meta(
                        Status.SUCCESS,
                        'success', i)
                return responcse
            else:

                i['flag'].append(10001)
                i['option_html'] = ''
                i['answer_all_html'] = ''
                i['jieda'] = ''
                i['fenxi'] = ''
                i['dianping'] = ''
                responcse = aft_http.return_json_response_meta(
                    Status.SUCCESS,
                    'success', i)
                return responcse
        except Exception as a:

            print(a)
    responcse=aft_http.return_json_response_meta(Status.INVALID_PARAMS,'error')
    return  responcse

