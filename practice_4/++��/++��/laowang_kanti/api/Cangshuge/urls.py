"""Cangshuge URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url

from question_viewer.views import (
                IndexView,
                QuestionLstView,
                QuestionCompareView,
                LoginView,
                LogoutView,
                QuestionDetailView,
                QuestionView,
                QuestionRenderView,
                QuestionBgiqView
)


urlpatterns = [
    url(r'^$', IndexView.as_view()),
    url(r'^api/v1/questions/$', QuestionLstView.as_view()),
    url(r'^api/v1/questions/bigq/$', QuestionBgiqView.as_view()),

    url(r'^api/v1/questions/compare/$', QuestionCompareView.as_view()),
    url(r'^api/v1/sessions/$', LoginView.as_view()),
    url(r'^api/v1/logout/', LogoutView.as_view()),
    url(r'^api/v1/questions/question_pre/(?P<search_condition>\S+)$', QuestionDetailView.as_view()
    ),
    url(
        r'^api/v1/questions/(?P<db_table>[a-zA-Z0-9`._]+)/(?P<question_id>\d+)$',
        QuestionView.as_view()
    ),
    url(
        r'^api/v1/questions/(?P<db_table>[a-zA-Z0-9`._]+)/(?P<question_id>\d+)/render$',
        QuestionRenderView.as_view()
    )
]
