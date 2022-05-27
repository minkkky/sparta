from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import UserModel

def first_view(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    elif request.method == 'POST':
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)

        if len(password) < 8:
             return HttpResponse("비밀번호 길이 에러")
        else:
            val = "@" not in email
            if val:
                return HttpResponse("이메일 형식 에러")
            else:
                new_user = UserModel()
                new_user.email = email
                new_user.password = password
                new_user.save()

                return HttpResponse("회원가입 완료!")

        return redirect('index.html')