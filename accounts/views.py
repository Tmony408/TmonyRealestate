from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from .passval import password_checker
from contacts.models import Contact
# Create your views here.
def register(request):
    if request.method == 'POST':
        # getting values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        #password verification
        if password == password2:
            if len(password) >=8:
                if password_checker(password) == True:
                    
                    #email and username existence
                    if User.objects.filter(email__iexact = email).exists():
                        messages.error(request, 'Email already exists')
                        return redirect('register')

                    elif User.objects.filter(username__iexact = username).exists():
                        messages.error(request, 'Username already exists')
                        return redirect('register')
                    else:
                        #complete registration and login
                        user = User.objects.create_user(
                            first_name=first_name, last_name=last_name, username=username, email=email, password=password
                        )
                        user.save()
                        messages.success(request,'You have been resgistered successfully')
                        return redirect('login')
                else:
                    messages.error(request,'Password must contain Uppercase Lowercase Number')
                    return redirect('register')


            else:
                messages.error(request,'Password must contain 8 characters')
                return redirect('register')


        else:
            messages.error(request,'Passwords do not match')
            return redirect('register')
       
    else:
        return render(request,'accounts/register.html')  
def login(request):
    if request.method == 'POST':
        # login user
        username= request.POST['username']
        password= request.POST['password']
        user= auth.authenticate(username=username, password=password)    
        if user is not None:
            auth.login(request, user)
            messages.success(request,'You are now logged in')
            return redirect('index')
        else:
            messages.error(request,'Incorrect Login Details')
            return redirect('login')
    else:
        return render(request,'accounts/login.html')  
def dashboard(request):
    user_purchase=Contact.objects.order_by('purchase_date').filter(user_id=request.user.id)
    context={
        'contacts': user_purchase,
    }
    return render(request,'accounts/dashboard.html', context)  
def logout(request):
    if request.method =='POST':
        auth.logout(request)
        messages.success(request,'You are now logged out')
        return redirect('index')
  