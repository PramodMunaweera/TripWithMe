from django.shortcuts import render
from django.http import HttpResponse,Http404

# Create your views here.
def index(request):
    return render(request,'travel/index.html')

def smart_planner(request):
    return render(request,'travel/CustomPlan.html')


def mytrip(request):
    return render(request,'travel/MyPlanHome.html')