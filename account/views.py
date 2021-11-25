from django.shortcuts import render, redirect # 추가
from django.contrib.auth.models import User # 추가
from django.contrib import auth # 추가

# Create your views here.
def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('main')
        else:
            return render(request, 'signin.html', {'error': '입력 정보가 잘못되었습니다.'})
    else:
        return render(request, 'signin.html')


def signout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('main')
    return redirect('signin')