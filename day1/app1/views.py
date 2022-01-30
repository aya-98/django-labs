from django.shortcuts import render
from django.http import HttpResponse

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

