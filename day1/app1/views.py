import django
from django.shortcuts import render ,HttpResponseRedirect
from django.http import HttpResponse
from .models import myuser
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login as auth_login , logout

def navbar(req):
    return render(req , 'navbar.html')

def home(req):
    res=HttpResponse("<center><a href='/home'> Home   </a> <br><br><a href='/contact'> Contact Us  </a> <br><br><a href='/about'> About Us </a> <br><br></center><br><br>")
    res.write("<center> <h1> Welcome   </h1> </center>")
    return res

    

def contact(req):
    return render(req ,'contact.html')

def about(req):
    return render(req , 'about.html')

def view_info(req):
    
    obj={'mail' : req.GET['email'] , 'm': req.GET['msg']}
    return render(req , 'info.html' ,obj)

def login(req):
    if req.method =='GET':
        return render(req , 'login.html')

    else:

        # users=myuser.objects.all()

        # for usr in users:
        #     if req.POST['uname'] == usr.name and req.POST['passwd'] == usr.passwd:
        #         return render(req , 'home.html')
        users= myuser.objects.filter(name=req.POST['uname'] , passwd= req.POST['passwd'])
        st_user = authenticate( username=req.POST['uname'] , password= req.POST['passwd'])

        if (len(users)> 0 and st_user is not None):

            auth_login(req , st_user)
            req.session['uname']=users[0].name
            return render(req , 'home.html')
       
        elif (len(users)> 0 and st_user is  None):
            req.session['uname']=users[0].name
            print(req.session['uname'])
            return render(req , 'home.html')

        elif len(users) == 0 :
            return render(req , 'login.html' , {'msg' : 'incorrect username or password'})






        
        


        


def register(req):
    if req.method=='GET':

        return render(req , 'register.html')

    else:
        myuser.objects.create(name=req.POST['uname'] , mail=req.POST['mail'] , passwd=req.POST['passwd'])

        if 'staff' in req.POST:

            User.objects.create_user(username=req.POST['uname'] , password=req.POST['passwd'] , is_staff=True)
            
        
        return HttpResponseRedirect('/')


    
