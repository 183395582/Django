# coding=utf-8

from django.shortcuts import render_to_response,render
from online.models import User,Menu
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from json import dumps
from bootstrap_toolkit.widgets import BootstrapDateInput, BootstrapTextInput, BootstrapUneditableInput
# Create your views here.

def login(req):
    if req.method == 'POST':
        username = req.POST.get('username')
        password = req.POST.get('password')
        user = User.objects.filter(username=username, password=password)
        if user:
            response = HttpResponseRedirect('/online/index/')
            response.set_cookie('username',username,3600)
            return response
        return render_to_response("login.html")
    if req.method == 'GET':
        return render_to_response('login.html',{}, context_instance=RequestContext(req))

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
        User.objects.create(username= username,password=password);
        return render_to_response('login.html',{}, context_instance=RequestContext(req))
    if req.method == 'GET':
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
