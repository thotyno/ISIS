from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'pages/isos.html') 

def schools(request):
    return render(request,'pages/schools.html') 

def schools1(request):
    return render(request,'pages/schools1.html') 

def cs(request):
    return render(request,'pages/cs.html') 

def csmark(request):
    return render(request,'pages/mark.html') 

def classmap(request):
    return render(request,'pages/classmap.html') 

def classbill(request):
    return render(request,'pages/classbill.html') 

def personal(request):
    return render(request,'pages/personal.html') 

def personalinfo(request):
    return render(request,'pages/personalinfo.html') 

def classchat(request):
    return render(request,'pages/classchat.html') 
    
def classmem(request):
    return render(request,'pages/classmem.html') 

def sdb(request):
    return render(request,'pages/sdb.html') 

def tncs(request):
    return render(request,'pages/tncs.html') 

def teacher(request):
    return render(request,'pages/teacher.html') 

def tkball(request):
    return render(request,'pages/tkball.html') 

def tkbclass(request):
    return render(request,'pages/tkbclass.html') 

def notiall(request):
    return render(request,'pages/notiall.html') 

def noticlass(request):
    return render(request,'pages/noticlass.html')

def notiuser(request):
    return render(request,'pages/notiuser.html')  
    
def wj(request):
    return render(request,'pages/wj.html') 

def wjtop(request):
    return render(request,'pages/wjtop.html') 

def best(request):
    return render(request,'pages/best.html') 

def nap(request):
    return render(request,'pages/nap.html') 

def lbr(request):
    return render(request,'pages/lbr.html') 

def lh(request):
    return render(request,'pages/lh.html') 

def lal(request):
    return render(request,'pages/lal.html') 

def muvic(request):
    return render(request,'pages/muvic.html')

def fl(request):
    return render(request,'pages/fl.html') 

def nl(request):
    return render(request,'pages/nl.html') 

def settings(request):
    return render(request,'pages/settings.html') 
