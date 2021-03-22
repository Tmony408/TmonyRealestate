from django.shortcuts import render
from django.http import HttpResponse
from realtors.models import Realtor
from listings.models import Listing
from listings.choices import states, bedroom, prices
# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published = True) [:3]
    homeContent= {
        'listings': listings,
        'states' : states,
        'prices' : prices,
        'bedroom' : bedroom
    } 
    return render(request,'pages/index.html', homeContent)

def about(request):
    realtors= Realtor.objects.order_by('-hire_date')
    mvp = Realtor.objects.all().filter(is_mvp = True)
    aboutContent ={
        'mvp': mvp,
        'realtors': realtors
        
    }
    return render(request,'pages/about.html', aboutContent)    