from django.shortcuts import render
from django.http import HttpResponse ,HttpResponseNotFound ,HttpResponseRedirect
from django.urls import reverse

monthly_chal ={
    "january":"Walk 20KM at January Month",
    "february":'Code Everyday At February Month',
    "march":'Eat Non-Veg Everyday At March Month',
    "april" :"Walk 20KM at January Month",
    "may" :'Code Everyday At February Month',
    "june" :'Eat Non-Veg Everyday At March Month',
    "july" :"Walk 20KM at January Month",
    "augest":'Code Everyday At February Month',
    "september":'Eat Non-Veg Everyday At March Month',
    "october" :"Walk 20KM at January Month",
    "november":'Code Everyday At February Month',
    "december" :"Walk 20KM at January Month",
}
def index(request):
    list_item=""
    months=list(monthly_chal.keys())
    for month in months:
        cap=month.capitalize()
        month_path =reverse("month-challenge",args=[month])
        list_item+=f"<li> <a href=\"{month_path}\">{cap}</a> </li>"

    
    response_data =f"<ul>{list_item}</ul>"
    return HttpResponse(response_data)

def monthly_challenges_by_number(request,month):
    months=list(monthly_chal.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid Month")
    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge",args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def all(request,month):
    try:
        mon =monthly_chal[month]
        return HttpResponse(mon)
    except:
        return HttpResponseNotFound("Enter Valid URL")
