from django.shortcuts import render
# Create your views here.
from login import models
import hashlib
from django.core.paginator import Paginator
import math
from django.shortcuts import HttpResponse
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
import time


dengname=''
dengluzhuangtai='off'
# 自定义页码显示
class CustonPaginator(Paginator):
    def __init__(self,current_page,per_pager_num,*args,**kwargs):
        # 当前页
        self.current_page=int(current_page)
        # 页码数量，最多显示
        self.per_pager_num=int(per_pager_num)
        super(CustonPaginator,self).__init__(*args,**kwargs)
    def pager_num_range(self):
       # 总页数
        if self.num_pages<self.per_pager_num:
            return range(1,self.num_pages+1)
        # 总页数特别多
        part=int(self.per_pager_num/2)
        if self.current_page<=part:
            return range(1,self.per_pager_num+1)
        if (self.current_page+part)>self.num_pages:
            return range(self.num_pages-self.per_pager_num,self.num_pages+1)
        return range(self.current_page-part,self.current_page+part+1)

def login(request):
    return render(request, 'button/login.html')

def list_jiaoce(request):
    current_page=request.GET.get('p')
    if  current_page==  None:
        current_page=1
    # 对象
    paginator=CustonPaginator(current_page,8,models.jiaoce.objects.all()[4:],20)
    try:
        posts=paginator.page(current_page)
    except PageNotAnInteger:
        posts =paginator.page(1)
    except EmptyPage:
        posts=paginator.page(paginator.num_pages)
    xinjiaoce = models.jiaoce.objects.all()[:4]
    print(dengluzhuangtai)
    if dengluzhuangtai =='on':
        name=dengname
        return render(request,'button/list_jiaoce.html',locals())
    return render(request,'button/login.html')


def list_mpvce(request):
    current_page = request.GET.get('p')
    if  current_page==  None:
        current_page=1
    # 对象
    paginator = CustonPaginator(current_page, 8, models.mpvce.objects.all()[4:], 20)
    try:
        posts = paginator.page(current_page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    xinjiaoce = models.mpvce.objects.all()[:4]

    if dengluzhuangtai == 'on':
        name = dengname
        return render(request, 'button/list_mpvce.html', locals())
    return render(request, 'button/login.html')



def list_paoce(request):
    current_page = request.GET.get('p')
    if current_page == None:
        current_page = 1
    # 对象
    paginator = CustonPaginator(current_page, 8, models.paoce.objects.all()[4:], 20)
    try:
        posts = paginator.page(current_page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    xinjiaoce = models.paoce.objects.all()[:4]

    if dengluzhuangtai == 'on':
        name = dengname
        return render(request, 'button/list_paoce.html', locals())
    return render(request, 'button/login.html')
def list_pikamianbo(request):

    #改

    xinpikace = models.pikace.objects.all()[:2]

    xinmianbaoce=models.mianbaoce.objects.all()[:2]


    if '皮卡'==request.GET.get('ce'):
        current_page = request.GET.get('p')
        if current_page == None:
            current_page = 1
        # 对象
        paginator = CustonPaginator(current_page, 8, models.pikace.objects.all()[2:], 20)
        try:
            posts = paginator.page(current_page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
        xinjiaoce = models.pikace.objects.all()[:4]

    else:
        current_page = request.GET.get('p')
        if current_page == None:
            current_page = 1
        # 对象
        paginator = CustonPaginator(current_page, 8, models.mianbaoce.objects.all()[2:], 20)
        try:
            posts = paginator.page(current_page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
        xinjiaoce = models.mianbaoce.objects.all()[:4]
    if dengluzhuangtai == 'on':
        name = dengname
        return render(request, 'button/list_pikamianbo.html', locals())
    return render(request, 'button/login.html')
def list_xingnengyuan(request):
    current_page = request.GET.get('p')
    if current_page == None:
        current_page = 1
    # 对象
    paginator = CustonPaginator(current_page, 8, models.xinnengyuance.objects.all()[4:], 20)
    try:
        posts = paginator.page(current_page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    xinjiaoce = models.xinnengyuance.objects.all()[:4]
    if dengluzhuangtai == 'on':
        name = dengname
        return render(request, 'button/list_xingnengyuan.html', locals())
    return render(request, 'button/login.html')
def list_yueyece(request):
    current_page = request.GET.get('p')
    if current_page == None:
        current_page = 1
    # 对象
    paginator = CustonPaginator(current_page, 8, models.yueyece.objects.all()[4:], 20)
    try:
        posts = paginator.page(current_page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    xinjiaoce = models.yueyece.objects.all()[:4]
    if dengluzhuangtai == 'on':
        name = dengname
        return render(request, 'button/list_yueyece.html', locals())
    return render(request, 'button/login.html')





# 登录
def verify(request):

    user= request.POST.get('username',None)
    pwd=request.POST.get('pwd',None)
    danuser=models.user.objects.filter(username=user)
    if len(danuser)!=0:
        md5 = hashlib.md5()
        md5.update(bytes(pwd, encoding='utf-8'))
        if danuser[0].pwd==md5.hexdigest():
                exrr=''
                a=[]
                global dengluzhuangtai,dengname
                dengluzhuangtai = 'on'
                dengname=user


                print(dengluzhuangtai)
                return HttpResponseRedirect('/index/')

    exrr='账户或密码错误,请重新输入'
    return render(request, 'button/login.html', locals())
# 注册

def register(request):
    username=request.POST.get('user_name',None)
    pwd=request.POST.get('pwd',None)
    email=request.POST.get('email',None)
    al=request.POST.get('allow',None)
    if al=='on' and username!='' and pwd !='' and email!='':
        chongzai = models.user.objects.filter(username=username)
        if len(chongzai) == 0:
            err = ''
            # 给密码加密放入数据库
            md5=hashlib.md5()
            md5.update(bytes(pwd,encoding='utf-8'))

            models.user.objects.create(username=username,pwd=md5.hexdigest(),email=email)
            return render(request, 'button/login.html')
        else:
            err = '用户名已存在,请重新输入'

    return render(request, 'button/register.html', locals())



def index(request):
    jiaoce=models.jiaoce.objects.all()[:4]
    paoce=models.paoce.objects.all()[:4]
    pikace=models.pikace.objects.all()[:2]
    xinnengyuance=models.xinnengyuance.objects.all()[:4]
    yueyece=models.yueyece.objects.all()[:4]
    mpvce=models.mpvce.objects.all()[:4]
    mainbaoce = models.mianbaoce.objects.all()[:2]

    name=dengname

    return render(request, 'button/index.html', locals())
#注销
def zhuxiao(request):
    global dengluzhuangtai,dengname
    dengluzhuangtai='off'
    dengname=''
    return HttpResponseRedirect('/index/')

# 初始进入页面
def jing(request):
        jiaoce = models.jiaoce.objects.all()[:4]
        paoce = models.paoce.objects.all()[:4]
        pikace = models.pikace.objects.all()[:2]
        xinnengyuance = models.xinnengyuance.objects.all()[:4]
        yueyece = models.yueyece.objects.all()[:4]
        mpvce = models.mpvce.objects.all()[:4]
        mainbaoce = models.mianbaoce.objects.all()[:2]
        return render(request, 'button/aaa.html', locals())

def geren(request):
    return render(request,'button/user_info.html')
def geren1(request):
    return render(request,'button/user_info1.html')
def geren2(request):
    return render(request,'button/user_info2.html')