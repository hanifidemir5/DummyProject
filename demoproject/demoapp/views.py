from django.shortcuts import render
from .models import Menu
# Create your views here.
from django.http import HttpResponse

from datetime import datetime

from demoapp.forms import LoginForm 

def about(request):
    about_content = {'about' : "hebele hübele nereye geldik len dümbele"}
    return render(request,"about.html ",about_content)


def demo_form_view(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form": form }
    return render(request,"home.html",context)

def home_demo(request):
    path = request.path
    scheme = request.scheme
    method = request.method
    adress = request.META['REMOTE_ADDR']
    user_agent = request.META['HTTP_USER_AGENT']
    path_info = request.path_info
    
    content = HttpResponse("<html><body><h1>Hello you mothertucker.<h1><body><html> ")
    
    msg = f"""<br>
    <br>Path: {path}
    <br>Adress: {adress}
    <br>Scheme: {scheme}
    <br>Method: {method}
    <br>User agent: {user_agent}
    <br>Path info: {path_info}
    <br>
    """

    
    return HttpResponse(msg, content_type = 'text/html', charset = 'utf-8')
    




def animekizlari(request):
    text = """  <body><h1 style="color: red;">Animekizlari gerçek değil.<h1><body><html>"""
    return HttpResponse(text) 
def display_date(request):
    date_joined = "Current year: " + str(datetime.today().year) + " Month: " + str(datetime.today().month) + " Day: " + str(datetime.today().day) + " Hour: " + str(datetime.today().hour) + " Minute: " + str(datetime.today().minute) + " Second: " + str(datetime.today().second)
    return HttpResponse(date_joined)  

def menuitems(request, dish):

    items = {

        'pasta' : 'pasta hübele',
        'pizza' : 'pizza andasdadsa sos',
        'soup'  : 'soup and extras'
    }

    description = items[dish]

    return HttpResponse('<h2> {dish} <h2>' + description)

def menu(request):

    items = { 'dishes':[
        {'dish' : "pasta",'components' : "pasta hübele"},
        {'dish' : "pizza",'components' : "pizza andasdadsa sos"},
        {'dish' : "soup", 'components' : "soup and extras"},
    ]}

    return render(request, "menu.html", items)

def menu_by_id(request):
    newmenu = Menu.objects.all()
    newmenu_dict = {'menu' : newmenu}
    return render(request, 'menu_cards.html', newmenu_dict)

def home(request): 
    return render(request, "home.html", {}) 

def register(request): 
    return render(request, "register.html", {}) 

def login(request): 
    return render(request, "login.html", {}) 