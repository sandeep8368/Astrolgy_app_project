from django.shortcuts import render
from django.http import HttpResponse
import datetime,random
# Create your views here.
def display_view(request):
    time = datetime.datetime.now()
    hr = time.hour
    if hr < 12:
        s = "Morning"
    elif hr <16:
        s = "Afternoon"
    elif hr < 21:
        s = "Evening"
    else:
        s = "Night"
    name_list = ["SANDEEP","Shivam","Kartik","Suraj","Partik"]
    crush_list = ["KIARA","RASMIKA","TAMANAH","KASHISH","JENNIFER"]
    msg_list = ["Very soon you get the job",
           "Dont drink water drink beer",
           "Golden days ahead",
           "Work is worship"]
    name = random.choice(name_list)
    crush = random.choice(crush_list)
    msg = random.choice(msg_list)
    my_dict = {"name":name,
               "crush":crush,
               "msg":msg,
               "greet":s,
               "time":time
               }
    return render(request,'html/index.html',context=my_dict)



def Contact_view(request):
    return HttpResponse("Contact us page")


def about_view(request):
    return HttpResponse("About us page")