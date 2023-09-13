from django.shortcuts import render,redirect
import requests
from bs4 import BeautifulSoup
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from chanukyasepapp.models import Useradd,Contact
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def home(request):
    return render(request,"base.html")

def products(request):
    return render(request,"products.html")


#1
#realme Tv
response=requests.get("https://www.flipkart.com/search?q=tv+smart+tv&sid=ckf%2Cczl&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_2_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_2_na_na_na&as-pos=1&as-type=RECENT&suggestionId=tv+smart+tv%7CTelevisions&requestId=deed6b2c-ff89-42d4-a8da-19a5d2e0590a&as-searchtext=tv+smart+tv&p%5B%5D=facets.brand%255B%255D%3Drealme")
soup=BeautifulSoup(response.content,'html.parser')
names=soup.find_all('div',class_='_4rR01T')
prices=soup.find_all('div',class_='_30jeq3 _1_WHN1')
ratings=soup.find_all('div',class_='_3LWZlK')
images=soup.find_all('img',class_='_396cs4')
links=soup.find_all('a',class_='_1fQZEK')
image=[]
name=[]
price=[]
rate=[]
link=[]
for i in names[0:20]:
    d=i.get_text()
    name.append(d)
for i in prices[0:20]:
    d=i.get_text()
    price.append(d)
for i in ratings[0:20]:
    d=i.get_text()
    rate.append(float(d))
for i in images[0:20]:
    d=i['src']
    image.append(d)
for i in links[0:20]:
    d="https://www.flipkart.com/"+i['href']
    link.append(d)

mylist1=zip(name,
price,
rate,
image,
link
)



def realme(request):
    return render(request,"realme.html",{'mylist1':mylist1})

#2
#Mi Tv
response=requests.get("https://www.flipkart.com/search?q=tv+smart+tv&sid=ckf%2Cczl&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_2_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_2_na_na_na&as-pos=1&as-type=RECENT&suggestionId=tv+smart+tv%7CTelevisions&requestId=deed6b2c-ff89-42d4-a8da-19a5d2e0590a&as-searchtext=tv+smart+tv&p%5B%5D=facets.brand%255B%255D%3DMi")
soup=BeautifulSoup(response.content,'html.parser')
names=soup.find_all('div',class_='_4rR01T')
prices=soup.find_all('div',class_='_30jeq3 _1_WHN1')
ratings=soup.find_all('div',class_='_3LWZlK')
images=soup.find_all('img',class_='_396cs4')
links=soup.find_all('a',class_='_1fQZEK')
image=[]
name=[]
price=[]
rate=[]
link=[]
for i in names[0:20]:
    d=i.get_text()
    name.append(d)
for i in prices[0:20]:
    d=i.get_text()
    price.append(d)
for i in ratings[0:20]:
    d=i.get_text()
    rate.append(float(d))
for i in images[0:20]:
    d=i['src']
    image.append(d)
for i in links[0:20]:
    d="https://www.flipkart.com/"+i['href']
    link.append(d)

mylist2=zip(name,
price,
rate,
image,
link
)

def mi(request):
    return render(request,"mi.html",{'mylist2':mylist2})

# mobiles_rating=pandas.DataFrame()
# mobiles_rating['Ratings']=Rating
# print(mobiles_rating)
# mobiles_rating.to_csv('moblies_rating.csv')


#3
#oneplus
response=requests.get("https://www.flipkart.com/search?q=tv+smart+tv&sid=ckf%2Cczl&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_2_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_2_na_na_na&as-pos=1&as-type=RECENT&suggestionId=tv+smart+tv%7CTelevisions&requestId=deed6b2c-ff89-42d4-a8da-19a5d2e0590a&as-searchtext=tv+smart+tv&p%5B%5D=facets.brand%255B%255D%3DOnePlus")
soup=BeautifulSoup(response.content,'html.parser')
names=soup.find_all('div',class_='_4rR01T')
prices=soup.find_all('div',class_='_30jeq3 _1_WHN1')
ratings=soup.find_all('div',class_='_3LWZlK')
images=soup.find_all('img',class_='_396cs4')
links=soup.find_all('a',class_='_1fQZEK')
image=[]
name=[]
price=[]
rate=[]
link=[]
for i in names[0:20]:
    d=i.get_text()
    name.append(d)
for i in prices[0:20]:
    d=i.get_text()
    price.append(d)
for i in ratings[0:20]:
    d=i.get_text()
    rate.append(float(d))
for i in images[0:20]:
    d=i['src']
    image.append(d)
for i in links[0:20]:
    d="https://www.flipkart.com/"+i['href']
    link.append(d)

mylist3=zip(name,
price,
rate,
image,
link
)

def oneplus(request):
    return render(request,"oneplus.html",{"mylist3":mylist3})


#4
#Samsung
response=requests.get("https://www.flipkart.com/search?q=tv+smart+tv&sid=ckf%2Cczl&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_2_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_2_na_na_na&as-pos=1&as-type=RECENT&suggestionId=tv+smart+tv%7CTelevisions&requestId=deed6b2c-ff89-42d4-a8da-19a5d2e0590a&as-searchtext=tv+smart+tv&p%5B%5D=facets.brand%255B%255D%3DSAMSUNG")
soup=BeautifulSoup(response.content,'html.parser')
names=soup.find_all('div',class_='_4rR01T')
prices=soup.find_all('div',class_='_30jeq3 _1_WHN1')
ratings=soup.find_all('div',class_='_3LWZlK')
images=soup.find_all('img',class_='_396cs4')
links=soup.find_all('a',class_='_1fQZEK')
image=[]
name=[]
price=[]
rate=[]
link=[]
for i in names[0:20]:
    d=i.get_text()
    name.append(d)
for i in prices[0:20]:
    d=i.get_text()
    price.append(d)
for i in ratings[0:20]:
    d=i.get_text()
    rate.append(float(d))
for i in images[0:20]:
    d=i['src']
    image.append(d)
for i in links[0:20]:
    d="https://www.flipkart.com/"+i['href']
    link.append(d)

mylist4=zip(name,
price,
rate,
image,
link
)


def samsung(request):
    return render(request,"samsung.html",{'mylist4':mylist4})

#5
# LG
response=requests.get("https://www.flipkart.com/search?q=tv+smart+tv&sid=ckf%2Cczl&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_2_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_2_na_na_na&as-pos=1&as-type=RECENT&suggestionId=tv+smart+tv%7CTelevisions&requestId=deed6b2c-ff89-42d4-a8da-19a5d2e0590a&as-searchtext=tv+smart+tv&p%5B%5D=facets.brand%255B%255D%3DLG")
soup=BeautifulSoup(response.content,'html.parser')
names=soup.find_all('div',class_='_4rR01T')
prices=soup.find_all('div',class_='_30jeq3 _1_WHN1')
ratings=soup.find_all('div',class_='_3LWZlK')
images=soup.find_all('img',class_='_396cs4')
links=soup.find_all('a',class_='_1fQZEK')
image=[]
name=[]
price=[]
rate=[]
link=[]
for i in names[0:20]:
    d=i.get_text()
    name.append(d)
for i in prices[0:20]:
    d=i.get_text()
    price.append(d)
for i in ratings[0:20]:
    d=i.get_text()
    rate.append(float(d))
for i in images[0:20]:
    d=i['src']
    image.append(d)
for i in links[0:20]:
    d="https://www.flipkart.com/"+i['href']
    link.append(d)

mylist5=zip(name,
price,
rate,
image,
link
)

def lg(request):
    return render(request,"lg.html",{'mylist5':mylist5})

#6
#SONY

response=requests.get("https://www.flipkart.com/search?q=tv+smart+tv&sid=ckf%2Cczl&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_2_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_2_na_na_na&as-pos=1&as-type=RECENT&suggestionId=tv+smart+tv%7CTelevisions&requestId=deed6b2c-ff89-42d4-a8da-19a5d2e0590a&as-searchtext=tv+smart+tv&p%5B%5D=facets.brand%255B%255D%3DSONY")
soup=BeautifulSoup(response.content,'html.parser')
names=soup.find_all('div',class_='_4rR01T')
prices=soup.find_all('div',class_='_30jeq3 _1_WHN1')
ratings=soup.find_all('div',class_='_3LWZlK')
images=soup.find_all('img',class_='_396cs4')
links=soup.find_all('a',class_='_1fQZEK')
image=[]
name=[]
price=[]
rate=[]
link=[]
for i in names[0:20]:
    d=i.get_text()
    name.append(d)
for i in prices[0:20]:
    d=i.get_text()
    price.append(d)
for i in ratings[0:20]:
    d=i.get_text()
    rate.append(float(d))
for i in images[0:20]:
    d=i['src']
    image.append(d)
for i in links[0:20]:
    d="https://www.flipkart.com/"+i['href']
    link.append(d)

mylist6=zip(name,
rate,
price,
image,
link
)

def sony(request):
    return render(request,"sony.html",{'mylist6':mylist6})


#7
#Panasonic

response=requests.get("https://www.flipkart.com/search?q=tv+smart+tv&sid=ckf%2Cczl&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_2_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_2_na_na_na&as-pos=1&as-type=RECENT&suggestionId=tv+smart+tv%7CTelevisions&requestId=deed6b2c-ff89-42d4-a8da-19a5d2e0590a&as-searchtext=tv+smart+tv&p%5B%5D=facets.brand%255B%255D%3DPanasonic")
soup=BeautifulSoup(response.content,'html.parser')
names=soup.find_all('div',class_='_4rR01T')
prices=soup.find_all('div',class_='_30jeq3 _1_WHN1')
ratings=soup.find_all('div',class_='_3LWZlK')
images=soup.find_all('img',class_='_396cs4')
links=soup.find_all('a',class_='_1fQZEK')
image=[]
name=[]
price=[]
rate=[]
link=[]
for i in names[0:20]:
    d=i.get_text()
    name.append(d)
for i in prices[0:20]:
    d=i.get_text()
    price.append(d)
for i in ratings[0:20]:
    d=i.get_text()
    rate.append(float(d))
for i in images[0:20]:
    d=i['src']
    image.append(d)
for i in links[0:20]:
    d="https://www.flipkart.com/"+i['href']
    link.append(d)

mylist7=zip(name,
rate,
price,
image,
link
)

def panasonic(request):
    return render(request,"panasonic.html",{'mylist7':mylist7})

#8
#ONIDA

response=requests.get("https://www.flipkart.com/search?q=tv+smart+tv&sid=ckf%2Cczl&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_2_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_2_na_na_na&as-pos=1&as-type=RECENT&suggestionId=tv+smart+tv%7CTelevisions&requestId=deed6b2c-ff89-42d4-a8da-19a5d2e0590a&as-searchtext=tv+smart+tv&p%5B%5D=facets.brand%255B%255D%3DONIDA")
soup=BeautifulSoup(response.content,'html.parser')
names=soup.find_all('div',class_='_4rR01T')
prices=soup.find_all('div',class_='_30jeq3 _1_WHN1')
ratings=soup.find_all('div',class_='_3LWZlK')
images=soup.find_all('img',class_='_396cs4')
links=soup.find_all('a',class_='_1fQZEK')
image=[]
name=[]
price=[]
rate=[]
link=[]
for i in names[0:20]:
    d=i.get_text()
    name.append(d)
for i in prices[0:20]:
    d=i.get_text()
    price.append(d)
for i in ratings[0:20]:
    d=i.get_text()
    rate.append(float(d))
for i in images[0:20]:
    d=i['src']
    image.append(d)
for i in links[0:20]:
    d="https://www.flipkart.com/"+i['href']
    link.append(d)

mylist8=zip(name,
rate,
price,
image,
link
)

def onida(request):
    return render(request,"onida.html",{'mylist8':mylist8})

#9
#TOSHIBA

response=requests.get("https://www.flipkart.com/search?q=tv+smart+tv&sid=ckf%2Cczl&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_2_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_2_na_na_na&as-pos=1&as-type=RECENT&suggestionId=tv+smart+tv%7CTelevisions&requestId=deed6b2c-ff89-42d4-a8da-19a5d2e0590a&as-searchtext=tv+smart+tv&p%5B%5D=facets.brand%255B%255D%3DTOSHIBA")
soup=BeautifulSoup(response.content,'html.parser')
names=soup.find_all('div',class_='_4rR01T')
prices=soup.find_all('div',class_='_30jeq3 _1_WHN1')
ratings=soup.find_all('div',class_='_3LWZlK')
images=soup.find_all('img',class_='_396cs4')
links=soup.find_all('a',class_='_1fQZEK')
image=[]
name=[]
price=[]
rate=[]
link=[]
for i in names[0:20]:
    d=i.get_text()
    name.append(d)
for i in prices[0:20]:
    d=i.get_text()
    price.append(d)
for i in ratings[0:20]:
    d=i.get_text()
    rate.append(float(d))
for i in images[0:20]:
    d=i['src']
    image.append(d)
for i in links[0:20]:
    d="https://www.flipkart.com/"+i['href']
    link.append(d)

mylist9=zip(name,
rate,
price,
image,
link
)

def toshiba(request):
    return render(request,"toshiba.html",{'mylist9':mylist9})

#10
#Lloyd

response=requests.get("https://www.flipkart.com/search?q=tv+smart+tv&sid=ckf%2Cczl&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_2_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_2_na_na_na&as-pos=1&as-type=RECENT&suggestionId=tv+smart+tv%7CTelevisions&requestId=deed6b2c-ff89-42d4-a8da-19a5d2e0590a&as-searchtext=tv+smart+tv&p%5B%5D=facets.brand%255B%255D%3DLloyd")
soup=BeautifulSoup(response.content,'html.parser')
names=soup.find_all('div',class_='_4rR01T')
prices=soup.find_all('div',class_='_30jeq3 _1_WHN1')
ratings=soup.find_all('div',class_='_3LWZlK')
images=soup.find_all('img',class_='_396cs4')
links=soup.find_all('a',class_='_1fQZEK')
image=[]
name=[]
price=[]
rate=[]
link=[]
for i in names[0:20]:
    d=i.get_text()
    name.append(d)
for i in prices[0:20]:
    d=i.get_text()
    price.append(d)
for i in ratings[0:20]:
    d=i.get_text()
    rate.append(float(d))
for i in images[0:20]:
    d=i['src']
    image.append(d)
for i in links[0:20]:
    d="https://www.flipkart.com/"+i['href']
    link.append(d)

mylist10=zip(name,
rate,
price,
image,
link
)

def lloyd(request):
    return render(request,"lloyd.html",{'mylist10':mylist10})

#11
#philips

response=requests.get("https://www.flipkart.com/search?q=tv+smart+tv&sid=ckf%2Cczl&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_2_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_2_na_na_na&as-pos=1&as-type=RECENT&suggestionId=tv+smart+tv%7CTelevisions&requestId=deed6b2c-ff89-42d4-a8da-19a5d2e0590a&as-searchtext=tv+smart+tv&p%5B%5D=facets.brand%255B%255D%3DPHILIPS")
soup=BeautifulSoup(response.content,'html.parser')
names=soup.find_all('div',class_='_4rR01T')
prices=soup.find_all('div',class_='_30jeq3 _1_WHN1')
ratings=soup.find_all('div',class_='_3LWZlK')
images=soup.find_all('img',class_='_396cs4')
links=soup.find_all('a',class_='_1fQZEK')
image=[]
name=[]
price=[]
rate=[]
link=[]
for i in names[0:20]:
    d=i.get_text()
    name.append(d)
for i in prices[0:20]:
    d=i.get_text()
    price.append(d)
for i in ratings[0:20]:
    d=i.get_text()
    rate.append(float(d))
for i in images[0:20]:
    d=i['src']
    image.append(d)
for i in links[0:20]:
    d="https://www.flipkart.com/"+i['href']
    link.append(d)

mylist11=zip(name,
rate,
price,
image,
link
)

def philips(request):
    return render(request,"philips.html",{'mylist11':mylist11})


#12
#BPL

response=requests.get("https://www.flipkart.com/search?q=tv+smart+tv&sid=ckf%2Cczl&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_2_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_2_na_na_na&as-pos=1&as-type=RECENT&suggestionId=tv+smart+tv%7CTelevisions&requestId=deed6b2c-ff89-42d4-a8da-19a5d2e0590a&as-searchtext=tv+smart+tv&p%5B%5D=facets.brand%255B%255D%3DBPL")
soup=BeautifulSoup(response.content,'html.parser')
names=soup.find_all('div',class_='_4rR01T')
prices=soup.find_all('div',class_='_30jeq3 _1_WHN1')
ratings=soup.find_all('div',class_='_3LWZlK')
images=soup.find_all('img',class_='_396cs4')
links=soup.find_all('a',class_='_1fQZEK')
image=[]
name=[]
price=[]
rate=[]
link=[]
for i in names[0:20]:
    d=i.get_text()
    name.append(d)
for i in prices[0:20]:
    d=i.get_text()
    price.append(d)
for i in ratings[0:20]:
    d=i.get_text()
    rate.append(float(d))
for i in images[0:20]:
    d=i['src']
    image.append(d)
for i in links[0:20]:
    d="https://www.flipkart.com/"+i['href']
    link.append(d)

mylist12=zip(name,
rate,
price,
image,
link
)

def bpl(request):
    return render(request,"bpl.html",{'mylist12':mylist12})


def login_user(request):
    if request.method=="POST":
        username=request.POST.get("username")# read 
        password=request.POST.get("password")# read
        user= authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
        return redirect("home")
    return render(request,"login.html")




def register(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        email=request.POST.get("email")
        c = User.objects.create_user(username=username,email=email,password=password)
        c.save()
        return redirect("login")
    
    return render(request,"register.html")



def logout_user(request):
    logout(request)
    return redirect("login")




def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        message=request.POST['message']
        


        c=Contact(name=name,email=email,message=message)
        c.save()
        return redirect("home")

    return render(request,"contact.html")

