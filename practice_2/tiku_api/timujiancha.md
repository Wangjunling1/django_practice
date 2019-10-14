# 二、题目检查

服务接口|请求类型|代码连接|详细解释

---|---|---|---

http://`地址`/api/v1/examine/checkout|POST|[views.py](\apps\examine\views.py)|_`传入json`_ 

传入json数据

    {
    data={
        "question_html":"xxx",
        "option_html":"xxx",
        "answer_all_html':'xxx',
        "jieda":"xxx",
        "fenxi":"xxx",
        "dianping":"xxx",
        "flag':0 
    },
    type='x'
    }


字段解释

类型|说明
---|---
type|题目类型，分两类，选择题:1  非选择题：0
data|json格式的数据

返回类型：
_`改变字段则的返回该字段修改的内容，不改变则不反回字段`_

    {"meta": 
        {
        "status": 0,
        "msg": "success"
        },
    "data": 
        {
        "question_html": "xxxx",
        "option_html": "xxxxx", 
        "answer_all_html": "", 
        "jieda": "xxxxx", 
        "fenxi": "xxxxx", 
        "dianping": "xxxxx", 
        "flag": 0
        }
    }

flag|说明
---|---
0       |正常
10001	|只有题干	
10002	|缺图片，无法修复	
10003	|缺图片，无需修复	
10004	|答案等各字段有错误，无法修复	
10005	|答案等各字段有错误，无需修复	
10006	|题目格式杂乱，无法修复	
10007	|题目格式杂乱，无需修复	
10008	|题目标签未闭合

功能：
字段没有实质内容，去掉纯粹的html标签
只有“略”，那么去掉“略”字
字段标签没有闭合，那么修正，将其闭合

题目检查/修正程序
经过程序检查，保证每个题目都是正确的了


例子在请运行代码[example.py](tiku_api\src\example.py)

测试：

传入的数据

       data = {'question_html': '<p>元素<span class="dG cT " tabindex="0" style="font-size: 121%;">',
                'option_html': '',
                'answer_all_html': '<div class="aft_question_wrapper">略',
                'jieda': '<div class="aft_question_wrapper">',
                'fenxi': '<p>元素<img src="http://qimg.afanti100.com/data/image/question_image/104/590e33fa3872d89672b1c91.png"><span class="dG cT " tabindex="0" style="font-size: 121%;">',
                'dianping': '<p><span class="dG cT " tabindex="0" style="font-size: 121%;"></span></p>',
                'flag': 0}
            
返回的数据

    {"meta": {"status": 0, "msg": "success"}, "data": {"flag": [10008, 10004, 10008, 10004, 10002], "question_html": "<p>元素<span class=\"dG cT\" style=\"font-size: 121%;\" tabindex=\"0\"></span></p>", "answer_all_html": "", "jieda": "", "fenxi": "<p>元素<img src=\"http://qimg.afanti100.com/data/image/question_image/104/590e33fa3872d89672b1c91.png\"/><span class=\"dG cT\" style=\"font-size: 121%;\" tabindex=\"0\"></span></p>", "dianping": ""}}
