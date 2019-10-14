# 一、提取文本


服务接口|请求类型|代码连接|详细解释

---|---|---|---

http://`地址`/api/v1/text/puretext/|POST|[views.py](\tiku_api\src\apps\views.py)|_`传入html`_ 由html获取带有latex信息的纯文本

传入的数据

    {
        html='xxx',
    }

返回数据
    
    {
        "meta":
            {
            "msg": "success", 
            "status": 0
            }, 
        "data": "xxx"
     }
     
 
例子在请运行代码[example.py](tiku_api\src\example.py)
