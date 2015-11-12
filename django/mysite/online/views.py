# coding=utf-8

from django.shortcuts import render_to_response,render
from online.models import Menu
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from json import dumps
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.

@login_required(login_url="/login")
def index(req):
    menus = Menu.objects.exclude(menu_name = '系统管理').order_by("parent_id")
    if menus:
        for item in menus:
            menu = Menu.objects.filter(parent_id = item.id).order_by("parent_id")
            item.sub_menu = menu
    username = req.COOKIES.get('username','')
    return render(req, 'index.html',locals())

def register(req):
    if req.method == 'POST':
        username = req.POST.get('username')
        password = req.POST.get('password')
        repassword = req.POST.get('repassword')
        if password != repassword:
            return render_to_response('register.html',{'reMsg':''}, context_instance=RequestContext(req))
        user = User.objects.create_user(username, '', password)
        user.save()
        return render_to_response('login.html',{}, context_instance=RequestContext(req))
    else:
        return render_to_response('register.html',{}, context_instance=RequestContext(req))

def register_valid(req):
    dic = {}
    username = req.GET.get("username")
    user = User.objects.filter(username = username)
    if user :
        dic['Msg'] = '用户名已存在！'
        jstr = dumps(dic)
        return HttpResponse(jstr, content_type='application/json')
    jstr = dumps(dic)
    print jstr
    return HttpResponse(jstr, content_type='application/json')

def gotoPage(req):
    pageName = req.GET.get("pageName")
    return render(req, pageName+'.html',locals())
