from django.shortcuts import render , redirect , HttpResponseRedirect
from .models import studnent
from django.contrib.auth import logout
def insert_stud(req):
    if req.method=='POST':
        studnent.objects.create(name=req.POST['uname'] , mail=req.POST['mail'] , address=req.POST['address'] , bdate=req.POST['bdate'])
        return render(req , 'insert.html')
        
    else:
        print('hellommmmm')
        return render(req , 'insert.html')

def select_stud(req) :
    studs=studnent.objects.all()
    obj={}
    obj['studs']=studs
    print(studs)
    return render (req , 'select.html' ,obj)
    

def search_stud(req):
    if req.method=='GET':
        return render(req ,'search.html')

    else:
        studs=studnent.objects.filter(name=req.POST['uname'])
        return render(req ,'res-search.html' ,{'studs' : studs})

        

    


def del_stud(req ,id):
    studnent.objects.filter(id=id).delete()
    return render(req ,'select.html' ,{'studs' : studnent.objects.all() })


def update(req , id):
    if req.method =='GET':
        stud = studnent.objects.get(id=id)
        return render(req ,'update.html', {'stud': stud})

    else:
        studnent.objects.filter(id=id).update(name=req.POST['uname'] , mail=req.POST['mail'] , address=req.POST['address'] )

        return redirect(select_stud)

        

def mylogout(req):

    req.session.clear()
    logout(req)

    return HttpResponseRedirect('/')

# Create your views here.
