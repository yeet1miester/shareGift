from django.shortcuts import render, redirect, get_object_or_404
from .models import RSVP
from django.contrib.auth.models import User
from django.contrib import auth

#main
def home(request):
    return render(request, 'frontend/base.html')

# publications
def publica(request):
    return render(request, 'frontend/publications.html')

# covid19
def covid19(request):
    return render(request, 'frontend/covid19/C19response.html')
def christ(request):
    return render(request, 'frontend/covid19/christmasgifttrain.html')
def donate(request):
    return render(request, 'frontend/covid19/COVID19donate.html')
def meal(request):
    return render(request, 'frontend/covid19/mealtrain.html')
def pande(request):
    return render(request, 'frontend/covid19/pandemictimes.html')
def peer(request):
    return render(request, 'frontend/covid19/peertutoring.html')

# branches
def baek(request):
    return render(request, 'frontend/branches/baekhyun.html')
def seoul(request):
    return render(request, 'frontend/branches/seoul.html')
def sing(request):
    return render(request, 'frontend/branches/singapore.html')
def branch(request):
    return render(request, 'frontend/branches/branches.html')

# aboutus
def about(request):
    return render(request, 'frontend/aboutUs/aboutus.html')
def dental(request):
    return render(request, 'frontend/aboutUs/dental.html')
def deaf(request):
    return render(request, 'frontend/aboutUs/deafandblind.html')
def indiv(request):
    return render(request, 'frontend/aboutUs/individal.html')
def ptimes(request):
    return render(request, 'frontend/aboutUs/ptimes.html')
def team(request):
    return render(request,'frontend/aboutUs/teammembers.html')

def history(request):
    return render(request,'frontend/history.html')

# join, login, logout
def join(request):
    # print("join 실행")
    if request.method== 'POST': #form이 post로 던지면 여기서 처리
        # print("여기는 포스트 요청")
        email = request.POST['email']
        name = request.POST['name']
        password = request.POST['name']
        # print(email)
        # print(name)
        User.objects.create_user(username=name, email=email, password=password)
        return redirect("/")
        # else :
        #     return render(request, 'app/user.html', {'nameCompare1':"이미 존재하는 닉네임입니다"})
    else:
        # print("user Join 페이지")
        return render(request, 'frontend/user.html')
def login(request):
    if request.method== 'POST': #form이 post로 던지면 여기서 처리
        email = request.POST['email']
        name = request.POST['name']
        # nameList = User.objects.filter()
        user = auth.authenticate(request, username=name, password=name)
        # for nameCheck in nameList:
        #     if nameCheck.email == email and nameCheck.username == name:
        #         print(nameCheck)
        #         email = nameCheck.email
        #         name = nameCheck.username
        if user is None:
            message = "아이디 또는 비밀번호가 틀렸습니다."
            return render(request, 'frontend/login.html',{"message":message})
        else:
            print("로그인완료")
            auth.login(request, user)
            return redirect("/")
    else:
        return render(request, 'frontend/login.html')
def logout(request):
    auth.logout(request)
    return redirect("/")

# volunteering
def calendar(request):
    rsvp = RSVP.objects.filter()

    if request.method== 'POST':
        id = request.POST['id']
        rsvpDetail = get_object_or_404(RSVP, pk=id) #데이터 받아오기
        rsvpDetail.count -= 1
        rsvpDetail.save()
        return render(request, 'frontend/volunteering/volunteering.html')
    else:
        return render(request, 'frontend/volunteering/calendarVolunteering.html', {'rsvp':rsvp})

def volunteering(request):
    return render(request,'frontend/volunteering/volunteering.html')