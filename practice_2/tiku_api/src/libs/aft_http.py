import json
from django.shortcuts import HttpResponse
from django.http import JsonResponse


def return_json_response(status, msg, **kw):
    return HttpResponse(json.dumps(dict(status=status, msg=msg, **kw)),
                        content_type='application/json', charset='utf-8')


def return_json_response_meta(status, msg, d={}):
    meta = {'status': status, 'msg': msg}
    if d:
        result = json.dumps({'meta': meta, 'data': d},ensure_ascii=False)
    else:
        result = json.dumps({'meta': meta},ensure_ascii=False)
    r = HttpResponse(result,content_type='application/json', charset='utf-8')
    r['Access-Control-Allow-Origin'] = '*'
    r['Access-Control-Allow-Headers'] = 'authorization,report'
    r['Access-Control-Allow-Credentials'] = 'true'
    return r


class Status(object):
    SUCCESS = 0  # 成功
    NEED_LOGIN = 1  # 需要登录
    INVALID_PARAMS = 2  # 参数错误
    INTERNAL_ERROR = 3  # 系统内部错误
    NOT_EXIST = 4  # 请求对象不存在
    ASYNC_WAIT = 5  # 需要等待


class JsonResult(object):
    def __init__(self):
        self.meta = {}
        self.data = {}

    def success(self, data=None, msg=None):
        self.meta['status'] = Status.SUCCESS
        if msg:
            self.meta['msg'] = msg
        else:
            self.meta['msg'] = 'success'
        if data is not None:
            self.data = data

    def need_login(self, msg=None):
        self.fail(Status.NEED_LOGIN, msg)

    def invalid_params(self, msg=None):
        self.fail(Status.INVALID_PARAMS, msg)

    def not_exist(self, msg=None):
        self.fail(Status.NOT_EXIST, msg)

    def sys_error(self, msg=None):
        self.fail(Status.INTERNAL_ERROR, msg)

    def need_vip(self, msg=None):
        self.fail(Status.NEED_VIP, msg)

    def fail(self, status, msg):
        self.meta['status'] = status
        if msg:
            self.meta['msg'] = msg

    def to_json(self):
        return json.dumps({
            'meta': self.meta,
            'data': self.data
        })

    @property
    def respone(self):
        return JsonResponse({
            'meta': self.meta,
            'data': self.data
        })