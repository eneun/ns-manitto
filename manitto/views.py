from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import Friend


# Create your views here.
def main(request):
    if request.user.is_authenticated:
        if request.user.username == 'master':
            return render(request,'main.html')
        else:
            manitto = Friend.objects.get(user1=request.user)
        return render(request,'main.html', {'manitto': manitto})
    else:
        return render(request,'main.html')



# 마니또 뽑기
def picker(request):
    # 관리자 아니면 메인으로
    if not request.user.username=='master':
        return redirect('main')

    import random

    # 마니또 참여할 사람 리스트 섞기
    users = User.objects.exclude(username='master')
    user_list = []
    for user in users:
        user_list.append(user.username)
    random.shuffle(user_list)

    # 새로 뽑아서 프렌드모델에 저장하기 전, 프렌드모델 비우기
    friends = Friend.objects.all()
    friends.delete()

    # 한 명씩 마니또 뽑기
    for user in users:
        user2 = User.objects.get(username=user_list[-1])
        Friend.objects.create(user1=user, user2=user2)
        user_list.pop()
        print(user_list)
    
    return render(request,'picker.html')

def result(request):
    # 관리자 아니면 메인으로
    if not request.user.username=='master':
        return redirect('main')
        
    friends = Friend.objects.all()
    for friend in friends:
        print(friend.user1,'의 마니또는 ',friend.user2)

    return render(request,'result.html', {'friends': friends})