from django.shortcuts import render, redirect, get_object_or_404
from .models import RSVP
from django.contrib.auth.models import User
from django.contrib import auth

def home(request):
    return render(request, 'frontend/base.html')
def about(request):
    return render(request, 'frontend/aboutus.html')
def response(request):
    return render(request, 'frontend/C19response.html')
def baek(request):
    return render(request, 'frontend/baekhyun.html')
def christ(request):
    return render(request, 'frontend/christmasgifttrain.html')
def donate(request):
    return render(request, 'frontend/COVID19donate.html')
def meal(request):
    return render(request, 'frontend/mealtrain.html')
def pande(request):
    return render(request, 'frontend/pandemictimes.html')
def peer(request):
    return render(request, 'frontend/peertutoring.html')
def publica(request):
    return render(request, 'frontend/publications.html')
def seoul(request):
    return render(request, 'frontend/seoul.html')
def sing(request):
    return render(request, 'frontend/singapore.html')
def branch(request):
    return render(request, 'frontend/branches.html')
def dental(request):
    return render(request, 'frontend/dental.html')
def deaf(request):
    return render(request, 'frontend/deafandblind.html')
def indiv(request):
    return render(request, 'frontend/individal.html')
def ptimes(request):
    return render(request, 'frontend/ptimes.html')
def vol(request):
    return render(request,'frontend/C19response.html')
def volunteering(request):
    return render(request,'frontend/volunteering.html')
def join(request):
    print("join 실행")
    if request.method== 'POST': #form이 post로 던지면 여기서 처리
        print("여기는 포스트 요청")
        email = request.POST['email']
        name = request.POST['name']
        print(email)
        print(name)
        User.objects.create_user(username=name, email=email)
        return redirect("/")
        # else :
        #     return render(request, 'app/user.html', {'nameCompare1':"이미 존재하는 닉네임입니다"})
    else:
        print("join 페이지")
        return render(request, 'frontend/user.html')
def login(request):
    if request.method== 'POST': #form이 post로 던지면 여기서 처리
        email = request.POST['email']
        name = request.POST['name']
        user = auth.authenticate(request, username=name, email=email)
        if user is None:
            redirect('/join')
        else:
            auth.login(request, user)
        return redirect("/")
    else:
        return render(request, 'frontend/login.html')
def logout(request):
    auth.logout(request)
    return redirect("/")

def calendar(request):
    rsvp = RSVP.objects.filter()

    if request.method== 'POST':
        id = request.POST['id']
        count = request.POST['count']
        rsvpDetail = get_object_or_404(RSVP, pk=id) #데이터 받아오기
        rsvpDetail.count -= 1
        rsvpDetail.save()
        return render(request, 'frontend/volunteering.html')
    else:
        return render(request, 'frontend/calendarVolunteering.html', {'rsvp':rsvp})