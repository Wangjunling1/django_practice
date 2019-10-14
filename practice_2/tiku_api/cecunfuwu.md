# 三、测重服务

服务接口|请求类型|代码连接|详细解释

---|---|---|---

http://`地址`/api/v1/check_repeat/detection|POST| |传入json

传入json定义

    data={
    'md5':'xxxxx'
    'source':'xxxxx',
    'spider_url':'xxxxx'
    "question_id":"xxxx",
    }

返回值
       
     {
     "meta": 
        {
        "status": 0,
        "msg": "success"
        },
     "data": 
        {
         "question_id":0,
         "origin_question_id":0,
         "source":0,
         "origin_source":0,
         "spider_url":0,
         "origin_spider_url":0,
         }
      }

返回全部为零 说明以存在并且表中的source最优

如果不存在并且question_id传入时为零（未分配）,则返回参数中replace_source=0，question_id=0

