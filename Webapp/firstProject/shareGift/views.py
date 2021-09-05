from django.shortcuts import render
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
# Create your views here.
