from __future__ import unicode_literals
import json
from django.views.decorators.csrf import csrf_exempt
from libs import aft_http
from libs.aft_http import Status
from apps.template.template import Question,Option
# Create your views here.

@csrf_exempt
def render_data(request):

    question={}
    responcse = aft_http.return_json_response_meta(Status.INVALID_PARAMS,
                                                   "error", question)
    if request.method=="POST":
        try:
            data=request.POST.get('data','')
            if data:
                data=json.loads(data)
                question = Question(**data)
                question = json.dumps(question.normialize(),ensure_ascii=False)
                responcse = aft_http.return_json_response_meta(Status.SUCCESS,
                                                            "success", question)
        except Exception as a:
            print(a)
    return responcse


