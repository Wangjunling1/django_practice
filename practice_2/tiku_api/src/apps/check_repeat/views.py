from __future__ import unicode_literals
from django.views.decorators.csrf import csrf_exempt
from libs import aft_http
from libs.aft_http import Status
from django.views import View
import json
import pymysql
import os
import logging
from .models import Md5Status


_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_FILE_PATH = os.path.join(_DIR, 'priority')
config = json.load(open(CONFIG_FILE_PATH))

LOGGING_FORMAT = '%(asctime)-15s:%(levelname)s: %(message)s'
logging.basicConfig(format=LOGGING_FORMAT, level=logging.INFO,
                    filename='apps/check_repeat/check.log', filemode='a',)

# ETCD_HOST = os.environ['ETCD_HOST']
# ETCD_PORT = int(os.environ['ETCD_PORT'])
# ETCD_USERNAME = os.environ.get('ETCD_USERNAME')
# ETCD_PASSWORD = os.environ.get('ETCD_PASSWORD')
# ETCD_DB = os.environ.get('ETCD_DB')


ETCD_HOST='172.16.16.17'
ETCD_PORT='3306'
ETCD_USERNAME='wangjunling'
ETCD_PASSWORD='Aftwjl3BwNe9D'
ETCD_DB='test'


class Detection(View):
    def __init__(self):
        super(Detection,self).__init__()
        self.connect = pymysql.connect(
            host=ETCD_HOST,
            user=ETCD_USERNAME,
            passwd=ETCD_PASSWORD,
            db=ETCD_DB,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
            )
        self.cursor = self.connect.cursor()
    def post(self,request):
        '''
        用来检查重复数据
        :param request:
        :return:
        '''
        if request.method=="POST":
            try:
                responcse_data={
                        "question_id":0,
                        "origin_question_id":0,
                        "source":0,
                        "origin_source":0,
                        "spider_url":0,
                        "origin_spider_url":0,
                    }
                data = json.loads(request.POST.get('data'))
                if len(data)!=4:
                    raise Exception('参数错误')

                if  int(config[str(data.get('source'))]) ==-1:
                    responcse = aft_http.return_json_response_meta(
                        Status.SUCCESS,
                        'success', responcse_data)
                    return responcse
                md5 = data.get('md5', '')
                # sql_get=f"""select * from `md5_status` where `md5`='{md5}'"""
                #
                # self.cursor.execute(sql_get)
                # dd=self.cursor.fetchone()
                dd=Md5Status.objects.filter(md5=md5)[0]
                print(dd.get('source'))
                if dd:
                    if int(config[str(dd.get('source'))]) <int(config[str(data.get('source'))]):
                        responcse_data['source'] = int(data.get('source'))
                        responcse_data['origin_source']= int(dd.get('source'))
                        responcse_data['question_id'] = int(data.get('question_id'))
                        responcse_data['origin_question_id'] = int(dd.get('question_id'))
                        responcse_data['spider_url'] = data.get('spider_url')
                        responcse_data['origin_spider_url'] = dd.get('key')
                        responcse = aft_http.return_json_response_meta(
                            Status.SUCCESS,
                            'success', responcse_data)
                        #修改md5_statu表，将数据更新为最优。
                        self.__sql_up_md5(data,dd.get('question_id'))
                        return responcse

                    elif int(config[str(data.get('source'))]) ==int(config[str(dd.get('source'))])\
                        and int(data.get('source'))<int(dd.get('source')):

                        responcse_data['source'] = int(data.get('source'))
                        responcse_data['origin_source'] = int(dd.get('source'))
                        responcse_data['question_id'] = int(data.get('question_id'))
                        responcse_data['origin_question_id'] = int(
                            dd.get('question_id'))
                        responcse_data['spider_url'] = data.get('spider_url')
                        responcse_data['origin_spider_url'] = dd.get('key')
                        responcse = aft_http.return_json_response_meta(
                            Status.SUCCESS,
                            'success', responcse_data)
                        # 修改md5_statu表，将数据更新为最优。
                        self.__sql_up_md5(data, dd.get('question_id'))
                        return responcse
                    else:
                        responcse = aft_http.return_json_response_meta(
                            Status.SUCCESS,
                            'success', responcse_data)
                        return responcse
                else:
                    responcse_data['source'] = int(data.get('source'))
                    responcse_data['question_id'] = int(data.get('question_id'))
                    responcse_data['spider_url'] = data.get('spider_url')
                    responcse = aft_http.return_json_response_meta(
                        Status.SUCCESS,
                        'success', responcse_data)
                    #将没有重复的数据插入md5_statu表
                    self.__sql_ins_md5(data)
                    return responcse

            except Exception as a:
                logging.error('原因：{}；数据：{}'.format(a, data))
                responcse = aft_http.return_json_response_meta(
                    Status.INTERNAL_ERROR,
                    '请求数据存在问题，详细请检查check.log文件')
                return responcse

        else:
            responcse=aft_http.return_json_response_meta(Status.INVALID_PARAMS,
                                                         '请求类型错误')
            return  responcse

    def __sql_up_md5(self,data, question_id):
        """
        修改数据表内容
        :param data:传来的修改的内容，类型为字典
        :param md5:要修改的md5值
        :return:无
        """
        sql_update = """
                update md5_status set                 
                source='{}',
                question_id='{}',
                `key`='{}' where `md5`='{}'
                """.format(data.get('source'),question_id,
                           data.get('spider_url'), data.get('md5'))
        try:
            self.cursor.execute(sql_update)
            self.connect.commit()
        except Exception as a:
            self.connect.rollback()
            raise Exception(f'{a}:数据存在问题，在update_md5时出现')

    def __sql_ins_md5(self,data):
        """
        将未存在的数据插入数据表中
        :param data:插入表中的数据，类型为字典
        :param md5:插入的唯一标识
        :return:无
        """
        sql_insert = """insert into md5_status(
                `source`,`question_id`,`key`,`md5`)
                values ('{}','{}','{}','{}')""".format(data.get('source'),
                data.get('question_id'),data.get('spider_url'), data.get('md5'))
        try:
            self.cursor.execute(sql_insert)
            self.connect.commit()
        except Exception as a:
            self.connect.rollback()
            raise Exception(f'{a}:数据存在问题，在insert_md5时出现')


