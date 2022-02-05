
from dataclasses import fields
from django.http import HttpResponse
from django.shortcuts import render , redirect , HttpResponseRedirect
from .models import student , track
from django.contrib.auth import logout
from .forms import form1 , form2
from django.views import View
from django.views.generic import ListView , CreateView

def insert_stud(req):
    if req.method=='POST':
        student.objects.create(name=req.POST['uname'] , mail=req.POST['mail'] , address=req.POST['address'] , bdate=req.POST['bdate'])
        return render(req , 'insert.html')
        
    else:
        print('hellommmmm')
        return render(req , 'insert.html')

def insert1(req):
    

    if req.method=='POST':
        s_form=form1(req.POST)
        if s_form.is_valid():
            print('hellonnnn')
            student.objects.create(name=req.POST['name'] , mail=req.POST['mail'] , address=req.POST['address'] , bdate=req.POST['bdate'] , track=track.objects.get(id = req.POST['track']))
            return  HttpResponseRedirect('/select/') 
        
        else:
            msg= 'incorrect format for fields ' + str(s_form.errors.keys())

            return render(req , 'insert.html' , {'form1' : s_form  , 'msg' : msg})


    else:
        s_form=form1()
        return render(req , 'insert.html' , {'form1' : s_form })


def insert2(req):
    if req.method=='GET':
        s_form=form2()
        return render(req , 'insert.html' , {'form1' : s_form})

    else:
        s_form=form2(req.POST)
        if s_form.is_valid():
            s_form.save()
            return  HttpResponseRedirect('/select/')

        else:
            msg= 'incorrect format for fields ' + str(s_form.errors.keys())
            return render(req , 'insert.html' , {'form1' : s_form  , 'msg' : msg})


   


def select_stud(req) :
    studs=student.objects.all()
    obj={}
    obj['studs']=studs
    print(studs)
    return render (req , 'select.html' ,obj)
    

def search_stud(req):
    if req.method=='GET':
        return render(req ,'search.html')

    else:
        studs=student.objects.filter(name=req.POST['uname'])
        return render(req ,'res-search.html' ,{'studs' : studs})

        

    


def del_stud(req ,id):
    student.objects.filter(id=id).delete()
    return render(req ,'select.html' ,{'studs' : student.objects.all() })


def update(req , id):
    if req.method =='GET':
        stud = student.objects.get(id=id)
        return render(req ,'update.html', {'stud': stud})

    else:
        student.objects.filter(id=id).update(name=req.POST['uname'] , mail=req.POST['mail'] , address=req.POST['address'] )

        return redirect(select_stud)

class update1(View):

    def get(self , req , id):
        obj = student.objects.get(id=id)
        print(obj.name)
        s_form=form1({'name':obj.name , 'mail': obj.mail , 'address':obj.address , 'bdate':obj.bdate , 'track':obj.track.id })
        return render(req ,'update.html', {'form1':s_form })

    def post (self , req , id):
        #obj = student.objects.get(id=id)
        # print(obj.name)
        s_form=form1(req.POST)
        if s_form.is_valid():
            student.objects.filter(id=id).update(name= req.POST['name']  , mail=req.POST['mail'] , address=req.POST['address'] , bdate=req.POST['bdate'] , track=track.objects.get(id = req.POST['track']) )
            return  HttpResponseRedirect('/select/') 

        else:
            msg= 'incorrect format for fields ' + str(s_form.errors.keys())

            return render(req , 'update.html' , {'form1' : s_form  , 'msg' : msg})


        



class update2(View):
    def get(self , req , id):
        obj = student.objects.get(id=id)
        s_form= form2(instance=obj)
        return render(req ,'update.html', {'form1':s_form })

        

    def post(self , req , id):
        s_form=form2(req.POST)
        if s_form.is_valid():
            obj = student.objects.get(id=id)
            s_form2= form2(req.POST , instance=obj)
            s_form2.save()
            return  HttpResponseRedirect('/select/') 

        else:
            msg= 'incorrect format for fields ' + str(s_form.errors.keys())

            return render(req , 'update.html' , {'form1' : s_form  , 'msg' : msg})


class trackList(ListView):
    model=track
        
class trackCreate(CreateView):
    model=track
    fields="__all__"  

def insert_track(req):
    
    track.objects.create(name=req.POST['name'])
    return HttpResponseRedirect('/list-tracks-generic/')



def mylogout(req):

    req.session.clear()
    logout(req)

    return HttpResponseRedirect('/')

# Create your views here.
