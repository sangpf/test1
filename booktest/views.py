from django.http import HttpResponse,HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import render
from django.template import RequestContext, loader
from datetime import *
from .models import BookInfo

'''图书列表页'''
def index(request):
    # booklist = BookInfo.objects.all()
    booklist = BookInfo.books.get_queryset()
    template = loader.get_template('booktest/index.html')
    context = RequestContext(request, {'booklist': booklist})
    return HttpResponse(template.render(context))

'''图书详情页'''
def detail(reqeust, id):
    # book = BookInfo.objects.get(pk=id)
    book = BookInfo.books.get(pk=id)
    template = loader.get_template('booktest/detail.html')
    context = RequestContext(reqeust, {'book': book})
    return HttpResponse(template.render(context))


'''get属性'''
# 创建视图getTest1用于定义链接，
def getTest1(request):
    return render(request,'booktest/getTest1.html')

# getTest2用于接收一键一值，
def getTest2(request):
    a=request.GET['a']
    b=request.GET['b']
    context={'a':a,'b':b}
    return render(request,'booktest/getTest2.html',context)

# getTest3用于接收一键多值
def getTest3(request):
    a=request.GET.getlist('a')
    b=request.GET['b']
    context={'a':a,'b':b}
    return render(request,'booktest/getTest3.html',context)


'''post属性'''
def postTest1(request):
    return render(request,'booktest/postTest1.html')

def postTest2(request):
    uname=request.POST['uname']
    upwd=request.POST['upwd']
    ugender=request.POST['ugender']
    uhobby=request.POST.getlist('uhobby')
    context={'uname':uname,'upwd':upwd,'ugender':ugender,'uhobby':uhobby}
    return render(request,'booktest/postTest2.html',context)


'''HttpResponse对象'''
def response_index(request):
    response = HttpResponse()
    # if request.COOKIES.has_key('h1'):
    key = 'h1'
    if key in request.COOKIES:
            response.write('<h1>' + request.COOKIES['h1'] + '</h1>')
    response.set_cookie('h1', '你好', 120)
    # response.set_cookie('h1', '你好', None, datetime(2016, 10, 31))
    return response


'''子类JsonResponse'''
def json_index(requeset):
    return JsonResponse({'list': 'abc'})


