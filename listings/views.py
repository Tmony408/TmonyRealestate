from django.shortcuts import get_object_or_404, render
from .models import Listing
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import states, bedroom, prices

# Create your views here.


def index(request):
    listings= Listing.objects.order_by('-list_date').filter(is_published = True)
    paginator = Paginator(listings, 1)
    page= request.GET.get('page')
    paged_listings= paginator.get_page(page)
    textcontent = {'listings' : paged_listings}
    return render(request,'listings/listings.html', textcontent )

def listing(request, listing_id):
    listing= get_object_or_404(Listing, pk = listing_id)
    listingContext= {
        'listing': listing
    }
    return render(request,'listings/listing.html', listingContext)

def search(request):
    
    querylist = Listing.objects.order_by('-list_date')

    # keywords 
    if 'keywords' in request.GET:
        keywords= request.GET['keywords']
        if keywords:
            querylist= querylist.filter(description__icontains= keywords)

    #  city
    if 'city' in request.GET:
        city= request.GET['city']
        if city:
            querylist= querylist.filter(city__icontains=city )

    #  state
    if 'state' in request.GET:
        state= request.GET['state']
        if state:
            querylist= querylist.filter(state__iexact=state )

    #  bedrooms
    if 'bedrooms' in request.GET:
        bedrooms= request.GET['bedrooms']
        if bedrooms :
            querylist= querylist.filter(bedrooms__lte=bedrooms )

    #  price
    if 'price' in request.GET:
        price= request.GET['price']
        if price:
            querylist= querylist.filter(price__lte= price)

    
    searchContext ={
        'states' : states,
        'bedroom' : bedroom,
        'prices' : prices,
        'listings' : querylist,
        'values' : request.GET 
    }
    return render(request,'listings/search.html', searchContext )