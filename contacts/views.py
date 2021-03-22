from django.shortcuts import render,redirect
from .models import Contact
from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.core.mail import send_mail

# Create your views here.

def contacts(request):
    if request.method== 'POST':
        listing = request.POST['listing']
        listing_id = request.POST['listing_id']
        user_id = request.POST['user_id']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        realtor_name = request.POST['realtor_name']
        realtor_email = request.POST['realtor_email']
        

      
        if user_id == 0:
            messages.error(request, 'Login to make Inquiries')
            return redirect('/listings/'+listing_id)
        
        elif Contact.objects.filter(listing__iexact=listing, listing_id=listing_id, user_id=user_id,realtor_name=realtor_name).exists():
            messages.error(request, 'You have made this purchase before')
            return redirect('/listings/'+listing_id)
        else:
            purchase_index=1 
            contact = Contact(listing=listing, listing_id=listing_id, user_id=user_id,purchase_index=purchase_index,
            name=name, email=email, phone=phone, message=message, realtor_name=realtor_name)
            contact.save()
            send_mail(
                'Property Listing Inquiry',
                'There is an inquiry for '+listing+'. You might want to log into the admin to view the info about the inquiry.',
                'tmonyadetula@gmail.com',
                ['adetulatestimony@gmail.com',realtor_email],
                fail_silently=False,
            )
            messages.success(request, 'Thanks for making your first inquiry. The Realtor will reach out to you soon')
            return redirect('/listings/'+listing_id)
            # lcontact=Contact.objects.filter(user_id=user_id)
            # if lcontact:
            #     lastcontact=  Contact.objects.order_by('purchase_date').get(user_id=user_id,) [:1]
            #     pindex=lastcontact.purchase_index
            #     newpindex= int(pindex) +1
            #     purchase_index= str(newpindex)
            #     contact = Contact(listing=listing, listing_id=listing_id, user_id=user_id,purchase_index=purchase_index,
            #     name=name, email=email, phone=phone, message=message, realtor_name=realtor_name)
            #     contact.save()
            #     send_mail(
            #         'Property Listing Inquiry',
            #         'There is an inquiry for '+listing+'. You might want to log into the admin to view the info about the inquiry.',
            #         'tmonyadetula@gmail.com',
            #         ['adetulatestimony@gmail.com',realtor_email],
            #         fail_silently=False,
            #     )
            #     messages.success(request, 'Successful. The Realtor will reach out to you soon')
            #     return redirect('/listings/'+listing_id)
                
                
            # else:
            #     purchase_index='1' 
            #     contact = Contact(listing=listing, listing_id=listing_id, user_id=user_id,purchase_index=purchase_index,
            #     name=name, email=email, phone=phone, message=message, realtor_name=realtor_name)
            #     contact.save()
            #     send_mail(
            #         'Property Listing Inquiry',
            #         'There is an inquiry for '+listing+'. You might want to log into the admin to view the info about the inquiry.',
            #         'tmonyadetula@gmail.com',
            #         ['adetulatestimony@gmail.com',realtor_email],
            #         fail_silently=False,
            #     )
            #     messages.success(request, 'Thanks for making your first inquiry. The Realtor will reach out to you soon')
            #     return redirect('/listings/'+listing_id)
                
      
    else:
        return render(request, 'listings/listing.html')
