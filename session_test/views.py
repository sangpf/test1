from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse

def index(request):
    uname = request.session.get('uname')
    return render(request, 'session_test/index.html', {'uname': uname})

def login(request):
    return render(request, 'session_test/login.html')

def login_handle(request):
    request.session['uname'] = request.POST['uname']
    # request.session.set_expiry(10)
    # request.session.set_expiry(timedelta(days=5))
    # request.session.set_expiry(0)
    # request.session.set_expiry(None)
    return redirect(reverse('session_test:index'))

def logout(request):
    # request.session['uname'] = None
    # del request.session['uname']
    # request.session.clear()
    # flush()：删除当前的会话数据并删除会话的Cookie
    request.session.flush()
    return redirect(reverse('session_test:index'))



